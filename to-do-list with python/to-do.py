import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")
root.configure(bg="plum")

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Select Task", "Please select a task to remove.")


def delete_all():
    listbox.delete(0, tk.END)


label_title = tk.Label(root, text="TO-DO-LIST", font=("Arial", 18, "bold"), bg="yellow", fg="red")
label_title.pack(pady=10)

frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

label_task = tk.Label(frame, text="Enter the Task Title:", font=("Arial", 12), bg="lightblue")
label_task.grid(row=0, column=0)

entry = tk.Entry(frame, width=25, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10)


btn_add = tk.Button(frame, text="Add", font=("Arial", 12), bg="orange", command=add_task)
btn_add.grid(row=1, column=0, pady=10)


btn_remove = tk.Button(frame, text="Remove", font=("Arial", 12), bg="orange", command=remove_task)
btn_remove.grid(row=1, column=1, pady=10)


btn_delete_all = tk.Button(frame, text="Delete All", font=("Arial", 12), bg="orange", command=delete_all)
btn_delete_all.grid(row=1, column=2, pady=10, padx=10)


listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)


root.mainloop()
