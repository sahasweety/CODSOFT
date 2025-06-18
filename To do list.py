'''def task():
    tasks = []  # Initialize an empty list to store tasks
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")
    
    while True:
        try:
            operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
            if operation == 1:
                add = input("Enter task you want to add = ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")
            elif operation == 2:
                updated_val = input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    up = input("Enter new task = ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Updated task '{updated_val}' to '{up}'.")
                else:
                    print("Task not found.")
            elif operation == 3:
                del_val = input("Which task you want to delete = ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task '{del_val}' has been deleted.")
                else:
                    print("Task not found.")
            elif operation == 4:
                print(f"Total tasks = {tasks}")
            elif operation == 5:
                print("Closing the program....")
                break
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

task()'''
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get().strip()
        if new_task:
            tasks[selected] = new_task
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter the updated task.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Entry Frame
entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(pady=20)

entry = tk.Entry(entry_frame, width=35, font=("Arial", 12))
entry.grid(row=0, column=0, padx=10)

# Button Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

update_btn = tk.Button(button_frame, text="Update Selected Task", width=20, command=update_task)
update_btn.pack(pady=5)

delete_btn = tk.Button(button_frame, text="Delete Selected Task", width=20, command=delete_task)
delete_btn.pack(pady=5)

# Listbox
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

listbox = tk.Listbox(listbox_frame, width=45, height=10, font=("Arial", 11), selectbackground="#a6a6a6")
listbox.pack()

# Start the app
root.mainloop()
