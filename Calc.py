# coding:utf-8

class Calculation():
    def add(self,x,y):
        return x + y
    def sub(self,x,y):
        return x - y
    def mul(self,x,y):
        return x * y
    def mov(self,x,y):
        try:
            return x / y
        except BaseException as msg:
            return msg