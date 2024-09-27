import random

def random_dice():
    dice =random.randint(1,6)
    return dice
while True:
    result = random_dice()
    print(f'the number you dice is {result}')
    if result==6:
        break
