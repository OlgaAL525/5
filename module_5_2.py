class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            i=1
            while i <= new_floor:
                print(i)
                i += 1


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название:{self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('Горский', 18)
h2 = House('Домик в деревне', 2)
print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))