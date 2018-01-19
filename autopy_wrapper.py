import pyautogui

class mouse:
    @staticmethod
    def smooth_move(x, y):
        return pyautogui.moveTo(x, y, 1)

    @staticmethod
    def click():
        return pyautogui.click()


