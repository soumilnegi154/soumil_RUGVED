
from collections import deque
import numpy as np
import cv2

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=64)
vs = cv2.VideoCapture(r"soumil_RUGVED\task3\Ball_Tracking.mp4")
while True:
	istrue, frame = vs.read()
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	(cnts, *_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	center = None
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
	pts.appendleft(center)
	for i in range(1, len(pts)):
		if pts[i - 1] is None or pts[i] is None:
			continue
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), 5)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

vs.release()
cv2.destroyAllWindows()