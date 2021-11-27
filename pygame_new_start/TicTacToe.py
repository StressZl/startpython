"""
                        井字棋游戏

                    O  |   X  |
                 ------+------+------
                       |   O  |
                 ------+------+------
                       |   X  |  O

        游戏开始
   询问玩家使用X或者O      决定谁先走

  轮到玩家落子          轮到计算机落子

    显示游戏版

   让玩家落子         让计算机落子

   判断玩家是否获胜    判断计算机是否获胜

    判断是否平局       判断是否平局

        询问玩家是否再来一次

             游戏结束

"""
import random
import copy


def display_chess_board(bd):
    # 该函数用于显示棋盘，bd=['','','','','','','','','']
    # 绘制空的棋盘
    cb = """
     %s  |  %s |  %s   
    ----+----+----
     %s  |  %s |  %s  
    ----+----+----
     %s  |  %s |  %s  
    """ % (bd[0], bd[1], bd[2], bd[3], bd[4], bd[5], bd[6], bd[7], bd[8])
    print(cb)


def get_chess_type():
    while True:
        print('使用X或者O(X or O)?')
        tp = input().upper()
        if tp == 'X' or tp == 'O':
            print('你选择了使用%s' % tp)
            return tp
        else:
            print('请重新选择！')


def get_act():
    while True:
        print('是否先手(y or n)?')
        ac = input().upper()
        if ac == 'Y' or ac == 'N':
            info = '先' if ac == 'Y' else '后'
            print('你选择了%s手！' % info)
            return ac
        else:
            print('请重新选择！')


def get_player_num(bd, typ):
    while True:
        # 获取玩家落子，返回board
        get_num = input('请落子（1-9）\n')
        if get_num in [str(i) for i in range(1, 10)] and bd[int(get_num) - 1] == ' ':
            bd[int(get_num) - 1] = typ
            return bd
        else:
            print('请重新选择！')


def get_ai_num(bd, typ):
    # AI根据玩家落子，返回board
    # 第一优先级，选择自己获胜的位置落子
    for k in range(0, 9):
        if bd[k] == ' ':
            bd_new = copy.deepcopy(bd)
            bd_new[k] = typ
            if check_result(bd_new, typ):
                bd[k] = typ
                return bd
    # 第二优先级，选择玩家即将获胜的位置落子
    f_typ = 'X' if typ == 'O' else 'O'
    for k in range(0, 9):
        if bd[k] == ' ':
            bd_new = copy.deepcopy(bd)
            bd_new[k] = f_typ
            if check_result(bd_new, f_typ):
                bd[k] = typ
                return bd
    # 第三优先级，选择中间位置下子
    if bd[4] == ' ':
        bd[4] = typ
        return bd
    # 第四优先级，选择角下子
    for k in [0, 2, 6, 8]:
        if bd[k] == ' ':
            bd[k] = typ
            return bd
    # 最后，选择边
    for k in [1, 3, 5, 7]:
        if bd[k] == ' ':
            bd[k] = typ
            return bd
    return bd


def play_again():
    # 该函数 返回真 如果 玩家想要再玩一次。否则 返回假。
    print('你想再玩一次吗？(yes or no)')
    return input().lower().startswith('y')


def check_result(b, t):
    # 该函数通过board判断是否胜利，是，返回真，否则返回假。
    if b[0] == b[1] == b[2] == t:
        return True
    elif b[0] == b[3] == b[6] == t:
        return True
    elif b[0] == b[4] == b[8] == t:
        return True
    elif b[1] == b[4] == b[7] == t:
        return True
    elif b[2] == b[5] == b[8] == t:
        return True
    elif b[2] == b[4] == b[6] == t:
        return True
    elif b[3] == b[4] == b[5] == t:
        return True
    elif b[6] == b[7] == b[8] == t:
        return True
    else:
        return False


board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
GameIsDone = False
while True:
    print('欢迎来到井字棋游戏！')
    display_chess_board(board)
    chess_type = get_chess_type()
    AI_type = 'X' if chess_type == 'O' else 'O'
    act = get_act()
    if act == 'N':
        # 机器先下子，这里选择随机落子
        board_index = random.randint(0, 9)
        board[board_index] = AI_type
        display_chess_board(board)
    while True:
        # 玩家落子
        board = get_player_num(board, chess_type)
        display_chess_board(board)
        if check_result(board, chess_type):
            print('你赢了！')
            GameIsDone = True
            break
        # AI落子
        print('AI思考中？')
        board = get_ai_num(board, AI_type)
        display_chess_board(board)
        if check_result(board, AI_type):
            print('你输了！')
            GameIsDone = True
            break
        for i in board:
            if i == ' ':
                break
        else:
            print('平局!')
            GameIsDone = True
            break
    if GameIsDone:
        if play_again():
            board = [' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' ']
        else:
            break
