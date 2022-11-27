money = 0

def addToBankAccount(sum: float):
    global money
    money += sum

def substractFromBankAccount(sum: float):
    global money
    money -= sum

def moneyConversion(sum: float, v1, v2):
    match v1,v2:
        case "USD","KZ":
            return sum * 470
        case "KZ","USD":
            return sum / 470
        case _:
            return "ERROR"

addToBankAccount(500)
print(money)

substractFromBankAccount(30)
print(money)

print(moneyConversion(money,"KZ","USD"))
