# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

str_two_numbers = input("По условию нужно ввести два числа через пробел: ")
num_set_1 = set(input("Введите первый набор чисел: ").split())
num_set_2 = set(input("Введите второй набор чисел: ").split())
res_list_1 = [num for num in list(num_set_1) if num in list(num_set_2)]
res_list_int = []
for num in res_list_1:
    res_list_int.append(int(num))
print(sorted(res_list_int))
