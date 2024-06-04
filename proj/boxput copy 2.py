import cv2
from ultralytics import YOLO

# YOLOv8 모델 로드
model = YOLO('yolov8n.pt')

# 이미지 로드
img_path = "/home/taepark/goinfre/proj/1.png"
img = cv2.imread(img_path)

# 검출 실행
results = model(img)

# 결과가 리스트로 반환된다고 가정하고 각 결과 처리
for result in results:
    # 각 result 객체에 바운딩 박스와 클래스 정보가 있다고 가정
    # 예시: result = {'x1': 100, 'y1': 100, 'x2': 200, 'y2': 200, 'class_id': 1, 'confidence': 0.9}
    x1, y1, x2, y2 = result['x1'], result['y1'], result['x2'], result['y2']
    class_id, confidence = result['class_id'], result['confidence']

    # 바운딩 박스 그리기
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 클래스 이름과 확률을 표시
    label = f"{class_id}: {confidence:.2f}"
    cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# 결과 이미지 표시
cv2.imshow('Detection Results', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
