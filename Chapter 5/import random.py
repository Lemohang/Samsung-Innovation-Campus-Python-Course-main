import random

multiples_of_5 = list(range(0, 101, 5))
selected = random.sample(multiples_of_5, 3)

print(selected)