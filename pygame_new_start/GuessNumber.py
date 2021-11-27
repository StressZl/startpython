# This is Guess the Number game
import random
Number0 = random.randint(0, 20)
myName = input('你好!你的名字是？\n')
for i in range(6):
    GuessesNumber = int(input('欢迎你！%s，请猜一个1到20的数字，你有6次机会！这是第%s次。\n' % (myName, i+1)))
    if GuessesNumber > Number0:
        print('猜错了，比%s小' % GuessesNumber)
    elif GuessesNumber < Number0:
        print('猜错了，比%s大' % GuessesNumber)
    elif GuessesNumber == Number0:
        print('猜对了!')
        break
else:
    print('很遗憾，你一次都没猜对！')
