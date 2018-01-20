# kancolle_bot

t's a **kantai collection** bot
for test only

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
> 一个map, 看不懂
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
> 看不懂你要check什么
### __wait
> 等待一个时间, 不是很懂
### __wait_network
> 空
### __wait_check
> 循环等待, 直到检测出目标
### __goto
> 跳转到指定页面吧
### __sysn_status
> 空
### auto_retrive
> 自动收远征
### goto_yuanzheng
> 先按出击, 等一下, 然后按远征
### send_yuanzheng
> 选页, 选行, 按决定, 选队, 按决定
### refresh_mugang
> 从母港按钮选一个按一下, 再按一下返回母港
### retrive_yuanzheng
> 回收一队远征
### fuse_up
> 补给4队并返回一个可出发的远征队数组
### auto_retrive
> 收远征加补给并回母港的操作
### set_yz
> 设置每队跑的远征的编号
### enable_auto_yz
> 如果收到了远征就发出去, 否则等