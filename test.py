import autopy
import math
from PIL import Image, ImageGrab
import itertools, operator, time, sys, threading

def hello_world():
    autopy.alert.alert("sdfsd")

'''futility... the algorithm is way too slow... 
def color_distance(e1, e2):
    rmean = (e1[0] + e2[0]) / 2
    r = e1[0] - e2[0]
    g = e1[1] - e2[1]
    b = e1[2] - e2[2]
    return math.sqrt((((512+rmean)*r*r)>>8) + 4*g*g + (((767-rmean)*b*b)>>8))

def color_variance(lst):
    sum = 0
    lst_len = len(lst)
    if lst_len == 0:
        return None
    for i in range(0,lst_len):
        sum += lst[i]

    avg = sum / lst_len
    v = 0
    for i in range(0, lst_len):
        v += (lst[i] - avg) * (lst[i] - avg)
    return v / lst_len

def find_bitmap_own(big, small):
    print big.width , '*' , big.height
    print small.width , '*' , small.height
    bigx = big.width - small.width
    bigy = big.height - small.height
    mins = 10000000
    mini = 1
    minj = 1
    for j in range(1,bigx):
        for i in range(1,bigy):
            cd = []
            for ii in range(1,small.width):
                for jj in range(1,small.height):
                    try:
                        bc = autopy.color.hex_to_rgb(big.get_color(i+ii-1,j+jj-1))
                        sc = autopy.color.hex_to_rgb(small.get_color(ii,jj))
                        cdp = color_distance(bc,sc)
                        cd.append(cdp)
                    except ValueError:
                        print 'point ', i,j

            cv = color_variance(cd)
            print '(',i,',',j,'):',cv
            if cv < mins:
                mins = cv
                mini = i
                minj = j
            if cv == 0:
                return (mini,minj)
    return (mini,minj)
    
'''

def get_hash(img):
    im = img.resize((16,12), Image.ANTIALIAS).convert('L')
    pixels = list(im.getdata())
    avg = sum(pixels) / len(pixels)
    return ''.join(map(lambda p : '1' if p > avg else '0', pixels))

def hamming_dest(hash1,hash2):
    return sum(itertools.imap(operator.ne, hash1, hash2))


def orderdd():
    kanbasetop = Image.open('img/basetop.png')
    current = Image.open('screen.png')

def find_bitmap(img,base = (1,1),rect = 50):
    current = ImageGrab.grab()
    imhash = get_hash(img)
    dist = 1000000
    mi,mj = 0,0
    for i in range(base[0],base[0] + rect):
        for j in range(base[1],base[1] + rect):
            tm = current.crop((i,j,i+img.size[0],j+img.size[1]))
            tmhash = get_hash(tm)
            d = hamming_dest(tmhash,imhash)
            #print i,j
            if d < dist:
                dist = d
                mi , mj = i ,j
            if d <= 5:
                return (mi,mj)
    if dist >=50:
        return None
    return (mi,mj)

def order(img, i , step=1):
       l, t = img.left + i * step, img.top
       r, b = l + img.width, t + img.height
       hash2 = self.get_hash(ImageGrab.grab((l, t, r, b)))
       (mi, dist) = None, 50
       for i, hash1 in enumerate(self.maps):
           if hash1 is None:
               continue
           this_dist = self.hamming_dist(hash1, hash2)
           if this_dist < dist:
               mi = i
               dist = this_dist
       return mi

def check_main_screen():
    """Look for the main screen for kancolle"""
    kanbasetop = autopy.bitmap.Bitmap.open('img/basetop.png')
    kanbasebottom = autopy.bitmap.Bitmap.open('img/d3.png')
    currentScreen = autopy.bitmap.capture_screen()

    #pos = currentScreen.find_bitmap(kanbasetop,0.3)
    pos = find_bitmap_own(kanbasebottom,kanbasetop)
    if pos is None:
        #do something
        print 'nothing'
        return None
    else:
        x = pos[0]
        y = pos[1]
        autopy.mouse.smooth_move(x,y)
       

def print_debug_info(cls):
    def _print_debug_info(func):
        def _debug_info(*args, **kwargs):
            print 'call %s()...'%(func.__name__)
            ret = cls.func(*args, **kwargs)
            return ret
        return _debug_info
    return _print_debug_info
'''
def print_debug_info(func):
    def _debug_info(*args, **kwargs):
        print 'call %s()...'%(func.__name__)
        ret = func.__cls__.func(*args, **kwargs)
        return ret
    return _debug_info
'''
class ssss:
    @print_debug_info(ssss)
    def ss():
        print '344'
        return 34
    
'''
@print_debug_info
def ss():
    print 'ssss'
    return 3
'''
pp = ssss()
ret = pp.ss()
print ret
#hello_world()
#autopy.mouse.smooth_move(1,1)

#autopy.bitmap.capture_screen().save('screen.png')
#check_main_screen()
'''
im = Image.open('img/basebottom.png')
rs = find_bitmap(im,(1168,490))
print rs
autopy.mouse.smooth_move(rs[0],rs[1])
'''

