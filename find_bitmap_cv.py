#coding=utf-8
import cv2


def find_bitmap_cv(img, template):
    """
    从img中找到template，并返回template左上角的坐标
    返回值top_left是个tuple，top_left[0]是x，top_left[1]是y，原图左上角为(0,0)
    :param img:
    :param template:
    :return: top_left
    """
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    return top_left
