# import libraries
import cv2
import face_recognition

video_capture = cv2.VideoCapture(0)

# face lokasyon listesi
face_locations = []

while True:


    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)

    for top, right, bottom, left in face_locations:
        # algılanan yüzün etrafına çerçeve çiz
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    # Çıkmak için q ya basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()