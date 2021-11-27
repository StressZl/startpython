#! python3
# mcb.pyw - 保存和加载文本到粘贴版
# 使用:py.exe mcb.pyw save <keyword> 保存文本
#     py.exe mcb.pyw <keyword> 加载文本
#     py.exe mcb.pyw list 查看已有文本
import shelve,pyperclip,sys
mcbShelf = shelve.open('mcb')
# TODO:保存粘贴板内容
# 保存变量
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# TODO:展示关键词以及加载内容
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

