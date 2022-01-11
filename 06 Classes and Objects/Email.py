class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
b = []
email = input()
a = email.split()
b.append(email)

while not a[0] == 'Stop':
    message = Email(a[0], a[1], a[2])
    emails.append(Email.get_info(message))

    email = input()
    a = email.split()
    b.append(email)

indexes = [int(index) for index in input().split(", ")]

for index in indexes:
    email = b[index].split()
    message = Email(email[0], email[1], email[2])
    Email.send(message)
    emails[index] = Email.get_info(message)

for email in emails:
    print(email)