import select
import sys
from socket import socket, AF_INET, SOCK_STREAM


class Server:
    def __init__(self, address: str, port: int, user_quantity: int, timeout: float):
        self.address = address
        self.port = port
        self.user_quantity = user_quantity
        self.timeout = timeout
        self.connection_stats = (self.address, self.port)
        self.socket_server = None

    def _configure_connection(self):
        socket_server = socket(AF_INET, SOCK_STREAM)
        socket_server.bind(self.connection_stats)
        socket_server.listen(self.user_quantity)
        socket_server.settimeout(self.timeout)
        return socket_server

    def _read_requests(self, readers_clients, all_clients):
        responses = {}
        for sock in readers_clients:
            try:
                data = sock.recv(1024).decode('UTF-8')
                responses[sock] = data
            except:
                print('Клиент {} {} отсоеденился '.format(sock.fileno(), sock.getpeername()))
                all_clients.remove(sock)
        return responses

    def _write_responses(self, requests, writers_clients, all_clients):
        for sock in writers_clients:
            for msg in requests.values():
                try:
                    sock.send(msg.encode('UTF-8'))
                except:
                    print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                    sock.close()
                    all_clients.remove(sock)

    def start(self):
        clients = []
        try:
            self.socket_server = self._configure_connection()
            print('Конфигурация сервера завершена успешно.')
        except OSError:
            print('Ошибка при конфигурации сервера. Завершение работы приложения...')
            sys.exit(1)
        while True:
            try:
                conn, addr = self.socket_server.accept()
            except OSError as error:
                pass
            else:
                print("Получен запрос на соединение от %s" % str(addr))
                clients.append(conn)
            finally:
                readers = []
                writers = []
                try:
                    readers, writers, error = select.select(clients, clients, clients, 0)
                except:
                    pass
                requests = self._read_requests(readers, clients)
                self._write_responses(requests, writers, clients)

if __name__ == '__main__':
    server = Server('localhost', 7777, 10, 0.2)
    server.start()