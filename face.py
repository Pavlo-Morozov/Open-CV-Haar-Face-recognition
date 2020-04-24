import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\HonorT\.virtualenvs\Open_cv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\HonorT\.virtualenvs\Open_cv\Lib\site-packages\cv2\data\haarcascade_eye.xml')
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
img = cv2.imread("photo5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.5, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()