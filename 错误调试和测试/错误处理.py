import logging
try:
    r = 10/int('a')
except ValueError,e:
    print "error",e
except StandardError,e:
    logging.exception(e)
else:
    print "sdfa"
finally:
    print "noerrors"

#logging:同样是出错，但程序打印完错误信息后会继续执行，并正常退出
#logging.exception(e)

def bar(s):
    try:
        10/0
    except StandardError,e:
        print "error"
        raise



