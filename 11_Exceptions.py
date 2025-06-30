import math


def undefined_variable():
    try:
        print(not_defined_variable)
    except NameError as e:
        print("Ошибка:", e)


def convert_to_int_list(inputs):
    result = []
    for item in inputs:
        try:
            number = int(item)
            result.append(number)
        except ValueError:
            print(f"Ошибка преобразования: '{item}' не является числом")
    print("Результат:", result)


def write_to_readonly_file():
    try:
        file = open("example.txt", "r")  
        file.write("Тестовая строка")    
    except IOError as e:
        print("Ошибка ввода-вывода:", e)
    finally:
        file.close()
        print("Файл закрыт.")

# Точка входа в программу
def main():
    undefined_variable()
    print("")
    
    str_list = ['10', '20', 'abc', '30', '5.5', '40']
    convert_to_int_list(str_list)
    print("")
    
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Содержимое файла\n")
    write_to_readonly_file()
    print("")
    
    return 0

if __name__ == '__main__':
    main()
