# -*- coding: utf-8 -*-
import cv2
import itertools
import operator

import matplotlib.pyplot as plt

from PIL import Image, ImageGrab

GAME_SIZE = Image.open('Game.png').size
X_RATE = GAME_SIZE[0] / 800.0
Y_RATE = GAME_SIZE[1] / 480.0


def find_bitmap_cv(img, template):
    """
    从img中找到template，并返回template左上角的坐标
    返回值top_left是个tuple，top_left[0]是x，top_left[1]是y，原图左上角为(0,0)
    :param img:
    :param template:
    :return: top_left
    """
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_RGBA2GRAY)
    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    return top_left


def __get_hash(img):
    """获取图片的hash，内部方法不需要知道干嘛用"""
    x, y = img.size
    a = int(20 * y / x)
    im = img.resize((20, a), Image.ANTIALIAS).convert('L')
    pixels = list(im.getdata())
    avg = sum(pixels) / len(pixels)
    return ''.join(map(lambda p: '1' if p > avg else '0', pixels))


def __hamming_dest(hash1, hash2):
    """同内部方法，不需要直达怎么用"""
    return sum(itertools.imap(operator.ne, hash1, hash2))


def find_bitmap(img, base, rect=50):
    """在一定区域内找图，img是图片，base是左上角坐标，rect是找图区域"""
    current = ImageGrab.grab()
    im_hash = __get_hash(img)
    dist = 1000000
    mi, mj = 0, 0
    for i in range(base[0], base[0] + rect):
        for j in range(base[1], base[1] + rect):
            tm = current.crop((i, j, i + img.size[0] * X_RATE, j + img.size[1] * Y_RATE))
            tm_hash = __get_hash(tm)
            d = __hamming_dest(tm_hash, im_hash)
            # print i,j
            if d < dist:
                dist = d
                mi, mj = i, j
                ss = tm
            if d <= 5:
                print '检测图像dist：', dist
                #plt.imshow(ss)
                #plt.show()
                return mi, mj
    print '检测图像dist：', dist
    plt.imshow(ss)
    plt.show()
    if dist >= 50:
        return None
    return mi, mj

def get_game_size():
    return GAME_SIZE

def get_screenshot_size():
    return ImageGrab.grab().size

'''
cur = ImageGrab.grab()
i , j  = 762,468
#tm = cur.crop((i, j, i + 21 , j + 20 ))
tm = cur.crop((0,0,100,100))
print SCREENSIZE
print (X_RATE, Y_RATE)
tm.save('www4.png')
'''





#plt.imshow(cur)
#plt.show()
