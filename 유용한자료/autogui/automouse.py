import cv2
import mediapipe as mp
import pyautogui

# 마우스 이동 (x 좌표, y 좌표)
pyautogui.moveTo(500, 500)

# 마우스 이동 (x 좌표, y 좌표 2초간)
pyautogui.moveTo(100, 100)  

# 마우스 이동 ( 현재위치에서 )
pyautogui.moveRel(200, 300)

# 마우스 클릭
pyautogui.click()

# 2초 간격으로 2번 클릭
pyautogui.click(clicks= 2, interval=2)

# 더블 클릭
pyautogui.doubleClick()

# 오른쪽 클릭
pyautogui.click(button='right')

# 스크롤하기 
pyautogui.scroll(10)

# 드래그하기
pyautogui.drag(0, 300, 1, button='left')



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