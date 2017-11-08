try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name="bob",age=20)
s = pickle.dumps(d)
#返回的是str
f.write(s)
pickle.loads(s)



with open('dump.txt','w') as f:
    pickle.dump(d,f)


f=open('dump.txt','rb')
d = pickle.load(f)
f.close()


------------json---------------
import json
json_str = json.dumps(d)

json.loads(json_str)
json.load(f)




---------对象转换为json------------
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)


def student2dict(std):
    return {
        'name':std.name
        'age':std.age
        'score':std.score
    }
print (json.dumps(s,default=student2dict))

print(json.dumps(s,lambda obj:obj.__dict__))




def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))
