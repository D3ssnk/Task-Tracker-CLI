import os
import json
import sys
from exceptions import *
class TaskManager():
    def __init__(self,json_file = "tasks.json"):
        if not os.path.exists(json_file) or os.path.getsize(json_file) == 0:
            with open(json_file, "w") as file:
                file.write('[]')
        self.json_file = json_file
    
    def get_file(self):
        with open(self.json_file, "r") as file:
            json_data = json.load(file)
        return json_data
    
    def check_task_exists(self, json_data, id):
        if json_data == [] or id > len(json_data):
            raise TaskNotFound()

    def add(self, description):
        with open(self.json_file, "r+") as file:
            json_data = json.load(file)
            task_id = len(json_data) + 1
            task = {"id": task_id, "description": description, "status": "todo"}
            
            json_data.append(task) # appends the task to the json list
            file.seek(0) # sets the cursor to the start so you can rewrite the entire file 
            json.dump(json_data,file) # writes the data back into the file 
    
    def delete(self, id):
        json_data = self.get_file()
        
        self.check_task_exists(json_data, id)
            
        task_index = id - 1 
        del json_data[task_index]
        for n in range(task_index,len(json_data),1):
            json_data[n]['id'] -= 1
        
        with open(self.json_file, "w") as file:
            json.dump(json_data, file)

    def update(self, id, description):
        json_data = self.get_file()
        
        self.check_task_exists(json_data, id)
        
        task_index = id - 1 
        json_data[task_index]["description"] = description

        with open(self.json_file, "w") as file:
            json.dump(json_data, file)
    
    def mark(self, id, status):
        json_data = self.get_file()

        self.check_task_exists(json_data, id)

        task_index = id - 1 
        json_data[task_index]["status"] = status

        with open(self.json_file, "w") as file:
            json.dump(json_data, file)

    def list_tasks(self, status = None):
        json_data = self.get_file()
        if len(json_data) == 0:
            return "There are no tasks!"

        if status:
            json_data = [n for n in json_data if n["status"] == status]
            if len(json_data) == 0:
                return "There are no tasks with status: " + status + "!"
        
        list_string = ""
        for task in json_data:
            task_string = f"id: {task['id']}\ndescription: {task['description']}\nstatus: {task['status']}\n\n"
            list_string += task_string
        
        return list_string.strip()

def print_tasks_helper(task_manager):
    print("\n=========Tasks=========\n")
    print(task_manager.list_tasks())

def main():
    instructions = """
    Welcome to the task tracker!
    These are the instructions:
    add: to add a task, type add followed by the task description
    update: to update a task, type update followed by the task's id, followed by the new task description
    delete: to delete a task, type delete followed by the task's id
    mark-todo: to mark a task as todo, type mark-todo followed by the task's id
    mark-in-progress: to mark a task as in-progress, type mark-in-progress followed by the task's id 
    mark-don: to mark a task as done, type mark-done followed by the task's id
    list: to list tasks, type list (you can also include either todo, in-progress, or done after to list those specific tasks) 
    exit: to exit, type exit
    help: to get the instructions again, type help
"""
    print(instructions)
    task_manager = TaskManager()
    while True:
        user_input = input("> ").strip()
        args = user_input.split(" ")

        if len(args) == 0:
            continue
    
        args[0] = args[0].lower()

        if len(args) >= 2 and args[0] == "add":
            task_description = " ".join(args[1:]).strip()
            task_manager.add(task_description)
            print(f"\ntask has been added")
            print_tasks_helper(task_manager)

        elif len(args) >= 3 and args[0] == "update" and args[1].isdigit():
            try:
                task_id = int(args[1])
                task_description = " ".join(args[2:]).strip()
                task_manager.update(task_id, task_description)
                print(f"\ntask id: {task_id} has been updated")
                print_tasks_helper(task_manager)

            except TaskNotFound as e:
                print(e)
        
        elif len(args) == 2 and args[0] == "delete" and args[1].isdigit():
            try:
                task_id = int(args[1])
                task_manager.delete(task_id)
                print(f"\ntask id: {task_id} has been deleted")
                print_tasks_helper(task_manager)

            except TaskNotFound as e:
                print(e)
        
        elif len(args) == 2 and args[0] == "mark-todo" and args[1].isdigit():
            try:
                task_id = int(args[1])
                task_manager.mark(task_id, "todo")
                print(f"task id: {task_id} has been marked as todo")
                print_tasks_helper(task_manager)

            except TaskNotFound as e:
                print(e)

        elif len(args) == 2 and args[0] == "mark-in-progress" and args[1].isdigit():
            try:
                task_id = int(args[1])
                task_manager.mark(task_id, "in-progress")
                print(f"task id: {task_id} has been marked as in-progress")
                print_tasks_helper(task_manager)

            except TaskNotFound as e:
                print(e)
        
        elif len(args) == 2 and args[0] == "mark-done" and args[1].isdigit():
            try:
                task_id = int(args[1])
                task_manager.mark(task_id, "done")
                print(f"task id: {task_id} has been marked as done")
                print_tasks_helper(task_manager)
            except TaskNotFound as e:
                print(e)
        
        elif (len(args) == 1 or len(args) == 2)and args[0] == "list":
            print("=========Tasks=========\n")
            if len(args) == 1:
                print(task_manager.list_tasks())
                continue
            
            task_status = args[1]
            if task_status in ["todo", "in-progress", "done"]:
                print(task_manager.list_tasks(task_status))
            else:
                print("invalid command or format, please try again")
            
        elif args[0] == "exit":
            sys.exit()
        
        elif args[0] == "help":
            print(instructions)
        
        else: 
            print("invalid command or format, please try again")


if __name__ == "__main__":
    main()
    