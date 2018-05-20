from socket import *
import time
#Импорт библиотеки
host = 'localhost'
port = 7777
addr = (host, port)
#данные сервера
#Переменный для удобства
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
#связываем адрес и порт с сокетом

s.listen(5)
#запускаем прием TCP

while True:
    # Бесконечный цикл работы программы

    print('wait connection...')
    # устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    client, addr = s.accept()
    # принимаем запрос и устанавливает соединение
    print('client addr: ', addr) # распечатаем адреас клиента

    # recv - получает сообщение TCP
    # если ничего не пришло , завершим программу
    # send - передает сообщение TCP
    timestr = time.ctime(time.time()) + "\n"
    client.send(timestr.encode('ascii'))
    client.close()
