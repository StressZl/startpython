# 习题册
'''
a 1
...
z 26
aa 1*26+1
...
az 1*26+26
ba 2*26+1
...
zz 26*26+26
aaa  1*(26**2)+1*(26**1)+1*(26**0)
aaaa 1*(26**3)+1*(26**2)+1*(26**1)+1*(26**0)

'''
# 实际上就是26进制的变形
letterstr = 'abcdefghijklmnopqrstuvwxyz'
print(letterstr.find('a')+1)
codelist = 'xxx'
l = len(codelist)
print(l)
n = 0
for i in codelist:
   l = l-1
   n += (letterstr.find(i)+1)*(26**l)
print(n)


'''
【请在一个字符串中找出连续最长的数字串】
请在一个字符串中找出连续最长的数字串，并返回这个数字串。
如果存在长度相同的连续数字串，返回最后一个。如果没有符合条件的字符串，返回空字符串""。
注意：
数字串可以由数字"0-9"、小数点"."、正负号"±"组成，长度包括组成数字串的所有符号。
"."、“±"仅能出现一次，”."的两边必须是数字，"±"仅能出现在开头且其后必须要有数字。
长度不定，可能含有空格。
例子：1234567890abcd9.+12345.678.9ed
输出：+12345.678
'''
str1 = '1234567890abcd9.+12345.678.9ed'
save_list = []
save = ''
for num, i in enumerate(str1):
    if i.isnumeric():
        if save:
            if save[-1] == '+' or \
                    save[-1] == '-'  or \
                    save[-1] == str(int(i)-1) or \
                    (save[-1] == '.' and save[-2] == str(int(i)-1)):
                save += i
            else:
                save_list.append(save)
                save = i
        else:
            save += i
    elif i == '+' or i == '-':
        if save:
            save_list.append(save)
            save = i
        else:
            save = i
    elif i == '.':
        if save:
            if i not in save:
                if num+1 <= len(str1):
                    print(str1[num+1])
                    if str1[num+1].isnumeric():
                        save += i
                    else:
                        save_list.append(save)
                        save = ''
            else:
                save_list.append(save)
                save = ''
if save:
    save_list.append(save)
print(save_list)
max_i=''
for i in save_list:
    if len(max_i) < len(i):
        max_i = i
print(max_i)