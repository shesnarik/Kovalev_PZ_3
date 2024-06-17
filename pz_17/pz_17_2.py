import tkinter as tk
from tkinter import ttk

def submit_form():

    pass

def reset_form():
    for entry in entries:
        entry.delete(0, tk.END)
    meal_preference.set("Vegetarian")
    payment_mode.set("Cash")

root = tk.Tk()
root.title("Workshop Registration")
root.geometry("800x600")
root.configure(bg="#e0ebe4")

header = tk.Label(root, text="Workshop Registration", font=("Arial", 16), bg="#e0ebe4")
header.grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

register_note = tk.Label(root, text="Register now while seats are available!", font=("Arial", 10, "italic"), bg="#e0ebe4")
register_note.grid(row=1, column=0, columnspan=4, pady=5, sticky="w")

labels = [
    "First Name", "Last Name", "Company/Institution", "Address",
    "City", "State / Province / Region", "Country", "Email", "Phone Number"
]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=f"{label} *", anchor="w", bg="#e0ebe4").grid(row=i + 2, column=0, pady=5, padx=5, sticky="w")
    entry = tk.Entry(root, width=30)
    entry.grid(row=i + 2, column=1, pady=5, padx=5)
    entries.append(entry)

meal_preference_label = tk.Label(root, text="Meal Preference", anchor="w", bg="#e0ebe4")
meal_preference_label.grid(row=2, column=3, pady=5, padx=5, sticky="w")
meal_preference = ttk.Combobox(root, values=["Vegetarian", "Non-Vegetarian"], width=20)
meal_preference.grid(row=2, column=4, pady=5, padx=5)

payment_mode_label = tk.Label(root, text="Payment Mode", anchor="w", bg="#e0ebe4")
payment_mode_label.grid(row=3, column=3, pady=5, padx=5, sticky="w")
payment_mode = ttk.Combobox(root, values=["Cash", "Cheque", "Demand Draft"], width=20)
payment_mode.grid(row=3, column=4, pady=5, padx=5)

dd_cheque_no_label = tk.Label(root, text="DD/Cheque No.", anchor="w", bg="#e0ebe4")
dd_cheque_no_label.grid(row=4, column=3, pady=5, padx=5, sticky="w")
dd_cheque_no_entry = tk.Entry(root, width=20)
dd_cheque_no_entry.grid(row=4, column=4, pady=5, padx=5)

drawn_on_label = tk.Label(root, text="Drawn On (Bank Name)", anchor="w", bg="#e0ebe4")
drawn_on_label.grid(row=5, column=3, pady=5, padx=5, sticky="w")
drawn_on_entry = tk.Entry(root, width=20)
drawn_on_entry.grid(row=5, column=4, pady=5, padx=5)

payable_at_label = tk.Label(root, text="Payable at", anchor="w", bg="#e0ebe4")
payable_at_label.grid(row=6, column=3, pady=5, padx=5, sticky="w")
payable_at_entry = tk.Entry(root, width=20)
payable_at_entry.grid(row=6, column=4, pady=5, padx=5)

submit_button = tk.Button(root, text="Submit", command=submit_form, bg="#c6d9c1", width=10)
submit_button.grid(row=10, column=1, pady=20)

reset_button = tk.Button(root, text="Reset", command=reset_form, bg="#c6d9c1", width=10)
reset_button.grid(row=10, column=2, pady=20)

root.mainloop()