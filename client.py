import PySimpleGUI as sg 

##-----DEFAULT SETTINGS----------------------------------##
bw: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F8F8F8")}
bt: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F1EABC")}
bo: dict = {'size':(15,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#ECA527"), 'focus':True}

class CalculatorGUI:
    
    def __init__(self) -> None:
        
        ##-----WINDOW AND LAYOUT---------------------------------##
        self.layout: list = [
            [sg.Text('PyDataMath-II', size=(50,1), justification='right', background_color="#272533", 
                text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
            [sg.Text('0.00', size=(18,1), justification='right', background_color='black', text_color='red', 
                font=('Digital-7',48), relief='sunken', key="_DISPLAY_")],
            [sg.Button('C',**bt), sg.Button('CE',**bt), sg.Button('%',**bt), sg.Button("/",**bt)],
            [sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button("*",**bt)],
            [sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button("-",**bt)],
            [sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button("+",**bt)],    
            [sg.Button('0',**bw), sg.Button('.',**bw), sg.Button('=',**bo, bind_return_key=True)]
        ]

        self.window: object = sg.Window('PyDataMath-II', layout=self.layout, background_color="#272533", size=(580, 660), return_keyboard_events=True)

        ##----CALCULATOR FUNCTIONS-------------------------------##
        self.var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

        self.calculate: function = None
        
    #-----HELPER FUNCTIONS
    def format_number(self) -> float:
        ''' Create a consolidated string of numbers from front and back lists '''
        return float(''.join(self.var['front']).replace(',','') + '.' + ''.join(self.var['back']))

    def update_display(self, display_value: str):
        ''' Update the calculator display after an event click '''
        try:
            self.window['_DISPLAY_'].update(value='{:,.2f}'.format(display_value))
        except:
            self.window['_DISPLAY_'].update(value=display_value)

    #-----CLICK EVENTS
    def number_click(self, event: str):
        ''' Number button button click event '''
        if self.var['decimal']:
            self.var['back'].append(event)
        else:
            self.var['front'].append(event)
        self.update_display(self.format_number())
        

    def clear_click(self):
        ''' CE or C button click event '''
        self.var['front'].clear()
        self.var['back'].clear()
        self.var['decimal'] = False 

    def operator_click(self, event: str):
        ''' + - / * button click event '''
        self.var['operator'] = event
        try:
            self.var['x_val'] = self.format_number()
        except:
            self.var['x_val'] = self.var['result']
        self.clear_click()


    def calculate_click(self):
        ''' Equals button click event '''
        
        try:
            self.var['y_val'] = self.format_number()
        except ValueError: # When Equals is pressed without any input
            self.var['x_val'] = self.var['result']
            
        expression = str(self.var['x_val']) + self.var['operator'] + str(self.var['y_val'])
        
        try:
            self.var['result'] = self.calculate(expression)
            # self.var['result'] = eval(expression)
            
            self.update_display(self.var['result'])
            self.clear_click()    
        except:
            self.update_display("ERROR! DIV/0")
            self.clear_click()

    def mainloop(self):
        #-----MAIN EVENT LOOP------------------------------------##
        while True:
            event, values = self.window.read()
            print(event)
            if event is None:
                break
            if event in ['0','1','2','3','4','5','6','7','8','9']:
                self.number_click(event)
            if event in ['Escape:27','C','CE']: # 'Escape:27 for keyboard control
                self.clear_click()
                self.update_display(0.0)
                self.var['result'] = 0.0
            if event in ['+','-','*','/']:
                self.operator_click(event)
            if event == '=':
                self.calculate_click()
            if event == '.':
                self.var['decimal'] = True
            if event == '%':
                self.update_display(self.var['result'] / 100.0)