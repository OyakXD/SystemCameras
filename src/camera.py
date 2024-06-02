import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error ao abrir a câmera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error ao capturar o frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video em escala cinza", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()