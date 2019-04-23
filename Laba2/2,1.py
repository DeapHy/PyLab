stro = input()
stro2 = stro.split()
b = len(stro2)
rez = []
for i in range(0,b):
    if len(stro2[i]) > 5 and len(stro2[i]) < 10:
        rez.append(stro2[i])
print(rez)
