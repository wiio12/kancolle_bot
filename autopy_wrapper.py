# -*- coding: utf-8 -*-

import pyautogui
import math
import random
import time

class mouse:
    @staticmethod
    def smooth_move(x, y):
        cur_pos = pyautogui.position()
        dis = math.sqrt((cur_pos[0] - x)*(cur_pos[0] - x) + (cur_pos[1] - y)*(cur_pos[1] - y))
        time = dis / random.randint(1500, 2000)
        print time
        return pyautogui.moveTo(x, y, time)

    @staticmethod
    def click():
        times = random.randint(2, 4)
        while times > 0:
            interval = random.randint(80, 150) / 1000
            pyautogui.click(None, None, 1)
            time.sleep(interval)
            times = times - 1


class alert:
    @staticmethod
    def alert(msg, title='autopyAlert', default_button='OK'):
        return pyautogui.alert(msg, title, default_button)
