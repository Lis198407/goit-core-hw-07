class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        # Додайте поле birthday для дня народження в клас Record . 
        # Це поле має бути класу Birthday. Це поле не обов'язкове, але може бути тільки одне.

    def add_birthday():
        pass
    # Додайте функціонал роботи з Birthday у клас Record, а саме функцію add_birthday, яка додає день народження до контакту.
    # Додайте функціонал перевірки на правильність наведених значень для полів Phone, Birthday.

    @input_error
    def add_birthday(args, book):
        # реалізація
        pass

    @input_error
    def show_birthday(args, book):
        # реалізація
        pass

    @input_error
    def birthdays(args, book):
        # реалізація
        pass


class Adressbook:
    pass
# Додайте та адаптуйте до класу AddressBook нашу функцію з четвертого домашнього завдання, тиждень 3, 
# get_upcoming_birthdays, яка для контактів адресної книги повертає список користувачів, 
# яких потрібно привітати по днях на наступному тижні.

def main():
    pass
# Тепер ваш бот (4 домашнє завдання тиждень 5) повинен працювати саме з функціоналом класу AddressBook. 
# Це значить, що замість словника contacts ми використовуємо book = AddressBook()

# Тож в фіналі наш бот повинен підтримувати наступний список команд:
# add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним номером, або телефонний номер к контакту який вже існує.
# change [ім'я] [новий телефон]: Змінити телефонний номер для вказаного контакту.
# phone [ім'я]: Показати телефонний номер для вказаного контакту.
# all: Показати всі контакти в адресній книзі.
# add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
# show-birthday [ім'я]: Показати дату народження для вказаного контакту.
# birthdays: Показати дні народження, які відбудуться протягом наступного тижня.
# hello: Отримати вітання від бота.
# close або exit: Закрити програму.

    # elif command == "add":
    #         print(add_contact(args, book))