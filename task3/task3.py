import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescale(frame, scale=0.75):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

def rotate(img, angle, rotpoint=None):
    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rotmat, dimension)

capture = cv.VideoCapture(r"soumil_RUGVED\task3\Ball_Tracking.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale(frame, 1)

    #drawing shapes and writing text
    #cv.rectangle(frame_resized, (0,0), (250,250), (0,255,0), thickness=2)
    #cv.putText(frame_resized, "diddy ahh blud", (225,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)


    blank = np.zeros(frame_resized.shape[:2], dtype='uint8')

    #grayscale
    frame_grey = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
    #blur
    frame_blur = cv.GaussianBlur(frame_resized, (11,11), cv.ADAPTIVE_THRESH_GAUSSIAN_C)
    #edge cascade
    frame_canny = cv.Canny(frame_resized, 125, 175)
    #dilating the image
    frame_dilate = cv.dilate(frame_canny, (5,5), iterations=1)
    #resize
    frame_cv_resized = cv.resize(frame_resized, (600, 600))
    #cropping
    frame_cropped = frame_resized[50:200, 60:300]


    #translating
    frame_translated = translate(frame_resized, 100, 100)
    #rotating
    frame_rotated = rotate(frame_resized, 45)
    #flipping
    frame_flipped = cv.flip(frame_resized, 0)


    # contours
    # contours, hierarchies = cv.findContours(frame_canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    # print(len(contours))
    # cv.drawContours(frame_resized, contours, -1, (0,0,255), 1)


    #colour spaces
    #RBG TO HSV
    frame_hsv = cv.cvtColor(frame_blur, cv.COLOR_RGB2HSV)
    #RGB TO LAB(L*A*B)
    frame_lab = cv.cvtColor(frame_resized, cv.COLOR_RGB2LAB)

    
    #color channels
    frame_blue, frame_green, frame_red = cv.split(frame_resized)
    frame_merged = cv.merge([frame_blue, blank, blank])



    # #color histogram
    # plt.figure()
    # plt.title("Color Histogram")
    # plt.xlabel('Bins')
    # plt.ylabel('# of pixels')
    # colors = ("b", 'g', 'r')
    # for i, col in enumerate(colors):
    #     hist = cv.calcHist([frame_resized], [i], None, [256], [0,256])
    #     plt.plot(hist, color=col)
    #     plt.xlim([0,256])
    # plt.show()
    

    #threshholding
    #simple threshholding
    threshhold, frame_thresh = cv.threshold(frame_grey, 200, 255, cv.THRESH_BINARY)
    threshhold, frame_thresh_inv = cv.threshold(frame_grey, 100, 255, cv.THRESH_BINARY_INV)
    #adaptive threshholding
    frame_thresh_adaptive = cv.adaptiveThreshold(frame_grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)



    #face detection using haar cascades
    haar_cascade = cv.CascadeClassifier(r'soumil_RUGVED\task3\haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(frame_grey, scaleFactor=1.1, minNeighbors=5)
    #print(f"number of faces found = {len(faces_rect)}")
    # for (x,y,w,h) in faces_rect:
    #     cv.rectangle(frame_resized, (x,y), (x+w,y+h), (0,255,0), thickness=2)


    #tracking green ball using mask
    frame_mask = cv.inRange(frame_hsv, (29,86,6), (64,255,255))
    frame_mask = cv.erode(frame_mask, None, iterations=2)
    frame_mask = cv.dilate(frame_mask, None, iterations=2)
    contours, hierarchies = cv.findContours(frame_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i in contours:
        # ball_rect = cv.boundingRect(i)
        if cv.contourArea(i) > 500:
            x, y, w, h = cv.boundingRect(i)
            cv.rectangle(frame_resized, (x,y), (x+w,y+h), (0,255,0), thickness=2)
            # cv.line(frame_resized, contours[contours.index(i)], contours[contours.index[i] - 1], (0,0,255), thickness=2)

    




    cv.imshow("vid", frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()