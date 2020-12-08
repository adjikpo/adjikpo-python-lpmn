#coding:utf-8

def areaRectangle(x,y):
    return x * y

def perimeterRectangle(x,y):
    return (x+y)/2

def results(x,y):
    resArea = areaRectangle(x,y)
    resPerimeter = perimeterRectangle(x,y)

    print("Results:\n -Area : {} \n -Perimeter : {} \n".format(resArea,resPerimeter))

print("Hello Everyone\nThis program calculate the area and perimeter of a rectangle\n")
numberX= int(input("Entrer a number : \n"))
numberY= int(input("Enter another number :\n"))

results(numberX,numberY)