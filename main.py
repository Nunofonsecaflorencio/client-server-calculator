import socket
from client import CalculatorGUI
from server import send_request, connect_to_server


if __name__ == '__main__':
    client_socket = connect_to_server('localhost', 5000)

    client = CalculatorGUI()
    client.calculate = lambda expr: send_request(expr, client_socket)
    client.mainloop()

    client_socket.close()
