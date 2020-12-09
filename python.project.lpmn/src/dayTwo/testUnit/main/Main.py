#coding:utf-8

# import package.calculate
import sys
sys.path.append('..')
from package.Calculate import Calculate

numberX= int(input("Entrer a number : \n"))
numberY= int(input("Enter another number :\n"))

Calculate().allResOfOperations(numberX,numberY)
