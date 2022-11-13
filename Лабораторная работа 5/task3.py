from random import randint
def get_unique_list_numbers() -> list[int]:
    list_numbers = []
    while True:
        a = randint(-10, 10)
        if a not in list_numbers:
            list_numbers.append(a)
        if len(list_numbers) == 15:
            break
    return list_numbers



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
