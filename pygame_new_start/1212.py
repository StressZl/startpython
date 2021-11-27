import shutil
import os
import re
# 切换文件目录
os.chdir('D:\\')
os_list = os.listdir('D:\\')
for i in os_list:
    os_path = 'D:\\' + i
    print(os_path)
    print(os.path.getsize(os_path))
    print("dir:"+str(os.path.isdir(os_path)))
    print("file:"+str(os.path.isfile(os_path)))
if 'copytest' in os_list:
    # 删除非空文件夹
    shutil.rmtree("D:\\copytest")
os.mkdir("D:\\copytest")
# 复制文件
shutil.copy('D:\\test1.txt', 'D:\\copytest')
shutil.copy('D:\\test1.txt', 'D:\\copytest\\test2.txt')
# 移动文件
shutil.move('D:\\copytest\\test1.txt', 'D:\\test1.txt')
# 删除文件
os.unlink('D:\\copytest\\test2.txt')
# 删除空文件夹
os.rmdir("D:\\copytest")
# 删除非空文件夹
os.makedirs("D:\\copytest\\copytest1\\copytest2")
shutil.rmtree("D:\\copytest")
print('test')


