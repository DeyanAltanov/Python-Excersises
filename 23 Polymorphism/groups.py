class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        group = []
        for member in self.people:
            group.append(f"{member.name} {member.surname}")
        return f"Group {self.name} with members {', '.join(member for member in group)}"

    def __add__(self, other):
        name = f"{self.name} {other.name}"
        people = []
        for member in self.people:
            people.append(member)
        for member in other.people:
            people.append(member)
        return Group(name, people)

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}"