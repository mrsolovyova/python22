# Написать простую программу, в которой создаются переменные со значениями:
# Переменная	Тип	Значение
# Переменная 1	Число	546
# Переменная 2	Строка	Моя первая программа
# Переменная 3	Список из двух предыдущих переменных (1 и 2)
# Переменная 4	Словарь, в котором имя переменной 1 и 2 – это ключ, а их значение – значения словаря.
# Переменная 5	Результат умножения переменной 1 на 234, а затем конкатенация переменной 2 с полученным результатом через пробел.
# После этого необходимо вывести все переменные при помощи оператора print
a1 = 546
a2 = 'Моя первая программа'
a3 = [a1, a2]
a4 = {
     'a1': a1,
     'a2': a2}
a5 = a2 + ' ' + str(a1 * 234)

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)