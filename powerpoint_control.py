import pyautogui

def control_powerpoint(gesture):
    if gesture == 'next_slide':
        pyautogui.press('right')
    elif gesture == 'previous_slide':
        pyautogui.press('left')
    elif gesture == 'start_slideshow':
        pyautogui.press('f5')
    elif gesture == 'stop_slideshow':
        pyautogui.press('esc')
