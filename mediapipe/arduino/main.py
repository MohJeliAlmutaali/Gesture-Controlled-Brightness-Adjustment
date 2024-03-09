from detect_open_index_finger import detect_open_index_finger
import cv2

def main():
    # Mulai webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Deteksi jari telunjuk terbuka
        frame = detect_open_index_finger(frame)
        resized_frame = cv2.resize(frame,(700, 550))
        # Tampilkan frame
        cv2.imshow('Open Index Finger Detection', resized_frame)

        # Tunggu tombol 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
