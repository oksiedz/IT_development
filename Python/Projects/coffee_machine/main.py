from graphics import logo

# dictionaries
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# constant variables
WATER = "water"
MILK = "milk"
COFFEE = "coffee"
COST = "cost"
ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"
REPORT = "report"
OFF = "off"


def print_report(money, resources_dict):
    """Input: value of money and dictionary of resources
    Outcome: prints all resources state."""
    for key, value in resources_dict.items():
        unit = ""
        if key in (WATER, MILK):
            unit = "ml"
        else:
            unit = "g"

        print(f"{key.title()}: {value} {unit}")
    print(f"Money: ${money}")


def return_resource_from_menu(order_name, ingredient, dictionary):
    """Input: order name, ingredient and dictionary
    Output: return the needed resource per order"""
    if order_name == ESPRESSO and ingredient == MILK:
        return int(0)
    else:
        return int(dictionary[order_name]["ingredients"][ingredient])


def return_resource_from_resources(ingredient, available_resources):
    """Input: ingredient name and available resources
    Output: value of resources"""
    return int(available_resources[ingredient])


def resource_enough(needed, available, resource_name):
    """Input needed and available water, coffee and milk
    Output boolean true - if available resources are higher or equal needed one"""
    if needed >= available:
        return resource_name


def check_resources(order, menu, available_resources):
    """Input: type of coffee as order and dictionary with resources
    Output: boolean if there is enough resources to do the order"""
    needed_water = return_resource_from_menu(order, WATER, menu)
    needed_coffee = return_resource_from_menu(order, COFFEE, menu)
    needed_milk = return_resource_from_menu(order, MILK, menu)

    available_water = return_resource_from_resources(ingredient=WATER, available_resources=available_resources)
    available_coffee = return_resource_from_resources(ingredient=COFFEE, available_resources=available_resources)
    available_milk = return_resource_from_resources(ingredient=MILK, available_resources=available_resources)

    print(f"Needed water: {needed_water}, coffee: {needed_coffee}, milk: {needed_milk}")
    print(f"Available water: {available_water}, coffee: {available_coffee}, milk: {available_milk}")

    lacking_resources = ""
    if resource_enough(needed_water, available_water, WATER) == WATER:
        lacking_resources += WATER
        if resource_enough(needed_milk, available_milk, MILK) == MILK:
            lacking_resources += " and " + MILK
        if resource_enough(needed_coffee, available_coffee, COFFEE) == COFFEE:
            lacking_resources += " and " + COFFEE
    elif resource_enough(needed_milk, available_milk, MILK) == MILK:
        lacking_resources += MILK
        if resource_enough(needed_coffee, available_coffee, COFFEE) == COFFEE:
            lacking_resources += " and " + COFFEE
    elif resource_enough(needed_coffee, available_coffee, COFFEE) == COFFEE:
        lacking_resources += COFFEE

    return lacking_resources


def coffee_machine():
    """Coffee Machine simulator"""
    program_working = 1
    money = 0
    while program_working == 1:
        print(logo)
        answer = ""
        while answer not in (ESPRESSO, LATTE, CAPPUCCINO, OFF, REPORT):
            answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if answer == OFF:
            return 0
        elif answer == REPORT:
            print_report(money=money, resources_dict=resources)
        else:
            resources_status = check_resources(order=answer, menu=MENU, available_resources=resources)
            if resources_status == "":
                print("enough_resources")
            else:
                print(f"Sorry there is not enough {resources_status}")


coffee_machine()
