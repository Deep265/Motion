import cv2

c = cv2.VideoCapture('walking.mp4')

boolean,frame1=c.read()
boolean,frame2=c.read()

while c.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    any, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours,any = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 2000:
            continue
        else:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow("Motion Frame",frame1)
    frame1 = frame2
    boolean, frame1 = c.read()

    if cv2.waitKey(40) & 0xFF == ord('d'):
        break
cv2.destroyAllWindows()
c.release()