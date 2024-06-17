import tkinter as tk
from tkinter import ttk

def get_first_digit():
    number = int(entry_number.get())
    first_digit = number // 100
    label_result.config(text=f"Первая цифра числа: {first_digit}")


root = tk.Tk()
root.title("Вывод первой цифры трехзначного числа")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, padx=10, pady=10)

label_number = ttk.Label(frame, text="Введите трехзначное число:")
label_number.grid(row=0, column=0, padx=5, pady=5)

entry_number = ttk.Entry(frame)
entry_number.grid(row=0, column=1, padx=5, pady=5)

button_calculate = ttk.Button(frame, text="Вычислить", command=get_first_digit)
button_calculate.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

label_result = ttk.Label(frame, text="")
label_result.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
