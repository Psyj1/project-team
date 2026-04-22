import cv2
from ultralytics import YOLO

# Carregar modelo YOLO
model = YOLO("yolov8n.pt")  # baixa automaticamente

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Rodar detecção
    results = model(frame)

    # Desenhar resultados
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0,255,0), 2)

    cv2.imshow("Detecção de Objetos", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()