from customtkinter import *
import json
from tkinter import Scrollbar, Listbox

def load_tasks():
    if os.path.exists(database):
        with open(database, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(database, "w") as f:
        json.dump(tasks, f, indent=4)

def update_task_list():
    task_listbox.delete(0, END)
    for task in tasks:
        task_text = task["text"]
        if task["status"] == "important":
            task_listbox.insert(END, task_text)
            task_listbox.itemconfig(END, {'bg' : 'orange'})
        elif task["status"] == "done":
            task_listbox.insert(END, task_text)
            task_listbox.itemconfig(END, {'bg' : 'green'})
        else:
            task_listbox.insert(END, task_text)

def add_task():
    task_text = task_entry.get()
    print(type(tasks))
    tasks.append({"text":task_text, "status":"default"})
    save_tasks()
    update_task_list()
    task_entry.delete(0, END)

def reset_task():
    selected_index = task_listbox.curselection()[0]
    tasks[selected_index]["status"] = "default"
    save_tasks()
    update_task_list()

def mark_done():
    selected_index = task_listbox.curselection()[0]
    tasks[selected_index]["status"] = "done"
    save_tasks()
    update_task_list()

def highlight_task():
    selected_index = task_listbox.curselection()[0]
    tasks[selected_index]["status"] = "important"
    save_tasks()
    update_task_list()

def clear_tasks():
    global tasks
    tasks = []
    save_tasks()
    update_task_list()

def remove_task():
    selected_index = task_listbox.curselection()[0]
    del tasks[selected_index]
    save_tasks()
    update_task_list()

def edit_task():
    selected_index = task_listbox.curselection()[0]
    # print(selected_index)
    new_task = task_entry.get()
    tasks[selected_index]["text"] = new_task
    save_tasks()
    update_task_list()
    task_entry.delete(0, END)

database = "database.json"
tasks = load_tasks()

set_appearance_mode("light")
set_default_color_theme("themes/rime.json")

window = CTk()
window.title("Todo List App")
window.geometry("700x500")
window.resizable(False, False)

frame = CTkFrame(window)
frame.pack(padx=20, pady=20, fill="x")

entry_frame = CTkFrame(frame)
entry_frame.pack(pady=10, fill="x")

task_entry = CTkEntry(entry_frame, width=500)
task_entry.pack(side="left")

add_button = CTkButton(entry_frame, text="Add", command=add_task, width=100)
add_button.pack(side="right")

task_frame = CTkFrame(frame)
task_frame.pack(padx=10, pady=10, fill="both")

task_scrollbar = Scrollbar(task_frame)
task_scrollbar.pack(side="right", fill="y")

task_listbox = Listbox(task_frame, yscrollcommand=task_scrollbar.set)
task_listbox.pack(side=LEFT, fill=BOTH, expand=True)

task_scrollbar.configure(command=task_listbox.yview)

update_task_list()

btn_frame = CTkFrame(frame)
btn_frame.pack(pady=10)

edit_btn = CTkButton(btn_frame, text="Edit", command=edit_task, width=200)
edit_btn.grid(row=0, column=0, padx=5, pady=5)

remove_btn = CTkButton(btn_frame, text="Remove", command=remove_task, width=200)
remove_btn.grid(row=0, column=1, padx=5)

clear_btn = CTkButton(btn_frame, text="Clear All", command=clear_tasks, width=200)
clear_btn.grid(row=0, column=2, padx=5)

highlite_btn = CTkButton(btn_frame, text="Highlight", command=highlight_task, width=200)
highlite_btn.grid(row=1, column=0, padx=5, pady=5)

mark_done_btn = CTkButton(btn_frame, text="Mark Done", command=mark_done, width=200)
mark_done_btn.grid(row=1, column=1, padx=5)

reset_btn = CTkButton(btn_frame, text="Reset", command=reset_task, width=200)
reset_btn.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()