import socket

socks = socket.socket()
socks.bind(('', 9090))
socks.listen(1)
conn, addr = socks.accept()

print('connected:', addr)

while True:
    mat1 = conn.recv(1024).decode()
    if not mat1:
        break
    rez = []; mat = []; line1 = []; line2 = []
    mat.append(mat1[2]); mat.append(mat1[4]); mat.append(mat1[7]); mat.append(mat1[9])
    line1.append(mat[0]); line1.append(mat[1])
    line2.append(mat[2]); line2.append(mat[3])
    det = int(line1[0]) * int(line2[1]) - int(line1[1]) * int(line2[0])
    mezh = line1 + line2
    length = len(mezh)
    for i in range(0, length):
        rez1 = int(mezh[i]) * det
        rez.append(rez1)
    rezu = str(rez)
    conn.send(rezu.encode())

conn.close()
