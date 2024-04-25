import random

dict_size = random.randint(5, 10)

random_dict = {f"key_{i}": random.randint(1, 100) for i in range(dict_size)}

print(random_dict)
