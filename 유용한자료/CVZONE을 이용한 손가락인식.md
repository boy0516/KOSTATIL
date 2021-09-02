## CVZONE을 이용한 손가락인식

https://www.youtube.com/watch?v=3xfOa4yeOb0&t=616s

두손으로 옮기기

```
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280) #폭 설정
cap.set(4, 720) #넓이 설정
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200

class DragRect():
    def __init__(self, posCenter, size=[200,200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 <cursor[0] <cx + w // 2 and cy - h // 2 < cursor[1] < cy + h //2 :
            self.posCenter = cursor

rectList = []
for x in range(4):
    rectList.append(DragRect([x*250+150, 150]))
    
while True:
    succes, img = cap.read()
    img = cv2.flip(img, 1) # 좌우 반전
    hands, img = detector.findHands(img)
    if hands:
        lmList1 = hands[0]["lmList"]
        length1, _, img = detector.findDistance(lmList1[8],lmList1[12], img)

        if length1<50:
            cursor = lmList1[8] # 커서는 길이 2의 리스트로 0에는 x좌표 1에는 y좌표가 들어간다
            for rect in rectList:
                rect.update(cursor)
                
        if len(hands)==2:
            lmList2 = hands[1]["lmList"]
            length2, _, img = detector.findDistance(lmList2[8],lmList2[12], img)

            if length2<50:
                cursor2 = lmList2[8] # 커서는 길이 2의 리스트로 0에는 x좌표 1에는 y좌표가 들어간다
                for rect in rectList:
                    rect.update(cursor2)

        

        
    # # Draw solid
    # for rect in rectList:
    #     cx, cy = rect.posCenter
    #     w, h = rect.size
    #     cv2.rectangle(img, (cx-w//2,cy-h//2), (cx+w//2,cy+h//2), colorR, cv2.FILLED) # 이미지에 도형 삽입
    #     cvzone.cornerRect(img,(cx - w //2, cy - h // 2,w, h),20 , rt=0)


    ## Draw Transperency
    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx-w//2,cy-h//2), (cx+w//2,cy+h//2), colorR, cv2.FILLED) # 이미지에 도형 삽입
        cvzone.cornerRect(imgNew,(cx - w //2, cy - h // 2, w, h),20 , rt=0)
    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    cv2.imshow("Image", out)
    cv2.waitKey(1)

```



```
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon = 0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img) # With Draw
    # hands, img = detector.findHands(img, drwa=False) # No Draw
    print(len(hands)) ## 캠에 찍힌 손 개수 보여줌

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] # List of 21 Landmarks points
        bbox1 = hand1["bbox"] # Bounding Box info x, y, w, h
        centerPoint1 = hand1["center"] # center of the hand cx, cy
        handType1 = hand1["type"] # hand Type Left or Right

        # print(len(lmList1), lmList1) # 21개 관절좌표
        # print(bbox1) #손전체 인식 박스
        # print(centerPoint1)# 손중앙좌표
        # print(handType1)
        fingers1 = detector.fingersUp(hand1)
        length, info, img = detector.findDistance(lmList1[8],lmList1[12],img) # 점표시
        # length, info, img = detector.findDistance(lmList1[8],lmList1[12]) # 점 안표시

        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"] # List of 21 Landmarks points
            bbox2 = hand2["bbox"] # Bounding Box info x, y, w, h
            centerPoint2 = hand2["center"] # center of the hand cx, cy
            handType2 = hand2["type"] # hand Type Left or Right

            fingers2 = detector.fingersUp(hand2)
            
            length, info, img = detector.findDistance(lmList2[8],lmList2[12],img) # 점표시, 두점간의 거리확인


    cv2.imshow("Image",img)
    cv2.waitKey(1)

```

