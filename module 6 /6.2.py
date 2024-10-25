import random
num_sides = int(input(f"Enter the number of sides on the dice: "))
max_number = int(input("Enter the maximum number to roll: "))
def roll_dice(num_sides):
    return random.randint(1,num_sides)
while True:
    result = roll_dice(num_sides)
    print(f"You rolled:", result)
    if result == max_number:
        print(f"Congratulations! You rolled the maximum number. ")
        break



