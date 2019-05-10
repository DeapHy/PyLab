import socket

sock = socket.socket()
sock.connect(('localhost', 9092))
mission = input('Введите матрицу в соответствии с шаблоном: [ 1 2; 3 4]: ')
sock.send(mission.encode())

answer= sock.recv(1024).decode()
sock.close()
print('Результат работы сервера: ', answer)
