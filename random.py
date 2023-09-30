import tkinter as tk
from tkinter import StringVar
from random import choice
def generate_password():
    special_chars = "!@#$%^&*- _~+-="
    digits="0123456789"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    all_chars=digits+uppercase+lowercase+special_chars
    password_length = 12 
    password = ''.join(choice(all_chars) for _ in range(password_length))
    return password
root = tk.Tk()
root.title('Password Generator')
root.geometry("300x80") 
password_var = StringVar()
def click_generate():
    password = generate_password()
    password_var.set(password)
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 16), padx=10, pady=5)
password_label.pack()
generate_button = tk.Button(root, text="Generate", command=click_generate, font=("Arial", 12))
generate_button.pack()
root.mainloop()
