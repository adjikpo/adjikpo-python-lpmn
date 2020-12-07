#coding:utf-8

for x in range(11):
    print("=================")
    print("Table of {} \n".format(x))
    for y in range (11):
        res = x*y
        print("{}*{} = {}\n".format(x,y,res))
    