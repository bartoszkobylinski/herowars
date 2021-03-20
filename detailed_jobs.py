import pyautogui


def locate_button_coords(picture):
    middle_X = picture.left + 15
    middle_Y = picture.top + 15
    try:
        pyautogui.click(x=middle_X, y=middle_Y)
    except AttributeError:
        pass
