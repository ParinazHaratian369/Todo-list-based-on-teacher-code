from customtkinter import *
import json

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