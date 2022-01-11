class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget - price <= 0 and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needs = 0
        for animal in self.animals:
            needs += animal.get_needs()
        if needs <= self.__budget:
            self.__budget -= needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = []
        for lion in self.animals:
            if lion.__class__.__name__ == 'Lion':
                lions.append(lion)
        if len(lions) > 0:
            result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"
        tigers = []
        for tiger in self.animals:
            if tiger.__class__.__name__ == 'Tiger':
                tigers.append(tiger)
        if len(tigers) > 0:
            result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"
        cheetahs = []
        for cheetah in self.animals:
            if cheetah.__class__.__name__ == 'Cheetah':
                cheetahs.append(cheetah)
        if len(cheetahs) > 0:
            result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"
        result = result.rstrip('\n')
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = []
        for keeper in self.workers:
            if keeper.__class__.__name__ == 'Keeper':
                keepers.append(keeper)
        if len(keepers) > 0:
            result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"
        caretakers = []
        for caretaker in self.workers:
            if caretaker.__class__.__name__ == 'Caretaker':
                caretakers.append(caretaker)
        if len(caretakers) > 0:
            result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"
        vets = []
        for vet in self.workers:
            if vet.__class__.__name__ == 'Vet':
                vets.append(vet)
        if len(vets) > 0:
            result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"
        result = result.rstrip('\n')
        return result