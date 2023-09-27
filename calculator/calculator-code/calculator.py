import tkinter as tk

# Function to update the expression
def update_expression(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(value))

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to calculate and display the result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and pack the entry widget
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)
entry.grid(pady=10)

# Create buttons for numbers
for i in range(1, 10):
    button = tk.Button(root, text=str(i), command=lambda i=i: update_expression(i))
    button.grid(row=(i-1)//3+1, column=(i-1)%3)

# Create buttons for 0, Clear, and Calculate
zero_button = tk.Button(root, text="0", command=lambda: update_expression(0))
clear_button = tk.Button(root, text="C", command=clear_entry)
equal_button = tk.Button(root, text="=", command=calculate)

zero_button.grid(row=4, column=0)
clear_button.grid(row=4, column=1)
equal_button.grid(row=4, column=2)

# Create buttons for operators
operators = ["+", "-", "*", "/"]
for i, operator in enumerate(operators):
    button = tk.Button(root, text=operator, command=lambda operator=operator: update_expression(operator))
    button.grid(row=i+1, column=3)

# Start the GUI main loop
root.mainloop()
