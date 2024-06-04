import torch
from PIL import Image
from matplotlib import pyplot as plt
from ultralytics import YOLO

# YOLOv8 모델 로드
model = YOLO('yolov8n.pt')

# 이미지 로드
img_path = "/home/taepark/goinfre/proj/1.png"
image = Image.open(img_path)

# 검출 실행
results = model(img_path)

# 결과 확인 및 표시
if isinstance(results, list):
    # 결과가 리스트인 경우, 각 결과에 대해 처리
    for result in results:
        # 이 부분에서는 결과가 이미지 데이터를 포함하고 있다고 가정
        # matplotlib을 사용하여 이미지 표시
        plt.imshow(result)
        plt.axis('off')  # 축 정보 제거
        plt.show()
else:
    # 결과가 단일 객체인 경우
    img_with_boxes = results.render()[0]  # render 메서드 호출
    plt.imshow(img_with_boxes)
    plt.axis('off')
    plt.show()
