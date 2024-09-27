import random
user = int(input("how many dice to roll? "))
dicesum = 0
for i in range(1,user+1):
    dice = random.randint(1,6)
    dicesum= dicesum + dice
    print(f" try {i} is {dice}")
print(f'the sum of all numbers is: {dicesum}')