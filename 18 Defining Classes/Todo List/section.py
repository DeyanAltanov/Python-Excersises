class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return f"Task Name: {task.name} - Due Date: {task.due_date} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        filtered = []
        for task in self.tasks:
            if task.name == task_name:
                filtered.append(task.name)
        if filtered:
            task.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        for task in self.tasks:
            if task.completed is True:
                self.tasks.remove(task)
                cleared_tasks += 1
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += f"{task.name} - Due Date: {task.due_date}\n"
        return result