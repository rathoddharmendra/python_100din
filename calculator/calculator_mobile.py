from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Set window size for desktop testing
Window.size = (400, 600)

# Kivy UI definition
Builder.load_string('''
<CalculatorWidget>:
    orientation: 'vertical'
    padding: 20
    spacing: 10
    canvas.before:
        Color:
            rgba: 0.17, 0.24, 0.31, 1  # #2c3e50
        Rectangle:
            pos: self.pos
            size: self.size
    
    # Display
    Label:
        id: display
        text: '0'
        size_hint_y: 0.3
        canvas.before:
            Color:
                rgba: 0.20, 0.29, 0.37, 1  # #34495e
            Rectangle:
                pos: self.pos
                size: self.size
        color: 1, 1, 1, 1  # White text
        font_size: '32sp'
        bold: True
        text_size: self.size
        halign: 'right'
        valign: 'middle'
        padding: 20, 0
    
    # Buttons grid
    GridLayout:
        id: buttons_grid
        cols: 4
        rows: 5
        spacing: 5
        size_hint_y: 0.7
        
        # Row 1: Clear, Plus/Minus, Percentage, Division
        Button:
            text: 'C'
            background_color: 0.58, 0.65, 0.65, 1  # #95a5a6
            on_press: root.clear()
        Button:
            text: '±'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.toggle_sign()
        Button:
            text: '%'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.percentage()
        Button:
            text: '÷'
            background_color: 0.91, 0.30, 0.24, 1  # #e74c3c
            on_press: root.set_operation('÷')
        
        # Row 2: 7, 8, 9, Multiplication
        Button:
            text: '7'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('7')
        Button:
            text: '8'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('8')
        Button:
            text: '9'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('9')
        Button:
            text: '×'
            background_color: 0.91, 0.30, 0.24, 1  # #e74c3c
            on_press: root.set_operation('×')
        
        # Row 3: 4, 5, 6, Subtraction
        Button:
            text: '4'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('4')
        Button:
            text: '5'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('5')
        Button:
            text: '6'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('6')
        Button:
            text: '-'
            background_color: 0.91, 0.30, 0.24, 1  # #e74c3c
            on_press: root.set_operation('-')
        
        # Row 4: 1, 2, 3, Addition
        Button:
            text: '1'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('1')
        Button:
            text: '2'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('2')
        Button:
            text: '3'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('3')
        Button:
            text: '+'
            background_color: 0.91, 0.30, 0.24, 1  # #e74c3c
            on_press: root.set_operation('+')
        
        # Row 5: 0, Decimal, Equals
        Button:
            text: '0'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_number('0')
            size_hint_x: 0.5
        Button:
            text: '.'
            background_color: 0.20, 0.56, 0.84, 1  # #3498db
            on_press: root.add_decimal()
        Button:
            text: '='
            background_color: 0.15, 0.68, 0.38, 1  # #27ae60
            on_press: root.calculate()
            size_hint_x: 0.5
''')

class CalculatorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_number = ""
        self.previous_number = ""
        self.operation = ""
        self.should_reset = False
        
    def add_number(self, number):
        if self.should_reset:
            self.current_number = ""
            self.should_reset = False
        
        if self.current_number == "0":
            self.current_number = number
        else:
            self.current_number += number
        
        self.update_display()
    
    def add_decimal(self):
        if self.should_reset:
            self.current_number = ""
            self.should_reset = False
        
        if '.' not in self.current_number:
            if not self.current_number:
                self.current_number = "0"
            self.current_number += "."
            self.update_display()
    
    def toggle_sign(self):
        if self.current_number and self.current_number != "0":
            if self.current_number[0] == '-':
                self.current_number = self.current_number[1:]
            else:
                self.current_number = '-' + self.current_number
            self.update_display()
    
    def percentage(self):
        if self.current_number:
            try:
                result = float(self.current_number) / 100
                self.current_number = str(result)
                self.update_display()
            except ValueError:
                self.current_number = "Error"
                self.update_display()
    
    def set_operation(self, operation):
        if self.current_number:
            if self.previous_number and self.operation:
                self.calculate()
            
            self.previous_number = self.current_number
            self.operation = operation
            self.should_reset = True
    
    def calculate(self):
        if not self.current_number or not self.previous_number or not self.operation:
            return
        
        try:
            prev = float(self.previous_number)
            current = float(self.current_number)
            
            if self.operation == '+':
                result = prev + current
            elif self.operation == '-':
                result = prev - current
            elif self.operation == '×':
                result = prev * current
            elif self.operation == '÷':
                if current == 0:
                    result = "Error"
                else:
                    result = prev / current
            
            if result == "Error":
                self.current_number = "Error"
            else:
                # Format result
                if result == int(result):
                    self.current_number = str(int(result))
                else:
                    self.current_number = str(round(result, 10)).rstrip('0').rstrip('.')
            
            self.previous_number = ""
            self.operation = ""
            self.should_reset = True
            self.update_display()
            
        except ValueError:
            self.current_number = "Error"
            self.update_display()
    
    def clear(self):
        self.current_number = ""
        self.previous_number = ""
        self.operation = ""
        self.should_reset = False
        self.ids.display.text = "0"
    
    def update_display(self):
        if self.current_number:
            self.ids.display.text = self.current_number
        else:
            self.ids.display.text = "0"

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == '__main__':
    CalculatorApp().run() 