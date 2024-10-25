seasons = ("Spring","Summer","Autumn","Winter")
month = int(input(f'enter a month from 1 to 12: '))

if 2<=month<=4:
    index = seasons[0]
elif 5<=month<=7:
    index = seasons[1]
elif 8<=month<=10:
    index = seasons[2]
else:
    index = seasons[3]


print(f' {month} month is in {index}')
