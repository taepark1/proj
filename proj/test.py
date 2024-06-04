import cv2

# 동영상 파일 사용시
#video_path = "/home/taepark/goinfre/proj/123.mp4"
#cap = cv2.VideoCapture(video_path)

# webcam 사용시
cap = cv2.VideoCapture(0)


# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Display the frame as is without YOLOv8 inference
        cv2.imshow("Video Frame", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
