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

window.mainloop()