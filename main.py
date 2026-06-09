import os
class TaskManager():
    def __init__(self,json_path):
        if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
            with open(json_path, "w") as file:
                file.write('{"task":[]}')
        self.json_path = json_path

    def add(self, task):
        return task

def main():
    print("hello world")

if __name__ == "__main__":
    main()
        
