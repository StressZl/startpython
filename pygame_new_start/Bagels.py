"""
 Bagels 百吉圈(硬面包);你猜测的三个数都不在神秘数字中
 Pico  你猜中了，但位置不对
 Fermi 你猜对了位置和数字
"""
import random

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_num():
    # 返回一个NUM_DIGITS长度不存在相同数字的随机整数
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(gs, secret_num):
    # 给用户返回一个Pico，Fermi和Bagels字符串
    if gs == secret_num:
        return '你猜对了！'
    clues = []
    for i in range(len(gs)):
        if gs[i] == secret_num[i]:
            clues.append('\033[0;33mFermi\033[0m')
        elif gs[i] in secret_num:
            clues.append('\033[0;32mPico\033[0m')
    if len(clues) == 0:
        return '\033[0;31mBagels\033[0m'
    clues.sort()
    return ' '.join(clues)


def is_only_digits(num):
    # 如果全是数字返回True，否则返回False
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


print('我想了一个%s位的数，试试猜下这个数字。' % NUM_DIGITS)
print('我会给你一点线索。')
print('当我说：      这意味着：')
print('      \033[0;31mBagels\033[0m         这里面没有正确的数字。')
print('      \033[0;32mPico\033[0m           这里面存在正确的数字，但是位置不对。')
print('      \033[0;33mFermi\033[0m          这里面存在一个正确的数字和位置。')

while True:
    secretNum = get_secret_num()
    print('我想好了一个数字，你有%s次机会去猜对它。' % MAX_GUESS)

    guessTaken = 1
    while guessTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not is_only_digits(guess):
            print('第%s次猜测：' % guessTaken)
            guess = input()

        print(get_clues(guess, secretNum))
        guessTaken += 1

        if guess == secretNum:
            break
        if guessTaken > MAX_GUESS:
            print('你浪费了所有次数，答案是%s。' % secretNum)

    print('你想再玩一次吗？（yes or no）')
    if not input().lower().startswith('y'):
        break
