import cv2


cap1 = cv2.VideoCapture(2)
cap1.set(3, 480)
cap1.set(4, 320)


cap2 = cv2.VideoCapture(0)
cap2.set(3, 480)
cap2.set(4, 320)

while True:
    
    ret1, frame1 = cap1.read()
    cv2.imshow('ve', frame1)
    
    
    ret2, frame2 = cap2.read()
    cv2.imshow('ve1', frame2)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()