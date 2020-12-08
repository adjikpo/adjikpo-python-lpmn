#coding:utf-8

print("Hello Everyone !")


numberX= input("Entrer a integer and even number : \n")
numberY= input("Enter another integer and even  number :\n")

error = 0

try:
    numberX = int(numberX)
    numberY = int(numberY)
except:
    error = error +1
    print('not a integer')
try:
    assert numberX % 2 == 0
except:
    error = error +1
    print('not even')
try:
    assert numberY != 0
except:
    error = error +1
    print('equals zero')

if error == 0:
    print("Results: \n {} ÷ {} = {} " .format(numberX,numberY,(numberX/numberY)))
    print("Thanks you ! See you soon ")

