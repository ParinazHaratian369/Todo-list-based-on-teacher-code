from customtkinter import *
import json
from tkinter import Scrollbar, Listbox

def load_tasks():
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        tasks = {}
        with open(path, "w") as f:
            json.dump(tasks, f, indent=4) 

path = "tasks.json"
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

add_button = CTkButton(entry_frame, text="Add", width=100)
add_button.pack(side="right")

task_frame = CTkFrame(frame)
task_frame.pack(padx=10, pady=10, fill="both")

task_scrollbar = Scrollbar(task_frame)
task_scrollbar.pack(side="right", fill="y")

task_listbox = Listbox(task_frame, yscrollcommand=task_scrollbar.set)
task_listbox.pack(side=LEFT, fill=BOTH, expand=True)

window.mainloop()