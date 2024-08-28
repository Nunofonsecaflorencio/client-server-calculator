from client import CalculatorGUI

def connect_to_server(host, port): 
    # TODO: returns a socket
    pass

def send_request(expression):
    # TODO: Send the expression to the server, wait for server response and returns the result
    return eval(expression) # temporary

if __name__ == '__main__':
    socket = connect_to_server('localhost', 5000)
    
    client = CalculatorGUI()
    client.calculate = send_request
    client.mainloop()
    
    # socket.close()