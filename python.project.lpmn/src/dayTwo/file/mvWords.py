#coding:utf-8

try:
    with open("./begin.txt", 'r') as file:
        content = file.read()
        print('begin :')
        print(content)
        try:
            with open("./end.txt", 'w') as fileTwo:
                fileTwo.write(content)
                print("\nend : \n")
        except FileNotFoundError:
            print('Not found')
except FileNotFoundError:
    print('Not found')

