from socket import *
import time
#Импорт библиотеки
host = 'localhost'
port = 8888
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

    question = input('Do you want to quit? y\\n: ')
    # Если мы захотели выйти из программы
    if question == 'y': break

    print('wait connection...')
    # устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    client, addr = s.accept()
    # принимаем запрос и устанавливает соединение
    print('client addr: ', addr) # распечатаем адреас клиента

    # recv - получает сообщение TCP
    data = client.recv(1024)
    # если ничего не пришло , завершим программу
    if not data:
        conn.close()
        break
    else:
        print(data)
        # send - передает сообщение TCP
        timestr = time.ctime(time.ctime()) + "\n"
        conn.send(timestr.encode('ascii'))
        # close - закрывает сокет
        conn.close()

tcp_socket.close()
