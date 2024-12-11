import pyautogui

def move_mouse(delta_x, delta_y):
   
    current_x, current_y = pyautogui.position()
    new_x = current_x + delta_x
    new_y = current_y + delta_y
    pyautogui.moveTo(new_x, new_y)

def click_mouse():
    pyautogui.click()