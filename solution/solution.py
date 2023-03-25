balance = 0


def main():
    print("balance:", balance)
    deposit(100)
    withdraw(50)
    print("balance:", balance)

def deposit(money):
    global balance
    balance += money


def withdraw(money):
    global balance
    balance -= money


if __name__ == "__main__":
    main()
