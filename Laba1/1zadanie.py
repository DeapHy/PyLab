from math import pow, fabs
vari = int(input('''----------------------------------
Введите необходимый вариант: '''))
if vari > 0 and vari <= 4:



    if vari == 1:
        print ('''
Введите значения данных переменых:
a b c k''')
        a, b, c, k = map(int, input().split())
        while a == 0 or b == 0 or (a + b + c * (k - a / pow(b,3))):
            print ("Вы ввели недопустимые числа, попробуйте снова")
            print ('''
Введите значения данных переменых:
a b''')
            a, b = map(int, input().split())
        rez = fabs((pow(a/b,2) + pow(c*a,2)) / (a + b + c * (k - a / pow(b,3))) + c + (k/b - k/a) * c)
        print ('Результат = ',rez)



    elif vari == 2:
        print ('''
Введите значения данных перемен:
a b c d k''')
        a, b, c, d, k = map(int, input().split())
        while a == 0 or b == 0:
            print ("Вы ввели недопустимые числа, попробуйте снова")
            print ('''
Введите значения данных переменых:
a b''')
            a, c = map(int, input().split())
        rez = fabs((pow(a,2) * (1 - pow(b,3) - pow(c,3)) * (b - c + c * (k - d/pow(b,3)))) - pow((k/b - k/a) * c,2) - 20000)
        print ('Результат = ',rez)



    elif vari == 3:
        print ('''
Введите значения данных перемен:
a b c''')
        a, b, c = map(int, input().split())
        while c == a:
            print ("Вы ввели недопустимые числа, попробуйте снова")
            print ('''
Введите значения данных переменых:
a c''')
            a, c = map(int, input().split())
        rez = fabs(1 - a * pow(b,c) - a * (pow(b,2) - pow(c,2)) + (b - c + a) * (12 + b) / (c - a))
        print ('Результат = ',rez)



    elif vari == 4:
        print ('''
Введите значения данных перемен:
a b c d f''')
        a, b, c, d, f = map(int, input().split())
        while a == 0 or f == 0:
            print ("Вы ввели недопустимые числа, попробуйте снова")
            print ('''
Введите значения данных переменых:
a f''')
            a, f = map(int, input().split())
        rez = fabs(a - b * c * pow(d,3) + (pow(c,5) - pow(a,2)) / a + pow(f,3) * (a - 213))
        print ('Результат = ',rez)



else: print('Данный вариант не существует')
