#coding:utf-8
class Calculate :
    def add(self,x,y):
        return  x +y

    def mult(self,x,y):
        return x*y

    def sub(self,x,y):
        return  x-y

    def div(self,x,y):
        try:
            return x/y
        except ZeroDivisionError:
            print("Impossible to do a zero division")

    def allResOfOperations(self,x,y):
        resAdd = add(self,x,y)
        resMult = mult(self,x,y)
        resSub = sub(self,x,y)
        resDiv = div(self,x,y)

        print("All results of Operation: \n -Addition :{} \n -Multiplication :{} \n -Subtraction :{} \n -Division :{} \n" .format(resAdd,resMult,resSub,resDiv))