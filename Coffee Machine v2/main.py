from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys



def operate():

    choice = input(f"What drink would you like?{menu.get_items()}: ").lower()

    if choice == "off":
        sys.exit()
    elif choice == "report":
        coffee_machine.report()
        operate()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if wallet.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
                operate()
            else:
                operate()    
        else:
            operate()                         
                

coffee_machine = CoffeeMaker()
menu = Menu()
wallet = MoneyMachine()
operate()