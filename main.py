import random 

p1_a = random.randint(1, 6)
p1_b = random.randint(1, 6)

p2_a = random.randint(1, 6)
p2_b = random.randint(1, 6)

p1_sum = p1_a + p1_b
p2_sum = p2_a + p2_b

if p1_sum > p2_sum:
    print("Переміг грпвець 1")

elif p2_sum > p1_sum:
    print("Переміг грпвець 2")

else:
    print("НІчия")