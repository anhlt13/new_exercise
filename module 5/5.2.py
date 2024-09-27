print("enter at least 5 numbers")
listnumber = []
number = input("type a number: ")
while number != "":
    listnumber.append(int(number))
    number = input("type a number: ")
listnumber.sort(reverse=True)

print(f"the 5 greatest numbers are: ")
for i in range(5):
    print(listnumber[i], end=" ")




