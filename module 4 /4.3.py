smallest = 0
largest = 0
number=input("Enter a number: ")

largest=float(number)
smallest=float(number)
while number!="":
    if float(number)>largest:
         largest=float(number)
    elif float(number)<smallest:
        smallest = float(number)
    number=input("Enter another number: ")
print("quit")
print("The largest number is ", largest)
print("The smallest number is ", smallest)

