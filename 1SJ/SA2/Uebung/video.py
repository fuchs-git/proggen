import cv2


# Video laden
video_path = "path_to_your_video.mp4"
video = cv2.VideoCapture(video_path)

frame_number = 0
success, frame = video.read()

while success:
    # Frame anzeigen
    cv2.imshow("Frame", frame)

    # Taste "q" zum Abbrechen, beliebige andere Taste für nächstes Frame
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    success, frame = video.read()
    frame_number += 1

video.release()
cv2.destroyAllWindows()