for i in range(10, 21):
    print(i, end=' ')

print(' ')
print(' ')

for i in range(10, 21):
    if i%3 != 0:
        continue
    print (i, end=' ')

print(' ')
print(' ')

numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number <1:
        print(number)
        break
else:
    print("Элемент не найден")
