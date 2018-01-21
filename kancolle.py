# -*- coding: utf-8 -*-
import random
import time
import cv2
import kancolle_img

from PIL import Image, ImageGrab

try:
    import autopy
except ImportError:
    import autopy_wrapper as autopy


def get_time():
    """获取当前时间字符串，终端写报告用的"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def print_msg(msg):
    """在终端写报告，传一个字符串就可以了"""
    print get_time(), ':', msg


def print_debug(msg):
    print msg


class KancolleStatus:
    def __init__(self, x=0, y=0):
        """构造函数，初始化一些资源"""
        self.x = x
        self.y = y
        self.__init_btn()
        self.__init_pic()
        self.__init_page()
        self.__init_yuanzheng()
        self.status = 'mugang'
        self.YZ_set = {1: 0, 2: 0, 3: 0, 4: 0}
        self.reset_base()

    def __init_pic(self):
        """图片构造函数，图片资源都在这里读取初始化"""
        pic_shezhi = Image.open('img/shezhi.png')
        pic_yuanzheng = Image.open('img/yuanzheng.png')
        pic_ci = Image.open('img/ci.png')
        pic_quanbuji = Image.open('img/quanbuji.png')
        pic_page_buji = Image.open('img/page/page_buji.png')
        pic_page_xuan = Image.open('img/page/page_xuan.png')
        pic_page_yuanzheng = Image.open('img/page/page_yuanzheng.png')

        pic_base = cv2.imread('img/shezhi.png')

        self.pic_map = {
            'pic_shezhi': pic_shezhi,
            'pic_yanzheng': pic_yuanzheng,
            'pic_ci': pic_ci,
            'pic_quanbuji': pic_quanbuji,
            'pic_page_buji': pic_page_buji,
            'pic_page_xuan': pic_page_xuan,
            'pic_page_yuanzheng': pic_page_yuanzheng,

            'pic_base': pic_base
        }

    def __init_btn(self):
        """按钮构造函数，按钮资源都在这里初始化"""
        self.pos_map = {
            'main_return': (15, 15, 60, 60),
            'zhanji': (132, 42, 60, 14),
            'youjun': (210, 42, 60, 14),
            'tujian': (290, 42, 60, 14),
            'shangdian': (375, 42, 60, 14),
            'fangjian': (450, 42, 60, 14),
            'renwu': (530, 42, 60, 14),

            # 母港那6个主要大按钮
            'chuji': (160, 220, 70, 70),  # 出击按钮
            'buji': (50, 200, 50, 50),  # 补给按钮
            'biancheng': (174, 110, 50, 50),  # 编成按钮
            'gaizhuang': (288, 200, 50, 50),  # 改装按钮
            'ruqu': (97, 335, 50, 50),  # 入渠按钮
            'gongchang': (244, 335, 50, 50),  # 工厂按钮

            'jianniang': (490, 310, 100, 100),  # 舰娘
            'shezhi': (760, 430, 30, 30),  # 设置按钮

            # 补给页面
            'buji_quanbuji': (110, 110, 20, 20),
            'buji_1': (145, 110, 9, 9),
            'buji_2': (170, 110, 9, 9),
            'buji_3': (203, 110, 9, 9),
            'buji_4': (231, 110, 9, 9),

            # 出击3选择页面
            'xuan_chuji': (160, 160, 120, 120),
            'xuan_yanxi': (390, 160, 120, 120),
            'xuan_yuanzheng': (610, 160, 120, 120),

            # 远征页面
            'yz_01': (120, 160, 400, 10),
            'yz_02': (120, 192, 400, 10),
            'yz_03': (120, 222, 400, 10),
            'yz_04': (120, 252, 400, 10),
            'yz_05': (120, 282, 400, 10),
            'yz_06': (120, 312, 400, 10),
            'yz_07': (120, 342, 400, 10),
            'yz_08': (120, 372, 400, 10),
            'yz_d1': (114, 440, 20, 7),
            'yz_d2': (193, 440, 20, 7),
            'yz_d3': (244, 440, 20, 7),
            'yz_d4': (295, 440, 20, 7),
            'yz_d5': (355, 440, 20, 7),
            'yz_jueding': (606, 430, 150, 23),
            'yz_s2': (387, 107, 9, 9),
            'yz_s3': (417, 107, 9, 9),
            'yz_s4': (447, 107, 9, 9),
            'yz_kaishi': (535, 433, 150, 18),

            'pos_page_yuanzheng': (470, 95, 50, 50),
            'pos_page_buji': (615, 101, 50, 50),
            'pos_page_xuan': (159, 378, 50, 50),
            'pos_yuanzhenghuilai': (503, 5, 290, 50),
            'pos_ci': (745, 420, 40, 40),
            'pos_quanbuji': (90, 95, 30, 30)
        }
        self.btn_list = ['main_return',
                         'zhanji',
                         'youjun',
                         'tujian',
                         'shangdian',
                         'fangjian',
                         'renwu',

                         'chuji',
                         'shezhi'
                         ]

    def __init_page(self):
        """初始化检测页面用的dict"""
        self.page_map = {
            'page_mugang': ('shezhi', 'pic_shezhi', 'main_return'),
            'page_buji': ('pos_page_buji', 'pic_page_buji', 'buji'),
            'page_xuan': ('pos_page_xuan', 'pic_page_xuan', 'chuji')

        }

    def __init_yuanzheng(self):
        self.YZ_map = {
            1: ('1', '01'), 2: ('1', '02'), 3: ('1', '03'), 4: ('1', '04'), 5: ('1', '05'), 6: ('1', '06'),
            7: ('1', '07'), 8: ('1', '08'),
            9: ('2', '01'), 10: ('2', '02'), 11: ('2', '03'), 12: ('2', '04'), 13: ('2', '05'), 14: ('2', '06'),
            15: ('2', '07'), 16: ('2', '08'),
            17: ('3', '01'), 18: ('3', '02'), 19: ('3', '03'), 20: ('3', '04'), 21: ('3', '05'), 22: ('3', '06'),
            23: ('3', '07'), 24: ('3', '08'),
            25: ('4', '01'), 26: ('4', '02'), 27: ('4', '03'), 28: ('4', '04'), 29: ('4', '05'), 30: ('4', '06'),
            31: ('4', '07'), 32: ('4', '08'),
            33: ('5', '01'), 34: ('5', '02'), 35: ('5', '03'), 36: ('5', '04'), 37: ('5', '05'), 38: ('5', '06'),
            39: ('5', '07'), 40: ('5', '08')
        }

    def reset_base(self):
        ImageGrab.grab().save('screen.png')
        screen = cv2.imread('screen.png')

        ret = kancolle_img.find_bitmap_cv(screen, self.pic_map['pic_base'])
        # TODO: what if no match
        # if ret is None:
        #    autopy.alert.alert('请处于母港界面重置Kancolle')
        self.x = ret[0] - 764
        self.y = ret[1] - 441
        # autopy.mouse.smooth_move(self.x, self.y)
        # print ret

    def __click_btn(self, btn):
        """按下一个按钮，btn传入一个字符串，是上面dict的名字
        :type btn: String 按按钮的名字
        """
        btn_pos = self.pos_map[btn]
        bx = self.x + btn_pos[0]
        by = self.y + btn_pos[1]
        xx = random.randint(bx, bx + btn_pos[2])
        yy = random.randint(by, by + btn_pos[3])
        autopy.mouse.smooth_move(xx, yy)
        # print xx,yy
        autopy.mouse.click()

    def __click(self):
        """原地按下一个按钮"""
        self.__wait(0.5, 0.5)
        autopy.mouse.click()

    def __click_rand_btn(self, btns):
        """传入一个btns的列表，随机选一个按下"""
        choice = random.randint(0, len(btns) - 1)
        self.__click_btn(btns[choice])

    def __click_rand_pos(self):
        """在游戏屏幕范围内随机选一个地方按下"""
        xx = random.randint(self.x, self.x + 480)
        yy = random.randint(self.y, self.y + 380)
        autopy.mouse.smooth_move(xx, yy)
        autopy.mouse.click()

    def __move_pos(self, pos):
        """移动到pos所指示的地方"""
        btn_pos = self.pos_map[pos]
        bx = self.x + btn_pos[0]
        by = self.y + btn_pos[1]
        xx = random.randint(bx, bx + btn_pos[2])
        yy = random.randint(by, by + btn_pos[3])
        autopy.mouse.smooth_move(xx, yy)

    """
    def __check_mugang(self):
        '''通过图片匹配检查是否在母港，旧方法，不推荐使用，推荐用__check_pic()'''
        btn_shezhi = self.pos_map['shezhi']
        bx = self.x + btn_shezhi[0]
        by = self.y + btn_shezhi[1]
        return find_bitmap(self.__pic_shezhi, (bx, by))
    
    def __check_yuanzheng(self):
        '''检查是否有远征回来,旧方法，不推荐使用'''
        pic_yz = self.pos_map['pos_yuanzhenghuilai']
        bx = self.x + pic_yz[0]
        by = self.y + pic_yz[1]
        return find_bitmap(self.__pic_yuanzheng, (bx, by))
    
    def return_mugang(self):
        '''返回母港'''
        if self.__check_mugang() is not None:
            self.status = 'mugang'
            return
        self.__click_btn('main_return')
        self.status = 'mugang'
        return
    
    """

    def __check_pic(self, pos, pic):
        """检查相似图片是否在相应区域，pos是区域，pic是检查的图片
        :type pos: String 位置字符串
        :type pic: String 图片字符串
        :return : tuple
        """
        pos = self.pos_map[pos]
        bx = self.x + pos[0]
        by = self.y + pos[1]
        bitmap = self.pic_map[pic]
        print '检查图片' + pic
        return kancolle_img.find_bitmap(bitmap, (bx, by))

    def __check_page(self, page):
        temp = self.page_map[page]
        return self.__check_pic(temp[0], temp[1])

    @staticmethod
    def __wait(base=0.5, delay=0.5):
        """等待一定时间，base是基础值，lagecy是随机"""
        t = random.randint(base * 1000, (base + delay) * 1000)
        t = t / 1000.0
        time.sleep(t)

    def __wait_network(self):
        """等待网络延时，还不知道怎么写"""
        pass

    def __wait_check(self, pos, pic):
        """循环等待，直到检测到对应的图案
        :type pos: String
        :type pic: String
        """
        pos = self.pos_map[pos]
        bx = self.x + pos[0]
        by = self.y + pos[1]
        bitmap = self.pic_map[pic]
        print '检查图片', pic
        c = 0
        while True:
            ret = kancolle_img.find_bitmap(bitmap, (bx, by))
            if ret is None:
                self.__wait(1, 0.5)
                c += 1
            else:
                self.__wait()
                return
            if c >= 15:
                # 错误处理！！
                break

    def __goto(self, page):
        """转到某个页面
        :type page: String 页面名称
        """
        temp = self.page_map[page]
        self.__wait()
        ret = self.__check_pic(temp[0], temp[1])
        if ret is None:
            self.__click_btn(temp[2])
            self.__wait_check(temp[0], temp[1])
        self.status = page
        self.__wait()

    def __sysn_status(self):
        pass

    def goto_yuanzheng(self):
        self.__sysn_status()
        self.__goto('page_xuan')
        self.__click_btn('xuan_yuanzheng')
        self.__wait_check('pos_page_yuanzheng', 'pic_page_yuanzheng')

    def send_yuanzheng(self, team, yz_num):
        yzp = self.YZ_map[yz_num]
        dao = 'yz_d' + yzp[0]  # 岛号
        pos = 'yz_' + yzp[1]  # 远征位置号
        te = 'yz_s' + str(team)  # 队伍号
        self.__click_btn(dao)
        self.__wait()
        self.__click_btn(pos)
        self.__wait()
        self.__click_btn('yz_jueding')
        self.__wait()
        self.__click_btn(te)
        self.__wait()
        self.__click_btn('yz_kaishi')
        print_msg(str(team) + '队开始' + str(yz_num) + '号远征')
        self.__wait(5, 1)

    def refresh_mugang(self):
        """刷新母港"""
        btn = ['zhanji', 'chuji', 'buji', 'gaizhuang', 'ruqu', 'gongchang', 'biancheng']
        self.__click_rand_btn(btn)
        self.__wait(1, 2)
        self.__click_btn('main_return')
        self.__wait(1, 2)

    def retrive_yuanzheng(self):
        """回收远征"""
        if self.status == 'notAllow':
            print_msg('尝试查远征，状态未许可')
            return

        ret = self.__check_pic('pos_yuanzhenghuilai', 'pic_yanzheng')
        if ret is None:
            self.refresh_mugang()
            self.__wait(0, 1)
            ret = self.__check_pic('pos_yuanzhenghuilai', 'pic_yanzheng')
            if ret is None:
                print_msg('检查远征后未有远征队回来')
                return None
        '''接下来收远征'''
        self.__click_rand_pos()
        self.__wait_check('pos_ci', 'pic_ci')
        self.__click_rand_pos()
        self.__click()
        print_msg('收回一队远征')
        self.__wait_check('shezhi', 'pic_shezhi')
        self.status = 'mugang'
        return 1

    def fuse_up(self):
        """补给4队"""
        if self.status != 'buji':
            print_msg('程序状态不同步')
            return
        btns = ['buji_1', 'buji_2', 'buji_3', 'buji_4']
        random.shuffle(btns)
        lst = []
        for i in range(0, 4):
            self.__click_btn(btns[i])
            self.__wait(0.5, 0.3)
            self.__move_pos('buji_quanbuji')
            self.__wait(0.5, 0.3)
            ret = self.__check_pic('pos_quanbuji', 'pic_quanbuji')
            if ret is not None:
                self.__click()
                self.__wait(2, 1)
                print_msg('成功补给' + btns[i][-1] + '队')
                lst.append(int(btns[i][-1]))
            self.__wait(0.5, 0.5)
        return lst

    def auto_retrive(self):
        """自动收远征"""
        flag = False
        ret = None
        while True:
            ret = self.retrive_yuanzheng()
            if ret is None:
                break
            else:
                flag = True
        if flag is True:
            self.__click_btn('buji')
            self.status = 'buji'
            self.__wait_check('pos_page_buji', 'pic_page_buji')
            ret = self.fuse_up()
            # TODO: wait
            self.__wait(0.5, 0.5)
            self.__click_btn('main_return')
            self.status = 'mugang'
        return ret

    def set_yz(self, team, yz_num):
        self.YZ_set[team] = yz_num

    def enable_auto_yz(self):
        self.__sysn_status()
        while True:
            yzlst = self.auto_retrive()
            if yzlst is not None:
                self.goto_yuanzheng()
                self.__wait()
                for i in yzlst:
                    if self.YZ_set[i] != 0:
                        self.send_yuanzheng(i, self.YZ_set[i])
                        self.__wait()
            self.__goto('page_mugang')
            self.__wait(300, 100)


ks = KancolleStatus()
# ks.return_mugang()
# ks.retrive_yuanzheng()
# ks.retrive_yuanzheng()
# ks.status = 'buji'
# ks.fuse_up()
# ks.auto_retrive()
# ks.goto_yuanzheng()
# ks.send_yuanzheng(3,11)

ks.set_yz(2, 2)
ks.set_yz(3, 5)
ks.set_yz(4, 6)
ks.enable_auto_yz()

# ks.reset_base()
