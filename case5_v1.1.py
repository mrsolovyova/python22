PHONE_BOOK = {"Иван": "3916", "Катя": "1298",
              "Лена": "0010", "Иосиф": "1953",
              "Владимир": "2022"}


# функция поиска имени в справочнике и выдачи номера телефона при соответствии
def search(check_name):
    print(PHONE_BOOK.get(check_name, 'undefined'))


check_name = input("Введите имя: ")
search(check_name)
