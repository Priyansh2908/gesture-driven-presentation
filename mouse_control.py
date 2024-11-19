from pyautogui import moveTo
from utils import map_value

screen_width, screen_height = 1920, 1080  # Replace with your resolution

def control_mouse(hand_landmarks):
    if not hand_landmarks:
        return

    index_finger = hand_landmarks.landmark[8]  # Index finger tip
    x = int(map_value(index_finger.x, 0, 1, 0, screen_width))
    y = int(map_value(index_finger.y, 0, 1, 0, screen_height))
    moveTo(x, y)
