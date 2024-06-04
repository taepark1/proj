import cv2
import queue
import threading
import time
from queue import Queue
import cv2
from ultralytics import YOLO
import sys
from os import system
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import cv2
import argparse
#import sonmari_video as sv
# Load the YOLOv8 model
#model = YOLO('yolov8n.pt')
model = YOLO('/home/taepark/goinfre/asdf.v1i.yolov8/runs/detect/train/weights/best.pt')

# 동영상 파일 사용시
video_path = "/home/taepark/goinfre/New_sample/data/REAL/WORD/01/NIA_SL_WORD1501_REAL01_L.mp4"
#video_path = "/home/taepark/goinfre/proj/123111.mp4"
cap = cv2.VideoCapture(video_path)



def parser():
    parser = argparse.ArgumentParser(description="YOLO Object Detection")
    parser.add_argument("--input", type=str, default=0,
                        help="video source. If empty, uses webcam 0 stream")
    parser.add_argument("--out_filename", type=str, default="",
                        help="inference video name. Not saved if empty")
    parser.add_argument("--weights", default="./model/yolov4-obj_96_best.weights",
                        help="yolo weights path")
    parser.add_argument("--dont_show", action='store_true',
                        help="windown inference display. For headless systems")
    parser.add_argument("--ext_output", action='store_true',
                        help="display bbox coordinates of detected objects")
    parser.add_argument("--config_file", default="./cfg/yolov4-obj.cfg",
                        help="path to config file")
    parser.add_argument("--data_file", default="./data/obj.data",
                        help="path to data file")
    parser.add_argument("--thresh", type=float, default=.70,
                        help="remove detections with confidence below this value")
    return parser.parse_args()

args = parser()


frame_queue = Queue()
darknet_image_queue = Queue(maxsize=1)
detections_queue = Queue(maxsize=1)
fps_queue = Queue(maxsize=1)

#def model(image):
#    """ 임의의 모델을 시뮬레이션하는 함수. 간단한 예로 객체 리스트를 반환 """
#    return [{'object': 'person', 'confidence': 0.9}, {'object': 'dog', 'confidence': 0.8}]
def video_capture(cap, frame_queue, darknet_image_queue):
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #필요없을듯 ? 리사이즈 불필요
        #frame.shape[0]으로 높이 값 출력가능  # frame.shape = (높이, 너비, 채널) 예: (720, 1280, 3)
        #frame_resized = cv2.resize(frame_rgb, (416, 416),
        #                           interpolation=cv2.INTER_LINEAR)
        frame_queue.put(frame_rgb)
        
        #img_for_detect = model()
        #필요없는듯?

        #img_for_detect = darknet.make_image(width, height, 3)
        
        #darknet.copy_image_from_bytes(img_for_detect, frame_resized.tobytes())
        darknet_image_queue.put(frame_rgb)
        print("video_capture : end") 
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
        print("inference : end") 
    cap.release()

def display_detections(detection_queue):
    """ 검출된 객체를 표시하는 함수 """
    while True:
        detections = detection_queue.get()
        if detections is None:
            break
        print("Type of detection:", type(detections))  # 객체의 타입 출력
        print("------------------------------1")
        print("Content of detection:", detections)  # 객체의 내용 출력
        print("------------------------------2")
        print("Detected objects and their paths3:")
        for result in detections:
            if hasattr(result, 'probs'):  # Check if the 'path' attribute exists
                print("Probs:3", result.probs)
            else:
                print("No path data available for this detection.")
        #print("Detected objects:", detections.path)


#        for result in detections:
#            if hasattr(result, 'boxes'):
#                # boxes 정보 가져오기 (여기서 .xyxy[0]는 첫 번째 이미지의 박스 리스트를 반환)
#                boxes = result.boxes.xyxy[0]
#                names = result.names  # names 정보 가져오기
#                for box in boxes:
#                    # 박스의 각 값에 대해 직접 인덱스를 사용하여 접근
#                    x1, y1, x2, y2, conf, cls = box[0].item(), box[1].item(), box[2].item(), box[3].item(), box[4].item(), int(box[5].item())
#                    class_name = names[cls]  # 클래스 인덱스를 사용하여 이름을 가져옵니다.
#                    print(f"Object: {class_name}, Confidence: {conf:.2f}")
#            else:
#                print("Detection format is not supported.")


def main():
    cap = cv2.VideoCapture(video_path)  # 올바른 카메라 또는 비디오 파일 경로
    args = {}
    frame_queue = queue.Queue()
    darknet_image_queue = queue.Queue()
    detections_queue = queue.Queue()
    fps_queue = queue.Queue()

    # 영상을 읽어 처리 큐에 추가하는 스레드
    capture_thread = threading.Thread(target=video_capture, args=(cap, frame_queue, darknet_image_queue))
    # 객체 검출 및 FPS 계산 스레드
    inference_thread = threading.Thread(target=inference, args=(cap, args, darknet_image_queue, detections_queue, fps_queue))
    # 검출 결과를 표시하는 스레드
    display_thread = threading.Thread(target=display_detections, args=(detections_queue,))

    capture_thread.start()
    inference_thread.start()
    display_thread.start()

    capture_thread.join()
    inference_thread.join()
    display_thread.join()

    cap.release()


if __name__ == '__main__':
    main()
