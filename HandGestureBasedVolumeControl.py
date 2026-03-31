import cv2
import math
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = HandDetector(detectionCon=0.8)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]
while True:
    try:
        success, img = cap.read()
        if not success or img is None:
            continue

        hands, img = detector.findHands(img)

        if hands and len(hands) > 0:
            lmList = hands[0]['lmList']

            if lmList:
                x1, y1 = lmList[4][0], lmList[4][1]
                x2, y2 = lmList[8][0], lmList[8][1]

                # Draw
                cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                length = math.hypot(x2 - x1, y2 - y1)
                vol = np.interp(length, [30, 200], [volMin, volMax])
                volBar = np.interp(length, [30, 200], [400, 150])
                volPer = np.interp(length, [30, 200], [0, 100])
                try:
                    volume.SetMasterVolumeLevel(vol, None)
                except:
                    print("Volume control failed")
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
                cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(volPer)} %', (40, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Volume Control", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print("Error:", e)

cap.release()
cv2.destroyAllWindows()