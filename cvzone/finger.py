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

