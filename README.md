# Gesture-Controlled-Brightness-Adjustment
## Hand Distance Brightness Control

Hand Distance Brightness Control is a Python program that allows users to control computer screen brightness using hand gestures. This program utilizes hand detection with MediaPipe and OpenCV to measure the distance between the index finger and thumb, and adjusts the screen brightness accordingly.

## Key Features
- Detects hands from the input camera feed.
- Measures the distance between the index finger and thumb.
- Controls computer screen brightness based on the detected distance.
- Displays brightness indicator as a cylinder shape on the screen.

## Installation

### Prerequisites
- Python 3.6 or higher.
- OpenCV (`opencv-python`) and MediaPipe (`mediapipe`) can be installed via pip.
- `screen_brightness_control` for adjusting screen brightness. You can install it via pip using the command `pip install screen-brightness-control`.

### Installation Steps
1. Clone this repository or download the `hand_distance_brightness_control.py` file.
2. Ensure all dependencies are installed by running `pip install -r requirements.txt`.
3. Run the program by executing the command `python main.py`.

## Usage
1. Run the program by executing the command `python hand_distance_brightness_control.py`.
2. Point your hand towards the camera.
3. Observe the brightness indicator displayed on the screen.
4. The distance between the index finger and thumb will control the screen brightness:
   - The closer the fingers, the brighter the screen will become.
5. Press the 'q' key on the keyboard to exit the program.

## Contributions
Open contributions for bug fixes, functionality enhancements, and addition of new features. Please open an issue for discussion before making a pull request.

## License
Distribution of this program is licensed under the MIT License. See [LICENSE](LICENSE) for further details.

## Notes
- This program has been tested in a Linux environment and may require additional adjustments to run on other platforms.
- Hand detection performance may vary depending on the camera quality and lighting conditions.

