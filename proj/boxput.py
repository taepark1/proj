import torch
from PIL import Image
from matplotlib import pyplot as plt
from ultralytics import YOLO
import cv2

# YOLOv8 모델 로드
model = YOLO('yolov8n.pt')

# 이미지 로드
img_path = "/home/taepark/goinfre/proj/1.png"
image = Image.open(img_path)

# 검출 실행
results = model(img_path)

# 검출 결과를 numpy 배열로 변환 (올바른 인덱싱이 필요할 수 있음)
img_with_boxes = results.render()[0]

# OpenCV를 사용하여 결과 이미지 표시
cv2.imshow('Detection Results', img_with_boxes)
cv2.waitKey(0)  # 키 입력 대기
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기

# matplotlib을 사용하여 이미지 표시 (선택적)
plt.imshow(img_with_boxes)
plt.axis('off')  # 축 정보 제거
plt.show()
