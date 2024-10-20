numbers = []
number = input(f"Enter a number: ")
while number != "":
    numbers.append(number)
    number = input(f"Enter a number: ")

def total_calculation(list_numbers):
    total = 0
    for i in list_numbers:
        total += int(i)
    return total
print(f'the sum of the list number is {total_calculation(numbers)}')