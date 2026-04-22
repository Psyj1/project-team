import cv2
from ultralytics import YOLO
import serial
import time

# Configurações
PORTA_ARDUINO = '/dev/ttyUSB0'  # MUDE PRA SUA PORTA
BAUD_RATE = 9600

# Conecta no Arduino
arduino = serial.Serial(PORTA_ARDUINO, BAUD_RATE)
time.sleep(2)

# Carrega modelo
model = YOLO("yolov8n.pt")

# Abre câmera
cap = cv2.VideoCapture(0)

def contar_carros(results):
    carros = 0
    for r in results:
        for box in r.boxes:
            if model.names[int(box.cls[0])] == "car":
                carros += 1
    return carros

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model(frame)
    carros = contar_carros(results)
    
    # Lógica do semáforo
    if carros > 0:
        arduino.write(b'A')  # libera via A
        print(f"Carros: {carros} -> Comando A (verde)")
    else:
        arduino.write(b'B')  # libera via B
        print(f"Carros: {carros} -> Comando B (vermelho)")
    
    # Interface
    cv2.putText(frame, f"Carros: {carros}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow("Smart Traffic", frame)
    
    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()