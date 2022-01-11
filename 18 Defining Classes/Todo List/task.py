class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False
        self.comments = []

    def change_name(self, new_name):
        if new_name == self.name:
            return f"Name cannot be the same."
        else:
            self.name = new_name
            return self.name

    def change_due_date(self, new_date):
        if new_date == self.due_date:
            return f"Date cannot be the same."
        else:
            self.due_date = new_date
            return self.due_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if 0 <= int(comment_number) < len(self.comments):
            self.comments[int(comment_number)] = new_comment
            return ", ".join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due date: {self.due_date}"