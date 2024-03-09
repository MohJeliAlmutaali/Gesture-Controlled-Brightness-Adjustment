import pyautogui
import time

# Tunggu 2 detik sebelum menekan tombol Fn+F2
time.sleep(2)

# Tekan tombol Fn+F2
pyautogui.keyDown('fn')
pyautogui.press('f2')

# Tunggu selama 3 detik
time.sleep(3)

# Lepaskan tombol Fn+F2
pyautogui.keyUp('fn')
