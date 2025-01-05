from typing import List, Callable
import sys

from PyQt6 import QtWidgets as qtw

from ui import Ui_MainWindow

num_button_names = [f'button_{num}' for num in range(10)]

def is_num_button(button_name:qtw.QPushButton):
    return button_name in num_button_names



class CalculatorState:
    def __init__(self, state_name):
        super().__init__()
        self.state_name=state_name
    def __str__(self):
        return str(self.state_name)

class CalcStates:
    INPUT = CalculatorState('INPUT')
    INPUT_2 = CalculatorState('INPUT_2')
    OPERATION = CalculatorState('OPERATION')
    RESULT = CalculatorState('RESULT')
      
class CalculatorOperation:
    def __init__(self,
                operation_name:str, operation_char:str, operation_func:Callable,
                ):
        self.operation_name=operation_name
        self.operation_char=operation_char
        self.operation_func=operation_func
    
class CalcOperations:
    PLUS=CalculatorOperation('PLUS', '+', lambda n1, n2: n1 + n2,)
    MINUS=CalculatorOperation('MINUS', '-', lambda n1, n2: n1 - n2,)
    MULTIPLAYING=CalculatorOperation('MULTIPLAYING', '*', lambda n1, n2: n1 * n2,)
    DIVIDE=CalculatorOperation('DIVIDE', '/', lambda n1, n2: n1 / n2,)
    
class MainWindow(qtw.QMainWindow):
    def get_res_text(self):
        return self.ui.result_label.text()
    def set_res_text(self, res_text):
        res_text = ''.join(list(res_text)[:15])
        try:
            res_text=float(res_text)
            if res_text.is_integer():
                res_text=int(res_text)
        except:
            pass
        self.ui.result_label.setText( str(res_text) )
        
    def result_is_0(self):
        return self.get_res_text() == '0'
    
    
    def __init__(self):
        super().__init__()
        self.setupConfig()  
    
    def setupConfig(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupProperties()
        self.setupLogic()
        
    def setupProperties(self):
        self.num_buttons:List[qtw.QPushButton] = []
        for key, val in self.ui.__dict__.items():
            val.setEnabled(True)
            self.num_buttons.append(val) if is_num_button(key) else None
        self.prev_input_num = None
        self.cur_input_num=0
        self.operation = None
    
    def setupLogic(self):
        self.state=CalcStates.INPUT
        self.set_all_handlers()
        
    def set_all_handlers(self):
        self.set_num_handlers()
        self.set_operations_handlers()
        self.set_equal_handler()
        self.set_clear_handler()
        
    
    def set_num_handlers(self):
        for num_btn in self.num_buttons:    
            num_btn.clicked.connect(lambda checked, num_btn=num_btn: self.on_num_button_click(checked, num_btn) )
        
    def on_num_button_click(self, checked, num_btn:qtw.QPushButton):
        res_text = self.ui.result_label.text()
        btn_num=int(num_btn.text())
        
        if self.state == CalcStates.INPUT and not self.operation:
            if len(res_text)<15:
                res_text=f'{res_text}{btn_num}' if not self.result_is_0() else f'{btn_num}'
        elif self.state == CalcStates.OPERATION:
            self.state = CalcStates.INPUT_2
            self.cur_input_num=btn_num
            res_text=f'{btn_num}'
        elif self.state == CalcStates.INPUT_2:
            res_text += f'{btn_num}'
            self.cur_input_num = int(res_text) 
            
        self.set_res_text( res_text )
    
        
    def set_operations_handlers(self):
        self.ui.button_plus.clicked.connect(self.on_plus_button_click)
        self.ui.button_minus.clicked.connect(self.on_minus_button_click)
        self.ui.button_multiplying.clicked.connect(self.on_multiplying_button_click)
        self.ui.button_divide.clicked.connect(self.on_divide_button_click)
        
    
    def operation_handler(self, calc_operation:CalculatorOperation):
        res_text = self.get_res_text()
        if self.result_is_0():
            pass
        elif self.state == CalcStates.INPUT:
            self.prev_input_num=float(res_text)
            self.operation=calc_operation
            res_text=calc_operation.operation_char
            self.state=CalcStates.OPERATION
        self.set_res_text(res_text)
    
    def on_plus_button_click(self):
        self.operation_handler(CalcOperations.PLUS)
        
    def on_minus_button_click(self):
        self.operation_handler(CalcOperations.MINUS)
        
    def on_multiplying_button_click(self):
        self.operation_handler(CalcOperations.MULTIPLAYING)
        
    def on_divide_button_click(self):
        self.operation_handler(CalcOperations.DIVIDE)
        
        
    def set_equal_handler(self):
        self.ui.button_equal.clicked.connect(self.on_equal_button_click)
    
    def on_equal_button_click(self):
        res_text = self.get_res_text()
        
        if self.state == CalcStates.INPUT_2:
            res_text = f'{self.operation.operation_func(self.prev_input_num, self.cur_input_num)}'
            self.clear_operation_data()
            self.state=CalcStates.INPUT
        
        self.set_res_text(res_text)
        
    def set_clear_handler(self):
        self.ui.button_clear.clicked.connect(self.on_clear_button_click)
    
    def clear_operation_data(self):
        self.prev_input_num=None
        self.cur_input_num=0
        self.operation=None
    
    def on_clear_button_click(self):
        self.set_res_text('0')
        self.clear_operation_data()
        self.state=CalcStates.INPUT


class App(qtw.QApplication):
    def __init__(self):
        super().__init__(sys.argv)        


def main():
    app = App()
    window = MainWindow()
    window.show()
    app.exec() 
    

if __name__=='__main__':
    main()





