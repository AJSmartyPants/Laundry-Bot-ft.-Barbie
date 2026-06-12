import cv2
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not camera.isOpened():
     raise RuntimeError("Could not open webcam")

try:
     while True:
          success, frame = camera.read()
          if not success:
               print("Failed to read a camera frame")
               break
          cv2.imshow("Lenovo Webcam", frame)
          if cv2.waitKey(1) & 0xFF == ord('q'):
               break
finally:
     camera.release()
     cv2.destroyAllWindows()