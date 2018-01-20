import pyautogui
import math
import random

class mouse:
    @staticmethod
    def smooth_move(x, y):
        curPos = pyautogui.position()
        dis = math.sqrt((curPos[0] - x)*(curPos[0] - x) + (curPos[1] - y)*(curPos[1] - y))
        time = dis / random.randint(1500,2000)
        print time
        return pyautogui.moveTo(x, y, time)

    @staticmethod
    def click():
        return pyautogui.click()


class alert:
    @staticmethod
    def alert(msg, title='autopyAlert', default_button='OK'):
        return pyautogui.alert(msg, title, default_button)

mouse.smooth_move(1,2)
mouse.click()