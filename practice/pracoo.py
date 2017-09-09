#--coding:utf-8--
class tt:
    def _onexiahua(self):
        print'one _'
    def __twoxiahua(self):
        print'two __'
    @staticmethod
    def staticMethod():
        print 'staticmethod'
    @classmethod
    def classMethod(cls):
        print cls.__dict__
        print 'classMethod'

class tt2(tt):
    def _onexiahua(self):
        tt._onexiahua(self)
        self.__twoxiahua()
        print '2 _onexiahua'
    def __twoxiahua(self):
        tt._tt__twoxiahua(self)
        print '2 __twoxiahua'

if __name__ == "__main__":
    #tt2()._onexiahua()
    #tt2()._tt2__twoxiahua()
    tt.classMethod()
