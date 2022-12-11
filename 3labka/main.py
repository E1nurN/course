class Enum:
    _money = 0

    def setMoney(self, money: int):
        self._money = money

    def getMoney(self):
        return self._money

    def addToBankAccount(self,sum: float):
        self._money += sum

    def substractFromBankAccount(self,sum: float):
        self._money -= sum

    def moneyConversion(self,v1, v2):
        match v1,v2:
            case "KZ","USD":
                self._money /= 470
            case "KZ","RUB":
                self._money /= 7
            case "KZ","EUR":
                self._money /= 498
            case "USD","KZ":
                self._money *= 470
            case "RUB","KZ":
                self._money *= 7
            case "EUR","KZ":
                self._money *= 498
            case _:
                print("В процессе разработки")


class BankAccount:
    _name = ''
    _surname = ''
    _account = Enum()

    def setName(self, name: str):
        self._name = name

    def setSurname(self, surname: str):
        self._surname = surname

    def setAccount(self, account: Enum):
        self._account = account

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getAccount(self):
        return self._account

    def toString(self):
        return f'Name: {self.getName()} Surname: {self.getSurname()} Money: {self.getAccount().getMoney()}'

accounts = []
while True:
    a = int(input("1. Создание пользователя\n2. Выбрать пользователя\n0. Выйти\n"))

    if a == 0:
        break
    elif a == 1:
        print(1)
        account = BankAccount()
        account.setName(input("Name:"))
        account.setSurname(input("Surname:"))

        enum = Enum()
        enum.setMoney(float(input("Money:")))
        account.setAccount(enum)

        accounts.append(account)
    elif a == 2:
        print("Accounts:")
        for a in accounts:
            print(f'\t{a.toString()}')
        num = int(input("Номер аккаунта:")) - 1
        if num < len(accounts):
            while True:
                san = int(input("1. addToBankAccount\n2. substractFromBankAccount\n3. moneyConversion\n0. Выйти\n"))
                if san == 0:
                    break
                elif san == 1:
                    accounts[num].getAccount().addToBankAccount(float(input("Сумма: ")))
                    print('Ваш счет составляет: ' + str(accounts[num].getAccount().getMoney()))
                elif san == 2:
                    accounts[num].getAccount().substractFromBankAccount(float(input("Сумма: ")))
                    print('Ваш счет составляет: ' + str(accounts[num].getAccount().getMoney()))
                elif san == 3:
                    v1 = input("USD, RUB, KZT, EUR\n")
                    v2 = input("USD, RUB, KZT, EUR\n")
                    accounts[num].getAccount().moneyConversion(v1, v2)
                    print(accounts[num].getAccount().getMoney())

