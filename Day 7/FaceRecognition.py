import cv2, os, numpy

haar = 'haarcascade_frontalface_default.xml'
dts = 'dataset'
(images, labels, names, id) = ([], [], {}, 0)

for (subdir, dirs, files) in os.walk(dts):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dts, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1

(images, labels) = [numpy.array(lis) for lis in [images, labels]]
(width, height)= (100,100)

# model = cv2.face.LBPHFaceRecognizer_create()
model = cv2.face.LBPHFaceRecognizer_create()

model.train(images, labels)

faceCascade = cv2.CascadeClassifier(haar)

cam = cv2.VideoCapture(1)
cnt = 0

while True:
    _,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
        face = gray[y:y+h, x:x+w]
        faceResize = cv2.resize(face, (width, height), interpolation=cv2.INTER_AREA)

        prediction = model.predict(faceResize)
        # cv2.rectangle(img)
        if(prediction[1] < 800):
            textonImg = names[prediction[0]]
            cv2.putText(img, textonImg, (x, y-20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cnt = 0
        else:
            print("Entered else......")
            cnt+=1
            if(cnt>150):
                cv2.putText(img, "Unknown face", (x-10, y-10), cv2.putText(img, '%s-%.0f' % (names[prediction[0]], prediction[1]), (x-10, y-20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, float(255), 2), (255,255, 0), 2)
                cv2.imwrite('unknown.png', img)
                cnt=0

    cv2.imshow('Face recognition', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()