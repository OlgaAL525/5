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


    def __eq__(self, other):
        if isinstance(other, House) and isinstance(self, House):
            return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        if isinstance(other, House) and isinstance(self, House):
            return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        if isinstance(other, House) and isinstance(self, House):
            return self.number_of_floors <= other.number_of_floors


    def __qt__(self, other):
        if isinstance(other, House) and isinstance(self, House):
            return self.number_of_floors > other.number_of_floors


    def __qe__(self, other):
        if isinstance(other, House) and isinstance(self, House):
            return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        if isinstance(other, House) and isinstance(self, House):
            return self.number_of_floors != other.number_of_floors


    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1+10
print(h1)

print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

