class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget:
            if len(self.animals) < self.__animal_capacity:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough space for animal"
        return "Not enough budget"

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
        workers_budget = 0
        for worker in self.workers:
            workers_budget += worker.salary

        if self.__budget >= workers_budget:
            self.__budget -= workers_budget
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_budget = 0
        for animal in self.animals:
            animal_budget += animal.money_for_care

        if self.__budget >= animal_budget:
            self.__budget -= animal_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        def add_animal(some_list):
            for animal in some_list:
                ll.append(animal)

        animal_count = len(self.animals)
        lions = []
        tigers = []
        cheetahs = []
        ll = [f'You have {animal_count} animals']

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            else:
                cheetahs.append(animal)

        ll.append(f'----- {len(lions)} Lions:')
        add_animal(lions)

        ll.append(f'----- {len(tigers)} Tigers:')
        add_animal(tigers)

        ll.append(f'----- {len(cheetahs)} Cheetahs:')
        add_animal(cheetahs)

        return '\n'.join(str(x) for x in ll)

    def workers_status(self):
        def add_workers(some_list):
            for worker in some_list:
                ll.append(worker)

        workers_count = len(self.workers)
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            else:
                vets.append(worker)

        ll = [f'You have {workers_count} workers', f'----- {len(keepers)} Keepers:']

        add_workers(keepers)

        ll.append(f'----- {len(caretakers)} Caretakers:')
        add_workers(caretakers)

        ll.append(f'----- {len(vets)} Vets:')
        add_workers(vets)

        return '\n'.join(str(x) for x in ll)
