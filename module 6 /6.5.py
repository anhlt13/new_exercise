
def second_list(number):
    even_numbers=[]
    for i in number:
        if i%2==0:
            even_numbers.append(i)
    return even_numbers
original_list = [1,2,3,4,5,6,7,8,9,10]
new_list = second_list(original_list)
print(f"original list: {original_list}")
print(f"second list without odd numbers: {new_list}")