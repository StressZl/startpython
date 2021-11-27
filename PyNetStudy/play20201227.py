# a = [1, 3, 5, 7, 9]
# b = [2, 4, 6, 8, 10]
#
#
# def foo(a, b):
#     c = a + b
#     d = []
#     while 1:
#         if not c:
#             break
#         d.append(min(c))
#         del c[c.index(min(c))]
#     return d
#
#
# a1 = a
# for i in b:
#     for index, j in enumerate(a):
#         if j >= i:
#             a1.insert(index, i)
#             break
#     else:
#         a1.append(i)
# print(a1)
list1 = ['爱', '死亡', '机器人']
list2 = ['仪式', '永生', '基因控制']
list3 = ['信仰', '轮回', '繁殖']
for i in list1:
    for j in list2:
        for k in list3:
            print(' '.join([i, j, k]))


