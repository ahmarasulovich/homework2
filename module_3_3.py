# Задание №1
def print_params(a=1, b="строка", c=True):
    print(a, b, c)

print_params(b=25, c=[1, 2, 3])
print_params(a=24, b=25, c=[1, 2, 3])

# Задание №2
values_list = "str", [2, 1, 2], True

values_dict = {'a': 1, 'b': 2, 'c': 3}

print_params(*values_list)

print_params(**values_dict)

# Задание №3
values_list_2 = ("dict", 12)
print(*values_list_2, 42)
