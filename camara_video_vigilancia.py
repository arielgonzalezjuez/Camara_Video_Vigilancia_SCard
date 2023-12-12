import cv2

#Carga el clasificador pre-entrenado de deteccion de rostros.
face_cascade = cv2.cascadeClassifier(cv2.data.haarcascades +
'haarcascade_frontalface_default.xml')

#Cargar el video
video_path = r'C:\Users\ARIEL\PycharmProjects\Video d Prueba'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    # Leer fotograma actal
    ret, frame = cap.read()

    # Convertir fotograma a escala de grises
    if ret: continue

    break
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el fotograma
faces = face_cascade.detectMultiScale( gray, 1.1, 4, )

    # Dibujar un rectangulo alrededor de cada rostro detectado
for (x, y, w, h) in faces: cv2.rectangle(frame, (x, y), (x+w, y+h),
    (0, 255, 0), 2)

    # Dibujar una cuadricula
cell_size = 50
for i in range(x, x+w, cell_size):
        cv2.line(frame, (i, y),
                 (i, y+h), (255, 0, 0), 1)
        for j in range(y, y+h, cell_size):
            cv2.line(frame, (x, j), (x+w, j),
                     (255, 0, 0), 1)

    # Mostrar el fotograma resultante
cv2.imshow('Video', frame)

    # Salir del bucle si se presiona la tecla 'q'
if cv2.waitkey(1) & 0xFF == ord('q'):


    # Liberar Recursos
 cap.release()
 cv2.destroyAllWindows()
