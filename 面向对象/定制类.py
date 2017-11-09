class Student(object):
    def __str__(self):
        return "student object %s" % self.name
    #print Student("jsi")

    __repr__ = __str__
    # s = Student("mich")
    # >> s


## __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该
# 迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b = self.b,self.a
        if self.a > 10000:
            raise StopIteration
        return self.a
for n in Fib():
    print n

## __getitem__
# 返回的是所需的列表的下标
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b = 1,1
            for x in range(item):
                a,b = b,a+b
            return a


        if isinstance(item,slice):
            start = item.start
            stop = item.stop
            a,b = 1,1
            L=[]
            for x in range(stop):
                if x > start:
                    L.append(a)
                a,b = b,a+b
            return L


## __getattr__
def __getattr__(self,attr):
    if attr == "age":
        return 25
    raise AttributeError("has not %s" % attr)

class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain("%s%s" % (self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__


#>>> Chain().status.user.timeline.list
#'/status/user/timeline/list'


##__call__
## 直接调用对象
class Student(object):
    def __call__(self, *args, **kwargs):
        print "hello"

s=Student("1231")
s()
#hello

callable(Student())
