class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        if args:
            cls.houses_history.append(args[0])
        return instance

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус')

print(House.houses_history)

h2 = House('ЖК Акация')

print(House.houses_history)

h3 = House('ЖК Матрёшки')

print(House.houses_history)



# Удаление объектов

del h2

del h3



print(House.houses_history)