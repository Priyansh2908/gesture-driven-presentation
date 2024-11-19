from pyautogui import mouseDown, mouseUp, moveTo

def handle_drawing(gesture, x, y):
    if gesture == 'draw':
        mouseDown()
        moveTo(x, y)
    else:
        mouseUp()
