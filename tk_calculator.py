import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except:
        messagebox.showerror("Error", "Enter valid numbers!")


tk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="Add (+)", width=12, command=lambda: calculate("add")).pack(pady=3)
tk.Button(root, text="Subtract (-)", width=12, command=lambda: calculate("sub")).pack(pady=3)
tk.Button(root, text="Multiply (×)", width=12, command=lambda: calculate("mul")).pack(pady=3)
tk.Button(root, text="Divide (÷)", width=12, command=lambda: calculate("div")).pack(pady=3)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()