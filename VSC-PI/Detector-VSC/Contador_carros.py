import cv2
from ultralytics import YOLO

# Carregar modelo
model = YOLO("yolov8n.pt")

# Webcam ou vídeo
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    car_count = 0
    person_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "car":
                car_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])


                # desenhar caixa
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.putText(frame, "car", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                            (0,255,0), 2)
                
            elif label == "person":
                        person_count += 1

                        x1, y1, x2, y2 = map(int, box.xyxy[0])


                        # desenhar caixa
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                        cv2.putText(frame, "person", (x1, y1-10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                    (0,255,0), 2)

    # mostrar contador na tela
    cv2.putText(frame, f"Carros na tela: {car_count}", (20,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0,0,255), 2)
    
    cv2.putText(frame, f"Pessoas na tela: {person_count}", (20,90),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0,0,255), 2)

    cv2.imshow("Contador", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()