import tkinter as tk
from tkinter import ttk
import random
import string
def generate_password():

    length = int(password_length_slider.get())

    include_symbols = var_symbols.get()
    include_numbers = var_numbers.get()

    characters = string.ascii_letters

    if include_symbols:
        characters += string.punctuation

    if include_numbers:
        characters += string.digits

    password = ''.join(
        random.choice(characters) for _ in range(length)
    )

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
def copy_password():
    password = entry_password.get()

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        copy_label.config(text="Password Copied Successfully!")
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x450")
window.config(bg="#f0f0f0")
window.resizable(False, False)
title_label = tk.Label(
    window,
    text="Password Generator",
    font=("Helvetica", 18, "bold"),
    bg="#f0f0f0"
)
title_label.pack(pady=20)
label_length = tk.Label(
    window,
    text="Password Length:",
    font=("Helvetica", 12),
    bg="#f0f0f0"
)
label_length.pack(pady=5)
password_length_slider = tk.Scale(
    window,
    from_=4,
    to=32,
    orient=tk.HORIZONTAL,
    length=250,
    bg="#f0f0f0",
    font=("Helvetica", 10)
)
password_length_slider.set(12)
password_length_slider.pack(pady=5)
var_symbols = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)

check_symbols = tk.Checkbutton(
    window,
    text="Include Symbols (!@#$%)",
    variable=var_symbols,
    bg="#f0f0f0",
    font=("Helvetica", 11)
)
check_symbols.pack(pady=5)

check_numbers = tk.Checkbutton(
    window,
    text="Include Numbers (123)",
    variable=var_numbers,
    bg="#f0f0f0",
    font=("Helvetica", 11)
)
check_numbers.pack(pady=5)
entry_password = tk.Entry(
    window,
    font=("Helvetica", 14),
    justify="center",
    width=25
)
entry_password.pack(pady=20)
generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password,
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20
)
generate_button.pack(pady=5)
copy_button = tk.Button(
    window,
    text="Copy Password",
    command=copy_password,
    font=("Helvetica", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=20
)
copy_button.pack(pady=5)
copy_label = tk.Label(
    window,
    text="",
    font=("Helvetica", 10),
    bg="#f0f0f0",
    fg="green"
)
copy_label.pack(pady=10)
window.mainloop()
