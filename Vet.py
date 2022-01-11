class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if self.space <= len(Vet.animals):
            return "Not enough space"
        Vet.animals.append(animal_name)
        self.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {self.space - len(Vet.animals)} space left in clinic"
