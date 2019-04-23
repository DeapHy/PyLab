import os, os.path

def resh(vibor):
    if vibor == 1:
    # Реализация 1-го задания
        n = 0
        path = input('Write Path ->')
        list = os.listdir(path)
        kolvo = len(list)
        for a in range(0,kolvo):
            if os.path.isfile(list[a]):
                n += 1
        print(n)

    if vibor == 2:
    # Реализация 2-го задания
        for i in ok: # Вывод списка на экран консоли
            print(i[0],i[1],i[2],i[3])

    if vibor == 3:
    # Реализация 3-го задания
        plus = int(input('на какое число вы желаете увеличить количество товара? '))
        for i in ok:
            i[3] = int(i[3]) + plus
            print(i[0],i[1],i[2],i[3])

    if vibor == 4:
    # Реализация 4-го задания
        dir = input('Введите директорию для сохранения файла -> ')
        e = open(dir, 'w')
        for i in ok:
            e.write(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + str(i[3]) + '\n')
        e.close()


vibor = int(input("Введите желаемый номер задания: "))
while vibor != 1 and vibor != 2 and vibor != 3 and vibor != 4:
    vibor = int(input("Введите номер варианта повторно: "))
f = open('test.txt', 'r') # Необходимо для нескольких функций, так что пришлось вставить сюда
kok = []
ko = []
ok = []
c = f.read()
kok = c.replace(' \n', ' '). split()
f.close()
lenc = len(kok)
for i in range(0,lenc): # Получаение "списка списков"
    ko = (kok[i].split(','))
    ok.append(ko[0].split(';'))
ok.sort(key = lambda i: i[2]) # Lambda - "быстрая" функция
if vibor == 1 or vibor == 2 or vibor == 3 or vibor == 4:
    resh(vibor)
    prov = input('Хотите продолжить? Введите yes, Y, 1 или no, N, 0: ')
    while prov != 'yes' and prov != 'Y' and prov != '1' and prov != 'no' and prov != 'N' and prov != '0':
        prov = input('Данный ответ некооректный/ Введите овтет еще раз. ')
    while prov == 'yes' or prov == 'Y' or prov == '1':
        vibor = int(input("Введите желаемый номер задания: "))
        while prov != 'yes' and prov != 'Y' and prov != '1' and prov != 'no' and prov != 'N' and prov != '0':
            prov = input('Данный ответ некооректный/ Введите овтет еще раз. ')
        while vibor != 1 and vibor != 2 and vibor != 3 and vibor != 4:
            vibor = int(input("Введите номер варианта повторно: "))
        resh(vibor)
        prov = input('Хотите продолжить? Введите yes, Y, 1 или no, N, 0: ')
    if prov == 'no' or prov == 'N' or prov == '0':
        exit()
