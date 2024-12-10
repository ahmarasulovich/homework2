#Что нужно сумммировть: dict, list, tuple, set, integer, strint
def podshot(data):
    summa= 0
    if isinstance(data, (list, tuple, set)):
        for i in data:
            summa+= podshot(i)
    elif isinstance(data, dict):
        for key, values in data.items():
            summa+= podshot(key)
            summa+= podshot(values)
    elif isinstance(data, int):
        summa+= data
    elif isinstance(data, str):
        summa+= len(data)
    return summa

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

a = podshot(data_structure)
print(a)
