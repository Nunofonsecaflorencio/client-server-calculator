import socket
from client import CalculatorGUI
from server import send_request, connect_to_server
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # python main.py [remote ip] [port]
        client_socket = connect_to_server(sys.argv[1], int(sys.argv[2]))
    else:
        client_socket = connect_to_server('localhost', 5000)

    client = CalculatorGUI()
    client.calculate = lambda expr: send_request(expr, client_socket)
    client.mainloop()

    client_socket.close()
