import cv2
from ultralytics import YOLO

# YOLOv8 모델 로드
model = YOLO('/home/taepark/goinfre/asdf.v1i.yolov8/runs/detect/train/weights/best.pt')

# 비디오 파일 경로
video_path = "/home/taepark/goinfre/New_sample/data/REAL/WORD/01/NIA_SL_WORD1501_REAL01_L.mp4"
cap = cv2.VideoCapture(video_path)

# 비디오 프레임을 통한 루프
while cap.isOpened():
    # 비디오에서 프레임 읽기
    success, frame = cap.read()

    if success:
        # 프레임에 대한 YOLOv8 추론 실행
        results = model(frame)

        # 결과 출력
        if isinstance(results, list):
            # 'results'가 리스트인 경우 직접 처리
            for result in results:
                print(result)
        else:
            # 'results'가 기대한 'Results' 객체인 경우
            if len(results.pred[0]) > 0:
                print("Detections:")
                for det in results.pred[0]:
                    x1, y1, x2, y2, conf, cls = int(det[0]), int(det[1]), int(det[2]), int(det[3]), det[4], int(det[5])
                    print(f"Class: {results.names[int(cls)]}, Confidence: {conf:.2f}, BBox: [{x1}, {y1}, {x2}, {y2}]")
            else:
                print("No detections")
    else:
        break

# 비디오 캡처 객체 해제 및 창 닫기
cap.release()
