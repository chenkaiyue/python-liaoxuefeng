import os

os.uname()

查看环境变量
os.environ

os.getenv('path')


os.path.abspath('.')

#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
#这样可以正确处理不同操作系统的路径分隔符
os.path.join('/users/michel','testdir')
('/Users/michael/testdir', 'file.txt')
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')

os.mkdir('/Users/michael/testdir')
os.rmdir('/Users/michael/testdir')

os.rename('test.txt', 'test.py')
os.remove('test.py')


[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


# 查找文件
import os,sys
def search(name,path):
    for x in os.listdir(path):
        current_path = os.path.join(path,x)
        if name == x and os.path.isfile(x):
            return current_path
        elif os.path.isdir(current_path):
            search(name,current_path)
if __name__ == "__main__":
    search_name = sys.argv[1]
    start_path = os.path.abspath('.')
    search(search_name,start_path)
