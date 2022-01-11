class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fish = []

    def add_animal(self, species, animal):
        if species == 'mammal':
            self.mammals.append(animal)
        elif species == 'bird':
            self.birds.append(animal)
        elif species == 'fish':
            self.fish.append(animal)

    def get_info(self, type):
        if type == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif type == 'bird':
            return f"Birds in {self.name}: {', '.join(self.birds)}"
        elif type == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fish)}"


zoo_name = input()
zoo = Zoo(zoo_name)
animals = int(input())

for a in range(0, animals):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
print(f"Total animals: {animals}")