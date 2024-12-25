import random

def play_game():
    # method #1
    random_result_1 = random.randint(0, 1)
    res_1 = "Tails" if random_result_1 == 0 else "Heads"
    # method #2
    random_result_2 = round(random.random(), 2)
    res_2 = "Tails" if random_result_2 < 0.5 else "Heads"
    return res_1, res_2
    # print(f'{result=}') 
