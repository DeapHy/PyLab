my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
b = my_string.split(";_")
a = len(b)
print('Ф      И      О            О студенте')
for i in range(1,a):
    c = b[i].split(";")
    print(c[0],c[1],' ',c[2],"  ",c[4],c[3])
