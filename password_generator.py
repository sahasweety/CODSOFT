'''import string
import random
def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = int(input("Enter the password length\n"))
    
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    

    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)

gen() '''

# Tkinker based GUI
import tkinter as tk
from tkinter import messagebox
import string
import random

# Password generation logic
def generate_password():
    try:
        passlen = int(length_entry.get())
        if passlen <= 0:
            raise ValueError("Length must be greater than 0")

        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = string.digits
        s4 = string.punctuation

        s = list(s1 + s2 + s3 + s4)
        random.shuffle(s)
        password = "".join(s[:passlen])
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for password length.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Heading
tk.Label(root, text="Random Password Generator", font=("Helvetica", 14, "bold")).pack(pady=10)

# Length input
tk.Label(root, text="Enter Password Length:").pack()
length_entry = tk.Entry(root, width=10, justify='center')
length_entry.pack(pady=5)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white").pack(pady=10)

# Output field
password_output = tk.Entry(root, width=40, justify='center', font=("Courier", 12))
password_output.pack(pady=5)

root.mainloop()