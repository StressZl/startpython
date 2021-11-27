"""
               火柴人游戏流程图

                    开始———————————————————
                     |                     \
              想到一个神秘的单词             \
                     |                     \
          ———向玩家显示游戏板和空格——        \
         |           |            |        \
         |  要求玩家猜测一个字母====玩家已经猜过这个字母
         |   |             |     |         |
       字母存在          字母不存在          |
            |              |               |
    玩家猜对所有字母     用完火柴人的身体     |
           |              |                |
         询问玩家是否要继续玩————————————————
                 |
               结束
"""

import random
import string
# 定义全局变量
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
 |\\  |
     |
    ===''', '''
 +---+
 O   |
/|\\  |
     |
    ===''', '''
 +---+
 O   |
/|\\  |
/    |
    ===''', '''
 +---+
 O   |
/|\\  |
/ \\  |
    ===''']

# 定义单词列表
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow dear dog donkey duck ' \
        'eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter ' \
        'owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth ' \
        'snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

# 依靠翻译模块翻译的字典（果然全是动物）
words_dic = {'ant': '蚂蚁', 'baboon': '狒狒', 'badger': '獾', 'bat': '蝙蝠', 'bear': '熊',
             'beaver': '美洲河狸', 'camel': '駱駝', 'cat': '猫', 'clam': '蛤蜊', 'cobra': '眼鏡蛇',
             'cougar': '美洲狮', 'coyote': '小狼', 'crow': '乌鸦', 'dear': '鹿', 'dog': '狗',
             'donkey': '驴子', 'duck': '鸭子', 'eagle': '鷹', 'ferret': '雪貂', 'fox': '狐狸',
             'frog': '青蛙', 'goat': '山羊', 'goose': '鹅', 'hawk': '鹰', 'lion': '狮子',
             'lizard': '蜥蜴', 'llama': '大羊駝', 'mole': '鼹鼠', 'monkey': '猴子', 'moose': '驼鹿',
             'mouse': '老鼠', 'mule': '騾', 'newt': '蠑螈', 'otter': '水獺', 'owl': '猫头鹰',
             'panda': '熊貓', 'parrot': '鹦鹉', 'pigeon': '鸽子', 'python': '蟒蛇', 'rabbit': '兔',
             'ram': '公羊', 'rat': '大鼠', 'raven': '渡鴉', 'rhino': '犀牛', 'salmon': '三文鱼',
             'seal': '海豹', 'shark': '鲨鱼', 'sheep': '綿羊', 'skunk': '臭鼬', 'sloth': '斯洛特',
             'snake': '蛇', 'spider': '蜘蛛', 'stork': '鸛', 'swan': '天鵝', 'tiger': '老虎',
             'toad': '蟾蜍', 'trout': '鳟鱼', 'turkey': '火鸡', 'turtle': '海龟', 'weasel': '鼬屬',
             'whale': '鲸鱼', 'wolf': '狼', 'wombat': '袋熊', 'zebra': '斑馬'}


def get_random_word(wd):
    # 这个功能是从单词列表选出一个单词
    word_index = random.randint(0, len(wd)-1)
    return wd[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('错误的字母：', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)
    for index1 in range(len(secret_word)):
        #  用猜正确的字母替换空白
        if secret_word[index1] in correct_letters:
            blanks = blanks[:index1] + secret_word[index1] + blanks[index1 + 1:]
    for letter in blanks:
        # 每隔一个空格展示猜测单词的字母
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # 获取玩家输入的字母，这个函数确保玩家必须每次输入单个字母。
    while True:
        print('猜一个字母。')
        guessed = input()
        guessed = guessed.lower()
        if len(guessed) != 1:
            print('请输入单个字母！')
        elif guessed in already_guessed:
            print('你输入了已猜过的字母，请重新输入！')
        elif guessed not in string.ascii_letters:
            print('请输入英文字母！')
        else:
            return guessed


def play_again():
    # 该函数 返回真 如果 玩家想要再玩一次。否则 返回假。
    print('你想再玩一次吗？(yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
print('火~ 柴~ 人~')
print('\033[1;32;40m 提示：全是动物。\033[0m')
missedLetters = ''
correctLetters = ''
secretWord = get_random_word(words)
gameIsDone = False
while True:
    display_board(missedLetters, correctLetters, secretWord)
    # 让玩家输入一个字母
    guess = get_guess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # 检查玩家是否猜出了所有字母
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('猜对了！这个秘密单词是%s %s，你赢了！' % (secretWord, words_dic[secretWord]))
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # 检查玩家是否因为猜错了太多次导致失败
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            display_board(missedLetters, correctLetters, secretWord)
            print('你已经用光了所有猜测机会！\n'
                  '正确答案是%s %s' % (secretWord, words_dic[secretWord]))
            gameIsDone = True
    # 询问玩家是否重新再来，当然是游戏结束时
    if gameIsDone:
        if play_again():
            missedLetters = ''
            correctLetters = ''
            secretWord = get_random_word(words)
            gameIsDone = False
        else:
            break
