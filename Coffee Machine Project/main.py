from data import MENU, resources
import sys

def report():
    """Gives back a report of our current resources"""
    print(f"Water: {resources['water']}ml.\nMilk: {resources['milk']}ml.\nCoffee: {resources['coffee']}gr.\nMoney: ${resources['money']}.\n")

def check_resources(drink):
    """Checks if there are sufficient resources to produce the drink we ordered"""
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry not enough water for your drink")
        return False
    elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry not enough milk for your drink")
        return False
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry not enough coffee for your drink")
        return False
    else:
        return True

def produce_drink(drink):
    """Simply reduces the number of resources according to the drink we ordered"""
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']

def collect_money(drink):
    """Asks the user the number of coins is about to insert,
    calculates the amount
    and informs him if the amount is enough and if there are change"""
    pennies = int(input("How many pennies: "))
    nickels = int(input("How many nickels: "))
    dimes = int(input("How many dimes: "))
    quarters = int(input("How many quarters: "))
    amount = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    if amount >= MENU[drink]["cost"]:
        resources["money"] += MENU[drink]['cost']
        print("Your order received\nDrink is being prepared")
        print(f"Your change: ${round(amount - MENU[drink]['cost'], 2)}")
        return True
    else:
        print("Sorry not enough. Money refunded")
        return False

def operate():
    """Coffee Machine starts to operate"""
    answer = input("What would you like? (espresso/latte/cappuccino):").lower()
    if answer == "off":
        sys.exit("Coffee Machine Turned Off")
    elif answer == "report":
        report()
        operate()
    else:
        if check_resources(answer):
            print(f"Your drink costs: ${MENU[answer]['cost']}")
            if collect_money(answer):
                produce_drink(answer)
                print(f"Your {answer} is ready☕")
                operate()
            else:
                operate()
        else:
            operate()

resources['money'] = 0
operate()