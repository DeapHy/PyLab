from random import randrange
def prog():
    a = randrange(1,101)
    print("Угадай число :)")

    ch = int(input("Твой вариант: "))
    while a != ch:
      if ch > a:
        print("Бери меньше")
      elif ch < a:
        print("Бери больше")
      ch = int(input("Попробуй еще раз: "))
    if ch == a:
      print('''----------------------------------
Поздравляю, ты угадал(-a) число :D''')

prog()
print("Хочешь попробовать еще раз?")
b = input('''Твой вариант(да/нет)
''')
while b == "да" or b == "y" or b == "yes" or b == "da" or b == "Да":
      prog()
      print("Хочешь попробовать еще раз?")
      b = input('''Твой вариант(да/нет)
''')
print("Спасибо за игру!")
