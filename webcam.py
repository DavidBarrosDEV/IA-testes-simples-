import cv2
import face_recognition

# Inicialize a webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Captura um quadro da webcam
    ret, frame = video_capture.read()

    # Encontre as coordenadas dos rostos no quadro
    face_locations = face_recognition.face_locations(frame)

    # Desenhe um retângulo ao redor de cada rosto
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Exiba o quadro resultante
    cv2.imshow('Video', frame)

    # Saia do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a webcam e feche a janela
video_capture.release()
cv2.destroyAllWindows()
