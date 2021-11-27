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

# 定义全局变量，增加两次机会
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
    ===''', '''
 +---+
[O   |
/|\\  |
/ \\  |
    ===''', '''
 +---+
[O]  |
/|\\  |
/ \\  |
    ===''']

# 定义单词列表
new_words = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
             'Shapes': 'square triangle rectangle circle ellipse rhombus '
                       'trapezoid chevron pentagon hexagon octagon'.split(),
             'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana '
                       'cantaloupe mango strawberry tomato'.split(),
             'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog '
                        'goat leech lion lizard monkey moose mouse otter owl panda python rabbit '
                        'rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat '
                        'zebra'.split()
             }


def get_random_word(wd):
    # 这个功能是从单词列表选出一个单词
    # 首先，从单词分类里面随机选择一个种类
    word_key = random.choice(list(wd.keys()))
    # 然后，从已选择的关键字内选择一个单词
    words = random.choice(wd[word_key])
    return words, word_key


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('错误的字母：', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)
    for ii in range(len(secret_word)):
        #  用猜正确的字母替换空白
        if secret_word[ii] in correct_letters:
            blanks = blanks[:ii] + secret_word[ii] + blanks[ii + 1:]
    for letter in blanks:
        # 每隔一个空格展示猜测单词的字母
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # 获取玩家输入的字母，这个函数确保玩家必须每次输入单个字母。
    while True:
        print('猜一个字母。')
        guesses = input()
        guesses = guesses.lower()
        if len(guesses) != 1:
            print('请输入单个字母！')
        elif guesses in already_guessed:
            print('你输入了已猜过的字母，请重新输入！')
        elif guesses not in string.ascii_letters:
            print('请输入英文字母！')
        else:
            return guesses


def play_again():
    # 该函数 返回真 如果 玩家想要再玩一次。否则 返回假。
    print('你想再玩一次吗？(yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N 2')
print('火~ 柴~ 人~ 升~ 级~ 版~')
difficulty = 'E'
while True:
    print('请设定难度： E-简单，M-中等，H-困难。')
    difficulty = input().upper()
    if difficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    if difficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]
    if difficulty in ['E', 'M', 'H']:
        break
    else:
        print('请输入有效值！')
missedLetters = ''
correctLetters = ''
secretWord, secretSet = get_random_word(new_words)
gameIsDone = False
while True:
    print('提示，该单词与%s有关！' % secretSet)
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
            print('猜对了！这个秘密单词是%s，你赢了！' % secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # 检查玩家是否因为猜错了太多次导致失败
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            display_board(missedLetters, correctLetters, secretWord)
            print('你已经用光了所有猜测机会！\n'
                  '正确答案是%s' % secretWord)
            gameIsDone = True
    # 询问玩家是否重新再来，当然是游戏结束时
    if gameIsDone:
        if play_again():
            missedLetters = ''
            correctLetters = ''
            secretWord, secretSet = get_random_word(new_words)
            gameIsDone = False
        else:
            break
