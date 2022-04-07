import cv2


cap1 = cv2.VideoCapture(0, cv2.CAP_V4L)
cap1.set(3, 80)
cap1.set(4, 40)


while True:
    
    ret1, frame1 = cap1.read()
    cv2.imshow('ve', frame1)
    
        
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap1.release()
cv2.destroyAllWindows()