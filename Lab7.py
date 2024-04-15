import tkinter as tk
from tkinter import ttk
from rx import from_rx
from rx.operators import map, filter

class ReactiveFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reactive Form")

        self.label = ttk.Label(root, text="Enter an Integer:")
        self.label.pack()

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.entry_var)
        self.entry.pack()

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack()

        # Создаем Observable из переменной StringVar
        observable = from_rx(self.entry_var.trace_add('write', self.validate_input))

        # Применяем операторы RxPy для фильтрации и маппинга
        observable.pipe(
            map(lambda value: int(value) if value.strip().isdigit() else None),
            filter(lambda value: value is not None)
        ).subscribe(
            on_next=self.handle_valid_input,
            on_error=self.handle_invalid_input
        )

    def validate_input(self, *args):
        # Пустая строка считается валидным вводом
        if self.entry_var.get().strip() == "":
            self.result_label.config(text="")
            return True
        # Проверяем, является ли введенное значение целым числом
        try:
            int(self.entry_var.get())
            self.result_label.config(text="")
            return True
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter an integer.", foreground="red")
            return False

    def handle_valid_input(self, value):
        self.result_label.config(text=f"You entered: {value}", foreground="green")

    def handle_invalid_input(self, error):
        print("Error:", error)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReactiveFormApp(root)
    root.mainloop()
