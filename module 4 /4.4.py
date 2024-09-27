import random
i = 9
number=int(input("Enter a number: "))
random=random.randint(1,10)

while 1<=i<=10:
    if int(number)>random:
        print("it's too high")
    elif int(number)<random:
        print("it's too low")
    else:
        print("correct")
        break
    number=input("enter another number: ")
