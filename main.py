import cv2
import mediapipe as mp
import math
import time
import screen_brightness_control as sbc

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Inisialisasi variabel waktu awal
start_time = time.time()

def get_finger_coordinates(hand_landmarks, landmark_index):
    height, width, _ = frame.shape
    landmark = hand_landmarks.landmark[landmark_index]
    cx, cy = int(landmark.x * width), int(landmark.y * height)
    return cx, cy

def draw_finger_tip(frame, coords, color):
    cv2.circle(frame, coords, 5, color, -1)

def calculate_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

last_brightness_update_time = time.time()  # Penanda waktu terakhir perubahan kecerahan
brightness_update_interval = 4  # Interval perubahan kecerahan (dalam detik)

def update_brightness(distance):
    global last_brightness_update_time
    current_time = time.time()
    if current_time - last_brightness_update_time >= brightness_update_interval:
        if 0 <= distance <= 200:
            brightness = min(int(distance / 2), 100)
            sbc.fade_brightness(brightness)
            last_brightness_update_time = current_time  # Update waktu terakhir perubahan kecerahan

def draw_shape(frame, shape_type, center_coords, size, color):
    if shape_type == 'cylinder':
        cv2.circle(frame, center_coords, size, color, -1)
    elif shape_type == 'rectangle':
        x1, y1 = center_coords[0] - size, center_coords[1] - size
        x2, y2 = center_coords[0] + size, center_coords[1] + size
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)

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
            fingertip_coords = get_finger_coordinates(hand_landmarks, mp_hands.HandLandmark.INDEX_FINGER_TIP.value)
            thumbtip_coords = get_finger_coordinates(hand_landmarks, mp_hands.HandLandmark.THUMB_TIP.value)
            draw_finger_tip(frame, fingertip_coords, (0, 0, 255))
            draw_finger_tip(frame, thumbtip_coords, (0, 255, 0))

    # Hitung jarak antara ujung jari telunjuk dan jempol
    if fingertip_coords and thumbtip_coords:
        distance = calculate_distance(fingertip_coords, thumbtip_coords)
        cv2.putText(frame, f'Jarak: {distance:.2f} pixels', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)
        update_brightness(distance)
        
        # Gambar bentuk sebagai indikator kecerahan
        brightness_indicator_size = int(distance / 10)
        draw_shape(frame, 'cylinder', (50, 50), brightness_indicator_size, (255, 255, 255))

    # Tampilkan frame
    cv2.imshow('Fingertip Distance', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
