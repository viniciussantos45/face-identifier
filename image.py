import cv2

xml_haar_cascade = 'haarcascade_frontalface_alt2.xml'

# Carregar classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

# Carrega imagem
imgRGB = cv2.imread('./faces2.jpg')
imgGray = cv2.imread('./faces2.jpg', 0)
faces = faceClassifier.detectMultiScale(imgGray)

for x, y, w, h in faces :
    cv2.rectangle(imgRGB, (x, y), (x+w, y+h), (0,255,0), 2)
cv2.imwrite('faces-cvReader2.jpg', imgRGB)