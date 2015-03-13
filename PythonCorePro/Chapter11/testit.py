#! /usr/bin/env python
#Filename : testit.py
#-*-coding:utf-8-*-

def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))

    return result


def test():
    funs = (int, long,float)
    vals = (1234, 12.34, '1234', '12.34')
    for eachfun in funs:
        print '-'  * 20
        for eachVar in vals:
            retval = testit(eachfun, eachVar)
            if retval[0]:
                print '%s(%s) = ' % (eachfun.__name__, `eachVar`), retval[1]
            else:
                print '%s(%s) = FAILED:' % (eachfun.__name__, `eachVar`), retval[1]

if __name__ == '__main__':
    test()
