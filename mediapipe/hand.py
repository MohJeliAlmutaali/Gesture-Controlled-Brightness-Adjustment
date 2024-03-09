import cv2
import mediapipe as mp
import math

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Buka kamera
cap = cv2.VideoCapture(0)  # Ganti 0 dengan nomor kamera yang ingin Anda gunakan, misalnya 1, 2, dll.

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Konversi gambar ke RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Deteksi tangan dalam gambar
    results = hands.process(frame_rgb)

    # Inisialisasi variabel untuk koordinat ujung jari telunjuk dan jempol
    fingertip_coords = None
    thumbtip_coords = None

    # Jika tangan ditemukan
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for idx, landmark in enumerate(hand_landmarks.landmark):
                # Koordinat ujung jari telunjuk (index finger)
                if idx == mp_hands.HandLandmark.INDEX_FINGER_TIP.value:
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    
                    # Simpan koordinat ujung jari telunjuk
                    fingertip_coords = (cx, cy)

                    # Gambar lingkaran pada ujung jari telunjuk
                    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                # Koordinat ujung jari jempol (thumb tip)
                elif idx == mp_hands.HandLandmark.THUMB_TIP.value:
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    
                    # Simpan koordinat ujung jari jempol
                    thumbtip_coords = (cx, cy)

                    # Gambar lingkaran pada ujung jari jempol
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    # Hitung jarak antara ujung jari telunjuk dan jempol
    if fingertip_coords and thumbtip_coords:
        distance = math.sqrt((fingertip_coords[0] - thumbtip_coords[0]) ** 2 + (fingertip_coords[1] - thumbtip_coords[1]) ** 2)

        # Tampilkan jarak pada layar
        cv2.putText(frame, f'Jarak: {distance:.2f} pixels', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Tampilkan frame
    cv2.imshow('Fingertip Distance', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
