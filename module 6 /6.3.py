def convert(number):
    litre = float(gallons) * 3.78
    return litre

gallons = float(input(f'enter a number you would like to convert from gallons to litres: '))
while gallons > 0:
    print(f'the volume in liters is: {convert(gallons)}')
    gallons = float(input(f'enter a number you would like to convert from gallons to litres: '))



