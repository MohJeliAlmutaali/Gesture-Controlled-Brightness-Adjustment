import cv2
import mediapipe as mp

# Inisialisasi modul MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def detect_open_index_finger(image):
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:

        # Ubah gambar menjadi RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        # Jika tangan terdeteksi
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Periksa posisi ujung jari telunjuk dan MCP
                tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

                # Periksa apakah hanya jari telunjuk yang terbuka
                only_index_finger_open = True
                for landmark in [mp_hands.HandLandmark.MIDDLE_FINGER_TIP, 
                                 mp_hands.HandLandmark.RING_FINGER_TIP,
                                 mp_hands.HandLandmark.PINKY_TIP]:
                    if hand_landmarks.landmark[landmark].y < mcp.y:
                        only_index_finger_open = False
                        break

                if only_index_finger_open:
                    cv2.putText(image, 'Jari Telunjuk Terbuka', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(image, 'Jari Telunjuk Tertutup atau Jari Lain Terbuka', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1)

        return image
