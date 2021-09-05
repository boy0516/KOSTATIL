import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8)
startDist = None
scale = 0
cx, cy = 500, 500
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread("qr.png")

    if len(hands)==2:
        #print("Zoom Gesture")
        # print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0])==[1,1,0,0,0] and\
            detector.fingersUp(hands[1])==[1,1,0,0,0]:
            # print("Zoom gesture")
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            # point 8 is the tip of th index finger
            if startDist is None:
                lmList1[8], lmList2[8]
                length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
                # print(length)
                startDist = length
            
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            scale = int((length-startDist)//2)
            cx,cy = info[4:] # 이미지가 두 손가락 포인터의 중심에 있기를 바람.
            print(scale)
    else:
        startDist = None
    
    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1 + scale)//2)*2, ((w1+scale)//2)*2
        img1 = cv2.resize(img1, (newW, newH))

        # 여기에 문제가 발생, 이미지의 크기가 홀수이면 2로 나누어졌을때 크기 1이 손실된다. 그래서 삽입되는 부분에서 문제가 발생
        img[cy-newH//2:cy+newH//2,cx-newW//2:cx+newW//2]= img1
    except:
        pass
    cv2.imshow("Image",img)
    cv2.waitKey(1)



