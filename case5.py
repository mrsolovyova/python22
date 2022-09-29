PHONE_BOOK = {"Иван": "3916", "Катя": "1298",
              "Лена": "0010", "Иосиф": "1953",
              "Владимир": "2022"}


# функция поиска имени в справочнике и выдачи номера телефона при соответствии
def search():
    for key in PHONE_BOOK:
        if check_name == key:
            print(PHONE_BOOK[key])
            break
    else:
        print("undefined")


check_name = input("Введите имя: ")
search()
