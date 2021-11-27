# 声纳宝藏猎手

import random
import sys
import math


def get_new_board():
    # 创造一个新的 60X15 的数据结构图
    board = []
    for x in range(60):
        # 创造一个有60个列表的主列表
        board.append([])
        for y in range(15):
            # 每个小列表有15个随机的字符
            i_str = random.choice(['-', '~'])
            board[x].append(i_str)
    return board


def draw_board(board):
    # 描画 数据结构图
    tens_digits_line = ' '
    for i in range(1, 6):
        tens_digits_line += (' ' * 9) + str(i)
    print(tens_digits_line)
    print(' '+('0123456789' * 6))
    print()
    for row in range(15):
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''
        board_row = ''
        for column in range(60):
            board_row += board[column][row]
        print('%s%s %s %s' % (extra_space, row, board_row, row))
    print()
    print(' '+('0123456789' * 6))
    print(tens_digits_line)


def get_random_chests(nm):
    # 生成一个宝藏的列表数据结构
    chests = []
    while len(chests) < nm:
        new_chest = [random.randint(0, 59), random.randint(0, 14)]
        if new_chest not in chests:
            chests.append(new_chest)
    return chests


def is_on_board(x, y):
    return x in range(0, 60) and y in range(0, 15)


def make_move(bd, ct, x, y):
    smallest_distance = 100
    for cx, cy in ct:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if distance < smallest_distance:
            smallest_distance = distance
    smallest_distance = round(smallest_distance)

    if smallest_distance == 0:
        ct.remove([x, y])
        return '你找到了闪闪发光的宝藏！'
    else:
        if smallest_distance < 10:
            bd[x][y] = str(smallest_distance)
            return 'Treasure detected at a distance of %s from the sonar device' % smallest_distance
        else:
            bd[x][y] = str(smallest_distance)
            return 'Sonar did not detect anything. All treasure chests out of range.'


def enter_player_move(previous_moves):
    print('Where do you want to drop the next sonar device?(0-59 0-14)(or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thank for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_on_board(int(move[0]),int(move[1])):
            if [int(move[0]), int(move[1])] in previous_moves:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]
        print('Enter a number from 0 to 59,a space,then a number from 0 to 14.')


def show_instruction():
    print('hello!')
    input()


print('S O N A R !')
print()

while True:
    sonarDevices = 20
    theBoard = get_new_board()
    theChests = get_random_chests(3)
    draw_board(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        print('You have %s sonar devices(s) left.%s treasure chests(s) remaining ' % (sonarDevices, len(theChests)))

        x, y = enter_player_move(previousMoves)
        previousMoves.append([x, y])

        moveResult = make_move(theBoard, theChests, x, y)
        if not moveResult:
            continue
        else:
            if moveResult == '你找到了闪闪发光的宝藏！':
                print(previousMoves)
                for x, y in previousMoves:
                    make_move(theBoard, theChests, x, y)
            draw_board(theBoard)
            print(moveResult)
        if len(theChests) == 0:
            print('你找到了所有宝藏，恭喜你！')
            break

        sonarDevices -= 1

        if sonarDevices == 0:
            print('很遗憾，你用光了所有机会！')
            print('宝藏位置如下：')
            for x, y in theChests:
                print('%s %s' % (x, y))

            print('你想再玩一次吗？')
            if not input().lower().startswith('y'):
                sys.exit()
