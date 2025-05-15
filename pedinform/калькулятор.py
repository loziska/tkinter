import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x450")  # Увеличиваем высоту окна для новых кнопок
        self.root.resizable(False, False)
        
        # Переменная для хранения текущего выражения
        self.current = ""
        
        # Создаем поле ввода
        self.display = ttk.Entry(root, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Кнопки калькулятора
        buttons = [
            '(', ')', 'C', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', '⌫'  # Добавляем кнопку удаления (⌫)
        ]
        
        # Создаем и размещаем кнопки
        row = 1
        col = 0
        for button in buttons:
            if button == 'C':
                cmd = lambda x=button: self.clear()
                ttk.Button(root, text=button, command=cmd).grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
            elif button == '⌫':
                cmd = lambda x=button: self.backspace()
                ttk.Button(root, text=button, command=cmd).grid(row=5, column=3, sticky="nsew", padx=2, pady=2)
            else:
                cmd = lambda x=button: self.click(x)
                ttk.Button(root, text=button, command=cmd).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Настраиваем веса строк и столбцов для правильного растяжения
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            
        # Привязываем клавиши клавиатуры
        self.root.bind('<Key>', self.key_press)
        
    def click(self, key):
        if key == '=':
            try:
                # Проверяем баланс скобок
                if self.current.count('(') != self.current.count(')'):
                    raise ValueError("Несбалансированные скобки")
                result = eval(self.current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Ошибка")
                self.current = ""
        else:
            self.current += key
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
    
    def clear(self):
        self.current = ""
        self.display.delete(0, tk.END)
    
    def backspace(self):
        self.current = self.current[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current)
    
    def key_press(self, event):
        key = event.char
        if key in '0123456789.+-*/()':  # Добавляем скобки в список разрешенных символов
            self.click(key)
        elif key == '\r':  # Enter
            self.click('=')
        elif key == '\x08':  # Backspace
            self.backspace()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
