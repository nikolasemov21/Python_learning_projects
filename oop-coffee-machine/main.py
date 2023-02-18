from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
# assigning the classes to objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while is_on:
    # user input for the required drink
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        # check if the user wants to turn off the coffe machine
        is_on = False
    elif choice == "report":
        # check if the user want a report for the ingredients and money in the machine
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        drink_cost = drink.cost
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink_cost):
            # ask the user to input money and check if the money and the ingredients are enough to make the coffe
            # that the user wants
            coffee_maker.make_coffee(drink)