import os

print('***获取当前目录***')
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname(".")))
# __file__ 为当前文件, 若果在ide中运行此行会报错,可改为 #d = path.dirname('.')
# 但是改为.后，就是获得当前目录，接着使用dirname函数访问上级目录
print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))
print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
