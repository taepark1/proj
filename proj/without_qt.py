import cv2
from ultralytics import YOLO
import sys
import argparse
from queue import Queue
import time
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
from threading import Thread

# Load the YOLOv8 model
#model = YOLO('/home/taepark/goinfre/asdf.v1i.yolov8/runs/detect/train/weights/best.pt')
model = YOLO('yolov8n.pt')
# 동영상 파일 사용시
#video_path = "/home/taepark/goinfre/New_sample/data/REAL/WORD/01/NIA_SL_WORD1501_REAL01_D.mp4"
#video_path = cv2.VideoCapture(0)
one = {'person': 'person output', 'chairs': 'chair output'}

def parser():
    parser = argparse.ArgumentParser(description="YOLO Object Detection")
    parser.add_argument("--input", type=str, default=0,
                        help="video source. If empty, uses webcam 0 stream")
    parser.add_argument("--out_filename", type=str, default="",
                        help="inference video name. Not saved if empty")
    parser.add_argument("--weights", default="./model/yolov4-obj_96_best.weights",
                        help="yolo weights path")
    parser.add_argument("--dont_show", action='store_true',
                        help="window inference display. For headless systems")
    parser.add_argument("--ext_output", action='store_true',
                        help="display bbox coordinates of detected objects")
    parser.add_argument("--config_file", default="./cfg/yolov4-obj.cfg",
                        help="path to config file")
    parser.add_argument("--data_file", default="./data/obj.data",
                        help="path to data file")
    parser.add_argument("--thresh", type=float, default=.70,
                        help="remove detections with confidence below this value")
    return parser.parse_args()

def video_capture(cap, frame_queue, darknet_image_queue):
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        #frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #frame_queue.put(frame_rgb)
        frame_queue.put(frame)
        #darknet_image_queue.put(frame_rgb)
        darknet_image_queue.put(frame)
    cap.release()

def inference(cap, args, darknet_image_queue, detections_queue, fps_queue):
    while cap.isOpened():
        darknet_image = darknet_image_queue.get()
        prev_time = time.time()
        detection = model(darknet_image)
        detections_queue.put(detection)
        fps = int(1 / (time.time() - prev_time))
        fps_queue.put(fps)
        print("FPS: {}".format(fps))
    cap.release()

def drawing(cap, args, frame_queue, detections_queue, fps_queue):
    while cap.isOpened():
        frame_resized = frame_queue.get()
        detections = detections_queue.get()
        fps = fps_queue.get()

        if frame_resized is not None:
            for r in detections:
                annotator = Annotator(frame_resized)
                boxes = r.boxes
                for box in boxes:
                    b = box.xyxy[0]
                    c = box.cls
                    label = model.names[int(c)]
                    #if label in list(one.keys()):
                    #    annotator.box_label(b, one.get(label))
                    annotator.box_label(b, model.names[int(c)])
                hand_image = annotator.result()
                cv2.imshow("YOLOv8 Inference", hand_image)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC 키를 누르면 종료
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    args = parser()

    frame_queue = Queue()
    darknet_image_queue = Queue(maxsize=1)
    detections_queue = Queue(maxsize=1)
    fps_queue = Queue(maxsize=1)

    #cap = cv2.VideoCapture(video_path)
    cap = cv2.VideoCapture(0)
    Thread(target=video_capture, args=(cap, frame_queue, darknet_image_queue)).start()
    Thread(target=inference, args=(cap, args, darknet_image_queue, detections_queue, fps_queue)).start()
    Thread(target=drawing, args=(cap, args, frame_queue, detections_queue, fps_queue)).start()
