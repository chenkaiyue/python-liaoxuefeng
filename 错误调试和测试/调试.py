# coding=utf-8


# ##断言
# assert n!=0,'n is zero'
# 关闭断言：
# python -0 err.py



##logging
import logging
logging.basicConfig(level=logging.INFO)
s='0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n