import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    frame = cv2.cvtColor(cv2.flip(cam.read()[1], 1), cv2.COLOR_BGR2RGB)

    if lmp := face_mesh.process(frame).multi_face_landmarks:
        nose = lmp[0].landmark[1]
        pyautogui.moveTo(screen_w * nose.x, screen_h * nose.y)

    cv2.imshow('Nose Controlled Mouse', frame)
    cv2.waitKey(1)