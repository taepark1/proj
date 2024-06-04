import cv2
import queue
import threading

# video_capture 함수는 위에서 제공한 그대로 사용

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
    cap.release()


def display_frames(queue):
    """ 큐에서 프레임을 가져와 화면에 표시 """
    while True:
        if not queue.empty():
            frame = queue.get()
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.destroyAllWindows()

def main():
    cap = cv2.VideoCapture(0)  # 0은 기본 카메라
    frame_queue = queue.Queue()
    darknet_image_queue = queue.Queue()

    # 비디오 캡처 스레드 시작
    capture_thread = threading.Thread(target=video_capture, args=(cap, frame_queue, darknet_image_queue))
    capture_thread.start()

    # 디스플레이 스레드 시작
    display_thread = threading.Thread(target=display_frames, args=(frame_queue,))
    display_thread.start()

    # 스레드가 종료되기를 기다림
    capture_thread.join()
    display_thread.join()

    cap.release()
    

    #-----
#    while cap.isOpened():
#        # Read a frame from the video
#        success, frame = cap.read()
#
#        if success:
            # Run YOLOv8 inference on the frame
            #results = model(frame)

            # Visualize the results on the frame
            #annotated_frame = results[0].plot()

            # Display the annotated frame
#            cv2.imshow("YOLOv8 Inference", frame)

            # Break the loop if 'q' is pressed
#            if cv2.waitKey(1) & 0xFF == ord("q"):
#                break
#        else:
            # Break the loop if the end of the video is reached
#            break


if __name__ == '__main__':
    main()
