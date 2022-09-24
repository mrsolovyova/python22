# Есть строка letters. Нужно пройтись по каждому символу строки с помощью цикла и:
#
# Посчитать количество символов равных значению переменной template
# Вывести все символы, не равные значению exclude
# Для теста можно использовать:
#
# letters = 'Who keeps company with the wolf, will learn to howl.'
# template = 'w'
# exclude = 'l'
# Важно: при выполнении задания соблюдать правила оформления кода (стиль кода)!

letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'
count_template = 0

for i in letters:
    if template == i:
        count_template += 1
    else:
        continue
print(count_template)

for j in letters:
    if exclude != j:
        print(j)
    else:
        continue
