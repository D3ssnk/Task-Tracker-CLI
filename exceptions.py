# when a task ID is not in task.json file
class TaskNotFound(Exception):
    def __init__(self, msg = "This task does not exist"):
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self):
        return self.msg