f=open(r'text.txt',r)
f.read()#一次读完
f.close()

with open('test.txt','r') as f:
    print f.read()
#with自带关闭

#，调用readline()可以每次读取一行内容， 生成器
# 调用readlines()一次读取所有内容并按行返回list（行的list）  迭代器
for line in f.readlines():
    print line.strip()


#非ascii码的文件:
f = open('/Users/michael/test.jpg', 'rb')
f.read()
#'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
u = f.read().decode('gbk')

import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read()

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
#当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
# 空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入
# 的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，
# 剩下的丢失了