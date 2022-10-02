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


def print_report(money, resources_dict):
    """Input: value of money and dictionary of resources
    Outcome: prints all resources state."""
    for key, value in resources_dict.items():
        unit = ""
        if key in ("water", "milk"):
            unit = "ml"
        else:
            unit = "g"

        print(f"{key.title()}: {value} {unit}")
    print(f"Money: ${money}")


def coffee_machine():
    """Coffee Machine simulator"""
    program_working = 1
    money = 0
    while program_working == 1:
        print(logo)
        answer = ""
        while answer not in ("espresso", "latte", "cappuccino", "off", "report"):
            answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if answer == "off":
            return 0
        elif answer == "report":
            print_report(money=money, resources_dict=resources)



coffee_machine()