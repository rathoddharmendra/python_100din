import random

def generate_random_numbers() -> int:
    return random.randint(0, 255)

def generate_random_rgb_color() -> tuple:
    return (generate_random_numbers(),generate_random_numbers(),generate_random_numbers())

# Generate 10 random RGB colors
for _ in range(10):
    print(generate_random_rgb_color())
