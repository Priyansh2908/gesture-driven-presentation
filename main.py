import cv2
import keyboard
from hand_tracking import track_hands
from mouse_control import control_mouse
from powerpoint_control import control_powerpoint
from drawing_tool import handle_drawing

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam not accessible!")
        return

    show_camera_feed = True
    while True:
        if keyboard.is_pressed('ctrl+q'):
            print("Exiting...")
            break

        ret, frame = cap.read()
        if not ret:
            break

        gestures, frame = track_hands(frame)

        for hand_landmarks in gestures:
            # Example: Add custom gesture recognition here
            control_mouse(hand_landmarks)
            # Add other functionalities like PowerPoint control or drawing here

        if show_camera_feed:
            cv2.imshow("Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
