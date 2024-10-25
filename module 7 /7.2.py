names = []
name = input(f"enter a name: ")

while name != "":

    if name in names:
        print(f'existing name')
    else:
        print(f'New name')
    names.append(name)
    name = input(f'enter a name: ')

for i in names:
    print(f'hello, {i}')