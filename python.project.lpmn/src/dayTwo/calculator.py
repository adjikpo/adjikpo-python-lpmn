#coding:utf-8

print("Hello Everyone !")

def add(x,y):
    return  x +y

def mult(x,y):
    return x*y

def sub(x,y):
    return  x-y

def div(x,y):
    return x/y

def allResOfOperations(x,y):
    resAdd = add(x,y)
    resMult = mult(x,y)
    resSub = sub(x,y)
    resDiv = div(x,y)

    print("All results of Operation: \n -Addition :{} \n -Multiplication :{} \n -Subtraction :{} \n -Division :{} \n" .format(resAdd,resMult,resSub,resDiv))

numberX= int(input("Entrer a number : \n"))
numberY= int(input("Enter another number :\n"))

allResOfOperations(numberX,numberY)