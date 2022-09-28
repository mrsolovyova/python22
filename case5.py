# функция поиска имени в справочнике и выдачи номера телефона при соответствии
def search():
    for key in phone_book:
        if check_name == key:
            print(phone_book[key])
            break
    else:
        print("undefined")


phone_book = {"Иван": "3916", "Катя": "1298",
              "Лена": "0010", "Иосиф": "1953",
              "Владимир": "2022"}

check_name = input("Введите имя: ")
search()
