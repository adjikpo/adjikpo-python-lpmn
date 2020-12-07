#coding:utf-8

currency = str(input("Choose you're currency ($ or €) :\n "))

if (currency == '$'):
    value = float(input("Value: \n"))
    valueInDollar = value * 1.21
    print("{}€ = {}$".format(value, valueInDollar))
elif (currency == '€'):
    value = float(input("Value: \n"))
    valueInEuro = value * 0.83
    print("{}$ = {}€".format(value, valueInEuro))
else :
    print("BYE! see you soon")

