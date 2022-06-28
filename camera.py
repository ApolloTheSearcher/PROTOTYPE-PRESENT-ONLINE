import cv2

cam = cv2.VideoCapture(0)
while True:
    retV, img = cam.read()
    cv2.imshow('WebCam', img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
cam.release()
cv2.destroyAllWindows()