import tkinter as tk
from tkinter import ttk
import base64

def add_task(event=None):
    password = task_entry.get()
    decoded_password = base64.b64decode(password).decode()
    decode_num.config(text=f"Decoded code: {decoded_password}")
    
root=tk.Tk()
root.geometry("400x400")
root.title("DECODE APP")

ent_code = ttk.Label(root, text="Enter your code", font=("arial", 10, "bold"))
ent_code.pack()

frame = ttk.Frame(root, width=400, height=60)
frame.pack()

task_entry = ttk.Entry(frame, font="arial 18", width=27)
task_entry.pack()

task_entry.bind("<Return>",add_task)

decode_button = ttk.Button(root, text="Encode", command=add_task)
decode_button.pack(pady=5)

decode_num = ttk.Label(root, text="", font=("arial", 10))
decode_num.pack()


root.mainloop()
