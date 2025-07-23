import cv2
from cvzone.HandTrackingModule import HandDetector
from controller import LEDController
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
led_controller = LEDController()

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        fingers = detector.fingersUp(hands[0])
        finger_count = sum(fingers)

        print(f"Fingers: {finger_count}")
        led_controller.turn_on_led(finger_count)

    else:
        led_controller.turn_off_all()

    cv2.imshow("Hand Detection", img)
    if cv2.waitKey(1) == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
