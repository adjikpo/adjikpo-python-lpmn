#coding:utf-8

value = int(input("Enter a value : \n"))

if value%2 == 0:
    print('This number is even and not multiple of 3')

if value%2 !=0:
    if value%3 == 0:
        print('This number is obb and multiple of 3 ')

    else: 
        print('This number is obb and not multiple of 3 ')