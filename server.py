import socket
import sys

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started, listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connection from {addr}')

        # Receive and process data
        try:
            while True:
                data = client_socket.recv(1024)
                if data:
                    expression = data.decode('utf-8')
                    print(f"Received expression: {expression}")

                    try:
                        result = str(eval(expression))
                    except Exception as e:
                        result = 'ERROR'

                    client_socket.sendall(result.encode('utf-8'))
                else:
                    break
        except Exception as e:
            print(f'Error: {e}')
        finally:
            client_socket.close()
            print(f"Connection closed from {addr}")


def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    return client_socket


def send_request(expression, client_socket):
    print(f"Sending expression to server: {expression}")
    client_socket.sendall(expression.encode('utf-8'))

    result = client_socket.recv(1024)
    print(f"Received result from server: {result.decode('utf-8')}")

    return result.decode('utf-8')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # python main.py [ip] [port]
        start_server(sys.argv[1], int(sys.argv[2]))
    else:
        start_server('localhost', 5000)
