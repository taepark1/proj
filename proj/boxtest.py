import torch
from PIL import Image
from matplotlib import pyplot as plt
from ultralytics import YOLO

# 모델 로드
model = YOLO('yolov8n.pt')
#model = YOLO('/home/taepark/goinfre/proj/yolov8/runs/detect/train2/weights/best.pt')

# 이미지 로드
img = "/home/taepark/goinfre/proj/1.png"

# 검출 실행
results = model(img)

# 결과 확인 및 표시
if isinstance(results, list):
    for result in results:
        if hasattr(result, 'show'):
            result.show()  # 각 결과 객체의 show 메서드 호출
        else:
            print("No show method available for the object:", type(result))
else:
    print("Unexpected type of results:", type(results))
# 검출 임계값 설정
model.conf = 0.3  # 낮은 임계값으로 설정하여 더 많은 객체를 검출할 수 있도록 합니다.

# 다시 검출 실행
results = model(img)

if isinstance(results, list):
    for result in results:
        if hasattr(result, 'show'):
            result.show()  # 각 결과 객체의 show 메서드 호출
        else:
            print("No show method available for the object:", type(result))
else:
    print("Unexpected type of results:", type(results))
print("--------------------------------1")
print(dir(model))