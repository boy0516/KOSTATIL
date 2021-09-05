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
