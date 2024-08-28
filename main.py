from client import CalculatorGUI

if __name__ == '__main__':
    client = CalculatorGUI()
    client.calculate = eval # call server here
    client.mainloop()