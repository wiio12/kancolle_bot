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
        times = dis / random.randint(1500, 2000)
        return pyautogui.moveTo(x, y, times)

    @staticmethod
    def click():
        times = random.randint(2, 4)
        interval = random.randint(80, 150) / 1000
        pyautogui.click(None, None, 2, interval)
        time.sleep(interval)
        times = times - 2
        interval = random.randint(80, 150) / 1000
        pyautogui.click(None, None, times, interval)


class alert:
    @staticmethod
    def alert(msg, title='autopyAlert', default_button='OK'):
        return pyautogui.alert(msg, title, default_button)

class screen:
    @staticmethod
    def get_size():
        return pyautogui.size()

'''
print pyautogui.size()
mouse.smooth_move(10,42)
time.sleep(3)
mouse.smooth_move(810,522)
'''




