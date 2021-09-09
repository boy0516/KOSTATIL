import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
width, height=1280,720
cap.set(3, width) #폭 설정
cap.set(4, height) #넓이 설정
# Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

while True:
    # Image
    _, image = cap.read()

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Facial landmarks
    result = face_mesh.process(rgb_image)
    # print(result)

    for facial_landmarks in result.multi_face_landmarks:
        pt1 = facial_landmarks.landmark[0]
        x = int(pt1.x * width)
        y = int(pt1.y * height)
        z = pt1.z
        print(z)
        cv2.circle(image, (x,y), 3, (255,0,0), -1)
        # print(facial_landmarks)
        # for i in range(len(facial_landmarks.landmark)):
        #     pt1 = facial_landmarks.landmark[i]
        #     x = int(pt1.x * width)
        #     y = int(pt1.y * height)
        #     cv2.circle(image, (x,y), 3, (255,0,0), -1)


    cv2.imshow("Frame",image)
    cv2.waitKey(1)