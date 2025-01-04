import random

def mutate(a_list):
    b_list = []
    new_item = 0

    for item in a_list:
        new_item = item * 3
        new_item += random.randint(1,5)
        b_list.append(new_item)
    print(b_list)

mutate([1, 4, 7, 3, 8, 11])