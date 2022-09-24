# На вход получаем строку, состоящую из двух чисел и символа между ними. На выходе получаем результат операции с числами.
#
# Операция определяется символом:
#
# # - возвращает остаток от деления второго числа на первое
# ! - возвращает число, у которого сумма цифр больше
# @ - возвращает большее число из двух
# $ - возвращает число, у которого больше цифр
# В случае если оба числа удовлетворяют условию, то возвращается первое.
#
# Примеры:
#
# 28#26379 => 3
# 1111!23 => 23
# 123@876 => 876
# 456$0007 => 0007

x = input("Введите строку: ")

if "#" in x:
    y = x.split("#")
    y = list(map(int, y))
    result_y = y[1] % y[0]
    print(result_y)

elif "!" in x:
    y = x.split("!")
    y = list(map(int, y))
    lst1 = [int(i) for i in str(y[0])]
    lst2 = [int(i) for i in str(y[1])]
    result_y = max(sum(lst1), sum(lst2))
    if sum(lst1) > sum(lst2) or sum(lst1) == sum(lst2):
        print(y[0])
    elif sum(lst1) < sum(lst2):
        print(y[1])

elif "@" in x:
    y = x.split("@")
    y = list(map(int, y))
    result_y = max(y)
    print(result_y)

elif "$" in x:
    y = x.split("$")
    if len(y[0]) > len(y[1]) or len(y[0]) == len(y[1]):
        print(y[0])
    else:
        print(y[1])
else:
    print("Try again")
