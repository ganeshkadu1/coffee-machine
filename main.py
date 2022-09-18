from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

SHUT_DOWN = False

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not SHUT_DOWN:
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice == "off":
        SHUT_DOWN = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(menu_item):
            money_machine.make_payment(menu_item.cost)
            coffee_maker.make_coffee(menu_item)




