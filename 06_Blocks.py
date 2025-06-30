# Простой цикл while
i = 7;
while (i < 10):

	print(i);    
	i += 1;  #$i++


# Условный оператор
a = 1;
b = 5;

if (a == b):

    print("a равно b");

else:

    print("a не равно b");

    
# Функция с параметром - контроль делимости на 3
def function_3(a):

    if (a%3 == 0):
    
        print("Число делится на 3");
    
    else:
    
        print("Число не делится на 3");
    

    
function_3(9);
function_3(10);
