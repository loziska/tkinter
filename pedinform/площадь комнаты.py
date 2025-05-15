import tkinter as tk
from tkinter import messagebox, filedialog
import math
import pickle

class RoomCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор комнаты")
        
        # Фиксируем размер окна
        self.root.resizable(False, False)
        
        # Создаем и размещаем элементы интерфейса
        self.length_label = tk.Label(root, text="Длина комнаты (м):")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.length_var = tk.StringVar()
        self.length_entry = tk.Entry(root, textvariable=self.length_var)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.width_label = tk.Label(root, text="Ширина комнаты (м):")
        self.width_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.width_var = tk.StringVar()
        self.width_entry = tk.Entry(root, textvariable=self.width_var)
        self.width_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.height_label = tk.Label(root, text="Высота комнаты (м):")
        self.height_label.grid(row=2, column=0, padx=5, pady=5)
        
        self.height_var = tk.StringVar()
        self.height_entry = tk.Entry(root, textvariable=self.height_var)
        self.height_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Добавляем разделитель
        separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
        separator.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=10)
        
        # Поля для размеров рулона
        self.roll_width_label = tk.Label(root, text="Ширина рулона (м):")
        self.roll_width_label.grid(row=4, column=0, padx=5, pady=5)
        
        self.roll_width_var = tk.StringVar(value="0.53")
        self.roll_width_entry = tk.Entry(root, textvariable=self.roll_width_var)
        self.roll_width_entry.grid(row=4, column=1, padx=5, pady=5)
        
        self.roll_length_label = tk.Label(root, text="Длина рулона (м):")
        self.roll_length_label.grid(row=5, column=0, padx=5, pady=5)
        
        self.roll_length_var = tk.StringVar(value="10.05")
        self.roll_length_entry = tk.Entry(root, textvariable=self.roll_length_var)
        self.roll_length_entry.grid(row=5, column=1, padx=5, pady=5)
        
        # Добавляем разделитель
        separator2 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
        separator2.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=10)
        
        # Добавляем кнопки сохранения и загрузки
        button_frame = tk.Frame(root)
        button_frame.grid(row=7, column=0, columnspan=2, pady=10)
        
        self.save_button = tk.Button(button_frame, text="Сохранить", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        self.load_button = tk.Button(button_frame, text="Загрузить", command=self.load_data)
        self.load_button.pack(side=tk.LEFT, padx=5)
        
        # Добавляем разделитель
        separator3 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
        separator3.grid(row=8, column=0, columnspan=2, sticky="ew", padx=5, pady=10)
        
        self.floor_label = tk.Label(root, text="Площадь пола:")
        self.floor_label.grid(row=9, column=0, padx=5, pady=5)
        
        self.floor_var = tk.StringVar(value="?")
        self.floor_result = tk.Label(root, textvariable=self.floor_var)
        self.floor_result.grid(row=9, column=1, padx=5, pady=5)
        
        self.walls_label = tk.Label(root, text="Площадь стен:")
        self.walls_label.grid(row=10, column=0, padx=5, pady=5)
        
        self.walls_var = tk.StringVar(value="?")
        self.walls_result = tk.Label(root, textvariable=self.walls_var)
        self.walls_result.grid(row=10, column=1, padx=5, pady=5)
        
        self.rolls_label = tk.Label(root, text="Количество рулонов:")
        self.rolls_label.grid(row=11, column=0, padx=5, pady=5)
        
        self.rolls_var = tk.StringVar(value="?")
        self.rolls_result = tk.Label(root, textvariable=self.rolls_var)
        self.rolls_result.grid(row=11, column=1, padx=5, pady=5)
        
        # Привязываем функции к изменению значений
        self.length_var.trace_add("write", self.calculate_all)
        self.width_var.trace_add("write", self.calculate_all)
        self.height_var.trace_add("write", self.calculate_all)
        self.roll_width_var.trace_add("write", self.calculate_all)
        self.roll_length_var.trace_add("write", self.calculate_all)
        
        # Привязываем функцию к закрытию окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Устанавливаем фиксированный размер окна
        self.root.geometry("300x450")

    def get_data_dict(self):
        """Получение словаря с текущими данными"""
        return {
            'length': self.length_var.get(),
            'width': self.width_var.get(),
            'height': self.height_var.get(),
            'roll_width': self.roll_width_var.get(),
            'roll_length': self.roll_length_var.get()
        }

    def set_data_from_dict(self, data):
        """Установка данных из словаря"""
        self.length_var.set(data.get('length', ''))
        self.width_var.set(data.get('width', ''))
        self.height_var.set(data.get('height', ''))
        self.roll_width_var.set(data.get('roll_width', '0.53'))
        self.roll_length_var.set(data.get('roll_length', '10.05'))

    def save_data(self):
        """Сохранение данных в файл"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".dat",
                filetypes=[("Data files", "*.dat"), ("All files", "*.*")],
                title="Сохранить данные"
            )
            if filename:
                data = self.get_data_dict()
                with open(filename, 'wb') as f:
                    pickle.dump(data, f)
                messagebox.showinfo("Успех", "Данные успешно сохранены")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {str(e)}")

    def load_data(self):
        """Загрузка данных из файла"""
        try:
            filename = filedialog.askopenfilename(
                defaultextension=".dat",
                filetypes=[("Data files", "*.dat"), ("All files", "*.*")],
                title="Загрузить данные"
            )
            if filename:
                with open(filename, 'rb') as f:
                    data = pickle.load(f)
                self.set_data_from_dict(data)
                self.calculate_all()  # Пересчитываем все значения
                messagebox.showinfo("Успех", "Данные успешно загружены")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {str(e)}")

    def calculate_all(self, *args):
        try:
            # Получаем размеры комнаты
            length = float(self.length_var.get())
            width = float(self.width_var.get())
            height = float(self.height_var.get())
            
            # Получаем размеры рулона
            roll_width = float(self.roll_width_var.get())
            roll_length = float(self.roll_length_var.get())
            
            if length <= 0 or width <= 0 or height <= 0 or roll_width <= 0 or roll_length <= 0:
                self.floor_var.set("?")
                self.walls_var.set("?")
                self.rolls_var.set("?")
                return
            
            # Расчет площади пола
            floor_area = length * width
            self.floor_var.set(f"{floor_area:.2f} м²")
            
            # Расчет площади стен (периметр * высота)
            walls_area = 2 * (length + width) * height
            self.walls_var.set(f"{walls_area:.2f} м²")
            
            # Расчет количества рулонов
            roll_area = roll_width * roll_length
            rolls_needed = math.ceil(walls_area / roll_area)
            self.rolls_var.set(str(rolls_needed))
            
        except ValueError:
            self.floor_var.set("?")
            self.walls_var.set("?")
            self.rolls_var.set("?")

    def on_closing(self):
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RoomCalculator(root)
    root.mainloop()
