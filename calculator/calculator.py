import tkinter as tk
from tkinter import ttk
import math

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Calculator state
        self.current_number = ""
        self.previous_number = ""
        self.operation = ""
        self.should_reset = False
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure custom styles
        self.style.configure('Display.TLabel', 
                           background='#34495e', 
                           foreground='white', 
                           font=('Arial', 24, 'bold'))
        
        self.style.configure('Number.TButton', 
                           background='#3498db', 
                           foreground='white', 
                           font=('Arial', 14, 'bold'))
        
        self.style.configure('Operator.TButton', 
                           background='#e74c3c', 
                           foreground='white', 
                           font=('Arial', 14, 'bold'))
        
        self.style.configure('Clear.TButton', 
                           background='#95a5a6', 
                           foreground='white', 
                           font=('Arial', 14, 'bold'))
        
        self.style.configure('Equals.TButton', 
                           background='#27ae60', 
                           foreground='white', 
                           font=('Arial', 14, 'bold'))
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        display_frame = tk.Frame(main_frame, bg="#34495e", relief="flat", bd=0)
        display_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.display = ttk.Label(display_frame, 
                                textvariable=self.display_var, 
                                style='Display.TLabel',
                                anchor='e',
                                padding=(20, 20))
        self.display.pack(fill=tk.BOTH)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="#2c3e50")
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button configurations
        button_configs = [
            # Row 1: Clear, Plus/Minus, Percentage, Division
            [('C', 'Clear'), ('±', 'Number'), ('%', 'Number'), ('÷', 'Operator')],
            # Row 2: 7, 8, 9, Multiplication
            [('7', 'Number'), ('8', 'Number'), ('9', 'Number'), ('×', 'Operator')],
            # Row 3: 4, 5, 6, Subtraction
            [('4', 'Number'), ('5', 'Number'), ('6', 'Number'), ('-', 'Operator')],
            # Row 4: 1, 2, 3, Addition
            [('1', 'Number'), ('2', 'Number'), ('3', 'Number'), ('+', 'Operator')],
            # Row 5: 0, Decimal, Equals
            [('0', 'Number'), ('.', 'Number'), ('=', 'Equals')]
        ]
        
        # Create buttons
        for i, row in enumerate(button_configs):
            for j, (text, button_type) in enumerate(row):
                if text == '0':
                    # Make 0 button span 2 columns
                    btn = self.create_button(buttons_frame, text, button_type, 
                                          row=i+1, column=j, columnspan=2)
                else:
                    btn = self.create_button(buttons_frame, text, button_type, 
                                          row=i+1, column=j)
            
            # Configure grid weights
            buttons_frame.grid_columnconfigure(0, weight=1)
            buttons_frame.grid_columnconfigure(1, weight=1)
            buttons_frame.grid_columnconfigure(2, weight=1)
            buttons_frame.grid_columnconfigure(3, weight=1)
            buttons_frame.grid_rowconfigure(i+1, weight=1)
        
        # Configure grid weights for rows
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
    
    def create_button(self, parent, text, button_type, **grid_options):
        if button_type == 'Number':
            style = 'Number.TButton'
            command = lambda: self.number_click(text)
        elif button_type == 'Operator':
            style = 'Operator.TButton'
            command = lambda: self.operator_click(text)
        elif button_type == 'Clear':
            style = 'Clear.TButton'
            command = self.clear
        elif button_type == 'Equals':
            style = 'Equals.TButton'
            command = self.calculate
        
        btn = ttk.Button(parent, text=text, style=style, command=command)
        
        # Set default sticky behavior
        if 'sticky' not in grid_options:
            grid_options['sticky'] = 'nsew'
        
        btn.grid(**grid_options, padx=5, pady=5)
        return btn
    
    def number_click(self, number):
        if self.should_reset:
            self.current_number = ""
            self.should_reset = False
        
        if number == '.' and '.' in self.current_number:
            return
        
        if number == '±':
            if self.current_number and self.current_number != '0':
                if self.current_number[0] == '-':
                    self.current_number = self.current_number[1:]
                else:
                    self.current_number = '-' + self.current_number
        elif number == '%':
            if self.current_number:
                try:
                    result = float(self.current_number) / 100
                    self.current_number = str(result)
                except ValueError:
                    self.current_number = "Error"
        else:
            if self.current_number == "0" and number != '.':
                self.current_number = number
            else:
                self.current_number += number
        
        self.update_display()
    
    def operator_click(self, operator):
        if self.current_number:
            if self.previous_number and self.operation:
                self.calculate()
            
            self.previous_number = self.current_number
            self.operation = operator
            self.should_reset = True
            self.update_display()
    
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
                # Format result to remove unnecessary decimal places
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
        self.display_var.set("0")
    
    def update_display(self):
        if self.current_number:
            self.display_var.set(self.current_number)
        else:
            self.display_var.set("0")

def main():
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 