import random
from time import sleep

# 显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
# 前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
# 背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）
#
# 常见开头格式：
# \033[0m            默认字体正常显示，不高亮
# \033[32;0m       红色字体正常显示
# \033[1;32;40m  显示方式: 高亮    字体前景色：绿色  背景色：黑色
# \033[0;31;46m  显示方式: 正常    字体前景色：红色  背景色：青色
# for i in range(30, 38):
#     for j in range(40, 48):
#         for k in (0,1,22,4,24,5,25,7,27):
#             print('front: ' + str(i) + ' back: ' + str(j) + '  \033[' + str(k) + ';' + str(i) + ';' + str(
#                 j) + 'm' + "Hello world \033[0m")


def choose_cave():
    i = input('\033[1;34m你醒来了！'
              '现在你在一个满是巨龙的大陆。\n'
              '在你的前面，有两个洞穴。\n'
              '在一个洞穴，有一些友好的巨龙会赠与你宝藏。\n'
              '在另一个洞穴，有另一群饥饿的巨龙会吃掉你。\n'
              '现在你选择哪一边\n'
              '左？ or 右？（1 or 2 选择）\n\033[0m'
              )
    return int(i)


def check_cave(choose):
    print('你走进了洞穴。。。')
    sleep(2)
    print('你感到了恐惧。。。')
    sleep(2)
    print('一条巨龙跳到了你的面前，并张开了大嘴。。。')
    sleep(2)
    print()
    friendly_cave = random.randint(1,2)
    if friendly_cave == choose:
        print('\033[0;31m巨龙给与了你,他的财宝！\033[0m')
    else:
        print('\033[0;32m巨龙吞噬了你！\033[0m')


play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    res = choose_cave()
    check_cave(res)
    print('\033[1;32;40m你想再玩一次？（yes or no）\033[0m')
    sleep(2)
    play_again = input()
