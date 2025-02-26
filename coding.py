

import os

is_running = True
file_path = "notes.txt"
while is_running:
        
    def new_task():
        task = input("What is my to do task? / q to Quit :").lower()
        if task == "q".lower():
            is_running = False
            print(task)

    def write_to_file():
        with open(file=file_path, mode="w") as file:
            file.write(task)
            print(f"{task} has been added to {file}")

    def read_file():
        with open(file=file_path, mode="r") as file:
            pass

    new_task()
    next_action = input("what to do next?")
    #if next_action == 
