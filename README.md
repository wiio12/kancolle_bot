# kancolle_bot

It's a **kantai collection** bot
for test only

启动前：  
+ 使用poi的截图工具截图
+ 复制截图，保存到根目录
+ 改变文件名称为`Game.png`

# Understanding wiio's code :V

## 变量

### x
> poi左上角横坐标
### y
> poi左上角纵坐标
### status
> 表示当前页面的字符串
### YZ_set
> 一个map, key是远征队的编号, value是远征的编号
### pic_map
> 一个map, key是图片的字符串, value是图片资源
### pos_map
> 一个map, key是图片的字符串, value是一个tuple, 是图片的左上角坐标和宽和长
### btn_list
> 一个数组, 存按钮图片的字符串
### page_map
> 一个map, 页面和图片的map，就是用来检测页面的map数组包括  
> `['page_buji': ('pos_page_buji', 'pic_page_buji', 'buji')]`  
> 其中 `'pos_page_buji'` 是检测补给页面的位置，`'pic_page_bujji'`是检测补给的页面的图片 `'buji'`是从母港去到补给页面的按钮  
> 感觉很没用很垃圾啊，这个map
### YZ_map
> 一个map, key是远征的编号, value是一个tuple, 是远征的页码和行数

## 函数

### init开头的
> 都不管了

### reset_base
> 通过找右下角的设置图标, 进而设置x和y
### __click_btn
> 传入一个按钮的字符串, 随机在该按钮区域鼠标点击一下
### __click
> 原地鼠标点击一下
### __click_rand_btn
> 在传入的按钮列表里, 随机选一个让鼠标点击一下
### __click_rand_pos
> 在游戏屏幕内, 随机选一个地方让鼠标点击一下
### __move_pos
> 根据传入的按钮的字符串, 将光标移动到该按钮区域
### __check_pic
> 判断某图片是否在某区域内
### __check_page
> 使用页面的map来直接检查页面，不用记住那么多图片对应的是哪个页面的检查了，检查的图片都是在img/page里面存放
### __wait
> 等待一个时间, 等待的基础时间是base，在（base，base+delay）时间内随机选择一个时间进行等待
### __wait_network
> 等待那个网络转转转的东西好。。。 还不会实现。我想可以用poi的通知一下
### __wait_check
> 循环等待, 直到检测出目标
### __goto
> 跳转到指定页面吧
### __sysn_status
> 同步一下状态，在出现状态不同步的时候使用，尝试回到母港
### goto_yuanzheng
> 先按出击, 等一下, 然后按远征
### send_yuanzheng
> 选页, 选行, 按决定, 选队, 按决定
### refresh_mugang
> 从母港按钮选一个按一下, 再按一下返回母港
### retrive_yuanzheng
> 回收一队远征
> 要求当前页面为母港页面
> 首先检查是否有远征回来的图片
> 如果没有，就先刷新一次母港，如果还没有，就输出远征没回来并返回None
> 如果有，收远征，收完后状态为母港页面
### fuse_up
> 补给4队并返回一个可出发的远征队数组
> 要求当前页面为补给页面
> 只有真正补给到的队伍才会被作为返回值返回出去
### auto_retrive
> 收远征加补给并回母港的操作
> 要求当前页面为母港页面
> 返回值为fuse_up返回出来的真正补给过的队伍数组
### set_yz
> 设置每队跑的远征的编号
### enable_auto_yz
> 收远征，发远征，回母港，等