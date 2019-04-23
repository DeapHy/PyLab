N = int(input("Введите количество чисел: "))
while N < 10:
    print("Данное количество чисел не удовлетворяет условию. Повторите попытку")
    N = int(input("Введите повторно количество чисел: "))
ryad = input("Введите числа через пробел: ")
otdelno = ryad.split(" ")
kolvo = len(otdelno)
while kolvo != N:
    print ('Вы Ввели неверное количество чисел, повторите попытку')
    ryad = input("Введите числа через пробел: ")
    otdelno = ryad.split(" ")
    kolvo = len(otdelno)
del otdelno[3:7]
novie = input("Введите 2 новых значения через пробел ")
otdelno2 = novie.split(' ')

'''Вводить новые числа через аппенд'''

rez = otdelno + otdelno2
print(rez)
