class Myobject(Object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
obj = Myobject()

hasattr(obj,'x')
setattr(obj,'y',19)
getattr(obj,'y')
getattr(obj,'y','not exist')
fn = getattr(obj,'power')
fn()


动态绑定
class Student(object):
	pass
from types import MethodType
s = Student()
def set_age(self,age):
	self.age = age

# 绑定给一个对象，其他的对象不能使用
# ，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
绑定给class
通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
Student.set_age = MethodType(set_age,None,Student)


__slots__
限制class能添加的属性
clas Student(object):
	__slots__ = ('name','age')

s = Student()
s.age=23
s.score=99 #报错


@property
Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score is int')
		if value < 0 or value > 100:
			raise ValueError('score 0-100')
		self._score = value
s = Student()
s.score = 99
s.score
定义只读属性的话就只用设置@property,不设置@variable.setter


定制类
