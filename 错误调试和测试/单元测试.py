class Dict(dict):
    def __int__(self,**kw):
        super(Dict,self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("dict has no %s" % key)

    def __setattr__(self, key, value):
        self[key] = value


import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEquals(d.a,1)
        self.assertEquals(d.b,'test')
        self.assertEquals(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key,'value')

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']


if __name__ = "__main__":
    unittest.main()
或者直接运行:
python -m unittest 单元测试.py