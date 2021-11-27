from translate import Translator


# 以下是将简单句子从英语翻译中文
translator = Translator(to_lang="chinese")
translation = translator.translate("Good night!")
print(translation)


# 在任何两种语言之间，中文翻译成英文
# translator = Translator(from_lang="chinese", to_lang="english")
# translation = translator.translate("我想你")
# print(translation)

# words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow dear dog donkey duck ' \
#         'eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter ' \
#         'owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth ' \
#         'snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
# chinese_words_dic = {}
# for i in words:
#     chinese_words_dic[i] = translator.translate(i)
#     print(chinese_words_dic[i])
# print(chinese_words_dic)
this = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
for i in this.split('\n'):
    print(translator.translate(i))