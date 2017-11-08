class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        self._score = value

    # 只读属性
    @property
    def age(self):
        return 2014-self._birth

s = Student()
s.score =100
print s.score