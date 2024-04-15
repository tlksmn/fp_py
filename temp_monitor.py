from rx import Observable
from rx.subject import Subject
from rx.operators import scan
import tkinter as tk


root = tk.Tk()
root.title("Температурный Монитор")

temperature_subject = Subject()
temperature_subject.on_next(0)

def increase_temperature():
    temperature_subject.on_next(1)

def decrease_temperature():
    temperature_subject.on_next(-1)

def update_temperature(value):
    temperature_label.config(text=str(value))
    if value >= 35:
        temperature_label.config(foreground="red")
        show_warning("Внимание! Высокая температура!")
    elif value <= 0:
        temperature_label.config(foreground="blue")  
        show_warning("Внимание! Низкая температура!")
    else:
        temperature_label.config(foreground="black")

def show_warning(message):
    warning_window = tk.Toplevel(root)
    warning_window.title("Предупреждение")
    warning_label = tk.Label(warning_window, text=message, font=("Helvetica", 16), fg="red")
    warning_label.pack(padx=20, pady=20)

frame = tk.Frame(root, bg="white")
frame.pack(expand=True, fill=tk.BOTH)

increase_button = tk.Button(frame, text="Увеличить", width=20, height=3, command=increase_temperature)
increase_button.pack(side=tk.LEFT, padx=10, pady=10)

decrease_button = tk.Button(frame, text="Уменьшить", width=20, height=3, command=decrease_temperature)
decrease_button.pack(side=tk.LEFT, padx=10, pady=10)

temperature_label_text = tk.Label(frame, text="Температура:", font=("Helvetica", 18))
temperature_label_text.pack(side=tk.LEFT, padx=(10,0), pady=20)

temperature_label = tk.Label(frame, text="0", font=("Helvetica", 24))
temperature_label.pack(pady=20)

temperature_stream = temperature_subject.pipe(
    scan(lambda acc, curr: max(0, acc + curr), 0)  # Температура не может быть меньше 0
)

temperature_stream.subscribe(update_temperature)

root.mainloop()
