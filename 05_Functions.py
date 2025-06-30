def function_1(numbers):
    for number in numbers:
        if number%5 !=0:
            continue
        print(number, end=' ')
    print("")

numbers = [4,5,6,7,8,9,10]

function_1(numbers)

print("")

def get_min(numbers):
    m=numbers[0]
    for n in numbers:
        if n<m:
            m=n
    return m

my_min = get_min(numbers)    
print(my_min)
            
print("")

my_value=8

def first_less_than(numbers, my_value):
    for n in numbers:
        if n<my_value:
           return n

less = first_less_than(numbers, my_value)
print(less)
