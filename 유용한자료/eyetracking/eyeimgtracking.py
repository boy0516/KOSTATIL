import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
width, height=1280,720
cap.set(3, width) #폭 설정
cap.set(4, height) #넓이 설정

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
eye=[7,33,130,133,144,145,153,154,155,157,158,159,160,161,163,173,246]
# eye2=[249,263,359,362,373,374,380,381,382,384,385,386,387,388,390,398,466]

area = [height,0,width,0]

def areaSelect(x,y):
    if area[0] > y:
        area[0] = y
    if area[1] < y:
        area[1] = y
    if area[2] > x:
        area[2] = x
    if area[3] < x:
        area[3] = x

while True:
    area = [height,0,width,0]
    _, image = cap.read(1)
    _, image2 = cap.read()
    image = cv2.flip(image,1)
    image2 = cv2.flip(image2,1)

    image = cv2.Canny(image, 100, 150)

    result = face_mesh.process(image2)
    try:
        for facial_landmarks in result.multi_face_landmarks:
            
            # print(facial_landmarks)
            for i in eye:
                # image2 = copy.deepcopy(image)
                pt1 = facial_landmarks.landmark[i]
                x = int(pt1.x * width)
                y = int(pt1.y * height)
                areaSelect(x,y)
                cv2.circle(image2, (x,y), 1, (0,0,255), -1)
                # cv2.putText(image,str(i),(x,y),0,0.5,(0,0,255))
    except:
        pass


    print(area)
    for i in range(area[0]-10,area[1]):
        for j in range(area[2],area[3]):
    # for i in range(0,1280):
    #     for j in range(0,720):    
            
            if 255 == int(image[i,j]):
                cv2.circle(image2, (j,i), 1, (255,255,255), -1)
            # cv2.circle(image_gray, (j,i), 1, (255,0,0), -1)
        # print()
    # print('###########')
    cv2.imshow("frame",image)
    cv2.waitKey(1)
    cv2.imshow("image",image2)
    cv2.waitKey(1)
    
    


# # try:
# #     for facial_landmarks in result.multi_face_landmarks:
        
# #         # print(facial_landmarks)
# #         for i in eye:
# #             # image2 = copy.deepcopy(image)
# #             pt1 = facial_landmarks.landmark[i]
# #             x = int(pt1.x * width)
# #             y = int(pt1.y * height)
# #             print(i,x,y)
# #             areaSelect(x,y)

            
# #             # cv2.circle(image_gray, (x,y), 1, (0,0,255), -1)

# #             # cv2.putText(image,str(i),(x,y),0,0.5,(0,0,255))
# # except:
# #     pass

# image_gray = cv2.Canny(image_gray, 100, 150)
# # for i in range(area[0],area[1]):
# #     for j in range(area[2],area[3]):
        
#     #     print(image_gray[j,i], end ="/")
#     #     # print(int(image_gray[j,i][0])+int(image_gray[j,i][1])+int(image_gray[j,i][2]))
#     #     # total += int(image_gray[j,i][0])+int(image_gray[j,i][1])+int(image_gray[j,i][2])
#     #     if 140>int(image_gray[j,i]):
#     #         cv2.circle(image_gray, (j,i), 1, (0,0,255), -1)
#     #     # cv2.circle(image_gray, (j,i), 1, (255,0,0), -1)
#     # print()

# # print(total//((area[1]-area[0])*(area[3]-area[2])))
# # for i in range(area[0],area[1]):
# #     for j in range(area[2],area[3]):        
        

# cv2.imshow("Image",image_gray)
# cv2.waitKey(1)



