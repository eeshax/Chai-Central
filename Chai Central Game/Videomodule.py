import cv2
import pygame

window_name = "Chai Central"
interframe_wait_ms = 30

cap = cv2.VideoCapture("Finalpiece.mp4")
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while (True):
    ret, frame = cap.read()
    if not ret:
        print("Reached end of video, exiting.")
        break

    cv2.imshow(window_name, frame)
    if cv2.waitKey(interframe_wait_ms) & 0x7F == ord("s"):
        print("Exit requested.")
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        break

cap.release()
cv2.destroyAllWindows()
