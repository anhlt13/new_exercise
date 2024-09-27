welcome = input("Enter the cabin class of a cruise ship: ")
if welcome == "LUX":
    print("Upper-deck cabin with a balcony")
elif welcome == "A":
    print("Above the car deck, equipped with a window")
elif welcome == "B":
    print("Windowless cabin above the car deck")
elif welcome == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")