import random

class Accounts:
    def __init__(self, id, name, bal):
        self.__id = id
        self.__name = name
        self.__bal = bal

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def bal(self):
        return self.__bal

    def update_bal(self, new_bal):
        self.__bal = new_bal

    def show(self):
        print(f"ID: {self.__id}, ім'я: {self.__name}, баланс: {self.__bal} грн")

class Bank:
    def __init__(self):
        self.__accs = []

    def new_acc(self, acc):
        self.__accs.append(acc)

    def del_acc(self, id):
        before = len(self.__accs)
        self.__accs = [a for a in self.__accs if a.id != id]
        return before != len(self.__accs)

    def sort_bal(self):
        self.__accs.sort(key=lambda a: a.bal, reverse=True)

    def show_all(self):
        if not self.__accs:
            print("немає акаунтів")
        for a in self.__accs:
            a.show()

    def get_account_by_id(self, id = None, name = None):
        if id is not None:
            for a in self.__accs:
                if a.id == id:
                    return a
        if name is not None:
            for a in self.__accs:
                if a.name == name:
                    return a
        return None

    def add(self, acc, x):
        acc.update_bal(acc.bal + x)
        print("поповнено")

    def take(self, acc, x):
        if x <= acc.bal:
            acc.update_bal(acc.bal - x)
            print("знято")
        else:
            print("замало грошей на балансі")



def main():
    b = Bank()
    while True:
        print("""
        1) новий акаунт
        2) увійти в акаунт
        3) показати всі акаунти (банк)
        4) сортувати акаунти (банк)
        5) видалити акаунт
        0) вихід
        """)

        ch = input("твій вибір: ")

        if ch == "1":
            auto = input("зробити ID автоматично?: ")
            if auto.lower() == "так":
                id = random.randint(1, 9999)
                print("ID:", id)
            else:
                id = int(input("введіть ID: "))

            name = input("ім'я: ")
            bal = 0.0

            a = Accounts(id, name, bal)
            b.new_acc(a)
            print("акаунт створено")

        elif ch == "2":
            key = input("введіть ID або ім'я: ")
            if key == "":
                continue
            acc = None
            if key.isdigit():
                acc = b.get_account_by_id(id = int(key))
            if acc is None:
                acc = b.get_account_by_id(name = key)
            if acc:
                while True:
                    acc.show()
                    print("""
                    1) поповнити
                    2) зняти
                    0) вийти з акаунта
                    """)
                    ch2 = input("твій вибір: ")
                    if ch2 == "1":
                        x = float(input("сума: "))
                        b.add(acc, x)
                    elif ch2 == "2":
                        x = float(input("сума: "))
                        b.take(acc, x)
                    elif ch2 == "0":
                        break
                    else:
                        print("невірний вибір")
            else:
                print("акаунт не знайдено")

        elif ch == "3":
            b.show_all()

        elif ch == "4":
            b.sort_bal()
            print("відсортовано")
            b.show_all()

        elif ch == "5":
            id = int(input("ID: "))
            if b.del_acc(id):
                print("видалено")
            else:
                print("не знайдено")

        elif ch == "0":
            break
        else:
            print("невірний вибір")


if __name__ == '__main__':
    main()
