import cv2
import numpy as np
import time
import autopy
import HandTrackingModule as htm
# import pyautogui

wCam, hCam = 640, 480
frameR = 100
smoothening = 5

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
plocX, plocY = 0, 0
clocX, clocY = 0, 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = []
        fingers.append(lmList[8][2] < lmList[6][2])  # index
        fingers.append(lmList[12][2] < lmList[10][2])  # middle

        if fingers[0] and not fingers[1]:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            autopy.mouse.move(wScr - clocX, clocY)
            plocX, plocY = clocX, clocY
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

        if fingers[0] and fingers[1]:
            length = np.hypot(x2 - x1, y2 - y1)
            if length < 40:
                autopy.mouse.click()
                time.sleep(0.2)

    cv2.imshow("AI Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
