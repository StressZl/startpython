"""
游戏规则
1.游戏初始有双黑双白
     1   2   3   4   5   6   7   8
    +---+---+---+---+---+---+---+---+
 1  |   |   |   |   |   |   |   |   | 1
    +---+---+---+---+---+---+---+---+
 2  |   |   |   |   |   |   |   |   | 2
    +---+---+---+---+---+---+---+---+
 3  |   |   |   |   |   |   |   |   | 3
    +---+---+---+---+---+---+---+---+
 4  |   |   |   | O | X |   |   |   | 4
    +---+---+---+---+---+---+---+---+
 5  |   |   |   | X | O |   |   |   | 5
    +---+---+---+---+---+---+---+---+
 6  |   |   |   |   |   |   |   |   | 6
    +---+---+---+---+---+---+---+---+
 7  |   |   |   |   |   |   |   |   | 7
    +---+---+---+---+---+---+---+---+
 8  |   |   |   |   |   |   |   |   | 8
    +---+---+---+---+---+---+---+---+
     1   2   3   4   5   6   7   8
2.双方轮流下子，必须有反转的情况才能下棋
3.结束条件:棋盘满了，哪方多就能成功;无子可下，对方赢
"""
import sys
import random


def display_introduce():
    # 展示游戏规则
    print('欢迎来到反转棋游戏！')
    print('1.游戏初始有双黑双白。')
    print('2.双方轮流下子，必须有反转的情况才能下棋')
    print('3.结束条件:棋盘满了，哪方多就能成功;无子可下，对方赢')


def init_game():
    # 初始化游戏
    print('游戏初始化中')
    i_board = create_board(WIDTH, HEIGHT)
    i_date = create_date(WIDTH, HEIGHT)
    # 在中央生成初始棋子
    init_piece = [(WIDTH // 2, HEIGHT // 2, 'O'), (WIDTH // 2 + 1, HEIGHT // 2 + 1, 'O'),
                  (WIDTH // 2 + 1, HEIGHT // 2, 'X'), (WIDTH // 2, HEIGHT // 2 + 1, 'X')]
    for piece in init_piece:
        i_board = add_piece(piece[0], piece[1], piece[2], i_board)
        i_date = add_date(piece[0], piece[1], piece[2], i_date)
    # 展示初始棋盘
    print(i_board)
    return i_board, i_date


def create_board(h_size_number=8, v_size_number=8):
    # 生成棋盘 8*8
    horizontal_line = '---'
    horizontal_space = '   '
    vertical_line = '|'
    clearance = '+'
    clearance_list = [clearance]*(h_size_number+1)
    vertical_line_list = [vertical_line]*(h_size_number+1)
    checkerboard = '    '+' '.join([str(i).center(3, " ") for i in range(1, h_size_number+1)]) + '\n'
    for i in range(v_size_number):
        checkerboard += '    ' + horizontal_line.join(clearance_list) + '\n' +\
                        str(i+1).center(4, ' ') + horizontal_space.join(vertical_line_list) + str(i+1).center(4, ' ') +'\n'
    checkerboard += '    ' + horizontal_line.join(clearance_list) + '\n'
    checkerboard += '    '+' '.join([str(i).center(3, " ") for i in range(1, h_size_number+1)])
    return checkerboard


def add_piece(x, y, piece_type, bd):
    # 棋盘上添加棋子 x为横轴坐标，y为纵轴坐标
    black_piece = ' \033[0;31mO\033[0m '
    white_piece = ' \033[0;32mX\033[0m '
    pieces = black_piece if piece_type == 'O' else white_piece
    b_line = bd.split('\n')
    for ln in range(len(b_line)):
        if '|' in b_line[ln] and ln / 2 == y:
            x_line = b_line[ln].split('|')
            x_line[x] = pieces
            b_line[ln] = '|'.join(x_line)
    bd = '\n'.join(b_line)
    return bd


def create_date(h_number, v_number):
    # 根据棋盘大小创造数据结构
    void_date = ''
    data_list = []
    for ix in range(v_number):
        h_list = [void_date]*h_number
        data_list.append(h_list)
    return data_list


def add_date(x, y, piece_type, dt):
    # 添加数据到data_list，x为横轴坐标，y为纵轴坐标，piece_type 0为O,1为X
    dt[y-1][x-1] = piece_type
    return dt


def is_on_board(x, y):
    # 判断是否在棋盘上
    return 0 <= x <= (WIDTH - 1) and 0 <= y <= (HEIGHT - 1)


def get_board_valid_move(piece_type, dl):
    # 获取所有有效的移动列表。
    # 首先获取所有的对手piece_type的位置。
    move_list = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
    opponent_type = 'O' if piece_type != 'O' else 'X'
    opponent_list = []
    for y0 in range(len(dl)):
        for x0 in range(len(dl[y0])):
            if dl[y0][x0] == opponent_type:
                opponent_list.append([x0, y0])
    # 定义有效移动列表，元素内容为（移动方位,转化方位）
    valid_move_list = []
    # 然后遍历对手棋子
    for x0, y0 in opponent_list:
        # 遍历对方棋子的八个方向
        for xm, ym in move_list:
            # 获取对角的方位
            opx = x0 - xm
            opy = y0 - ym
            # 获取移动方位
            mvx = x0 + xm
            mvy = y0 + ym
            # 首先对位和移动方位需要在棋盘上,然后对位棋子类型为piece_type，移动方位无棋子
            if is_on_board(opx, opy) and is_on_board(mvx, mvy) and dl[opy][opx] == piece_type and not dl[mvy][mvx]:
                valid_move_list.append([(mvx+1, mvy+1), (x0+1, y0+1)])
    return valid_move_list


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


def ai_act(bd1, data):
    print('AI思考中')
    # 机器先下子，这里选择随机落子
    xx = get_board_valid_move(AI_type, data)
    if not xx:
        print('游戏结束！你赢了！')
        sys.exit()
    rd = random.choice(xx)
    # 先填子
    bd1 = add_piece(int(rd[0][0]), int(rd[0][1]), AI_type, bd1)
    data = add_date(int(rd[0][0]), int(rd[0][1]), AI_type, data)
    reversal_list = [w[1] for w in xx if rd[0] == w[0]]
    # 再反转
    for j in reversal_list:
        bd1 = add_piece(j[0], j[1], AI_type, bd1)
        data = add_date(j[0], j[1], AI_type, data)
    print(bd1)
    return bd1, data


def play_act(bd1, data):
    xx = get_board_valid_move(chess_type, data)
    gambit = False
    introduce = False
    print('玩家思考中')
    # 玩家下子，这里选择随机落子
    if not xx:
        print('游戏结束！你输了！')
        sys.exit()
    while True:
        move = input('请选择落子位置!(or r-重来；t-提示；n-退出;h-帮助)\n')
        if move.lower() == 't':
            print('可下位置：(x,y):%s' % ([i[0] for i in xx]))
        if move.lower() == 'n':
            print('Thank for playing!')
            sys.exit()
        if move.lower() == 'r':
            gambit = True
            return bd1, data, gambit, introduce
        if move.lower() == 'h':
            introduce = True
            return bd1, data, gambit, introduce
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_on_board(int(move[0])-1, int(move[1])-1):
            if [c for c in xx if c[0][0] == int(move[0]) and c[0][0] == int(move[0])]:
                # 先填子
                bd1 = add_piece(int(move[0]), int(move[1]), chess_type, bd1)
                data = add_date(int(move[0]), int(move[1]), chess_type, data)
                reversal_list = [w[1] for w in xx if w[0][0] == int(move[0]) and w[0][0] == int(move[0])]
                # 再反转
                for j in reversal_list:
                    bd1 = add_piece(j[0], j[1], chess_type, bd1)
                    data = add_date(j[0], j[1], chess_type, data)
                    print(bd1)
                    return bd1, data, gambit, introduce
        else:
            print('请输入有效值！')


def play_again():
    # 该函数 返回真 如果 玩家想要再玩一次。否则 返回假。
    print('你想再玩一次吗？(yes or no)')
    return input().lower().startswith('y')


WIDTH, HEIGHT = 8, 8
board, date = create_board(WIDTH, HEIGHT), create_date(WIDTH, HEIGHT)
game_init, show_introduce, GameIsDone = True, True, False
AI_type = "O", "X"
while True:
    if show_introduce:
        display_introduce()
        switch = input('是否现在开始！r-重来；y-继续；n-退出\n')
        if switch == 'r':
            game_init = True
            show_introduce = False
        if switch == 'y':
            if game_init:
                print('新游戏！')
                show_introduce = False
            else:
                print('现在继续!')
                show_introduce = False
        if switch == 'n':
            print('欢迎再来!')
            sys.exit()
    if game_init:
        board, date = init_game()
        chess_type = get_chess_type()
        AI_type = 'X' if chess_type == 'O' else 'O'
        act = get_act()
        game_init = False
        if act == 'N':
            board, date = ai_act(board,date)
    if GameIsDone:
        if play_again():
            game_init = True
        else:
            break
    else:
        board, date, game_init, show_introduce = play_act(board, date)
        if not bool(show_introduce or game_init):
            board, date = ai_act(board, date)
