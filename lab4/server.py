import socket

socks = socket.socket()
socks.bind(('', 9092))
socks.listen(1)
conn, addr = socks.accept()

print('connected:', addr)

while True:
    mat1 = conn.recv(1024).decode()
    if not mat1:
        break
    leng = len(mat1)
    mat = mat1[2:leng-2]
    rez = []
    strok = mat.split('; ')
    line1 = strok[0].split(' ')
    line2 = strok[1].split(' ')
    det = int(line1[0]) * int(line2[1]) - int(line1[1]) * int(line2[0])
    mezh = line1 + line2
    length = len(mezh)
    for i in range(0, length):
        rez1 = int(mezh[i]) * det
        rez.append(rez1)
    rezu = str(rez)
    conn.send(rezu.encode())

conn.close()
