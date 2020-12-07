emoticons = {
    "hot_beverage": "☕",
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

beverages = {
    "espresso": {
        "water": 100,
        "milk": 0,
        "coffee": 16,
        "money": -1.5
    },
    "latte": {
        "water": 100,
        "milk": 100,
        "coffee": 24,
        "money": -2.5
    },
    "cappuccino": {
        "water": 100,
        "milk": 150,
        "coffee": 24,
        "money": -3.5
    }
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}


# inserted_money = {
#     "penny":0,
#     "nickel":0,
#     "dime": 0,
#     "quarter": 0
# }

def report():
    global resources
    answer = ""
    for name in resources:
        answer += f"{name}: {resources[name]} \n"
    return answer


def set_resources(beverage):
    global resources
    new_resources = {}
    for name in resources:
        new_resources[name] = resources[name] - beverage[name]
    return new_resources


def calcuate_total(inserted_money):
    total = 0
    for coin_name in inserted_money:
        total += inserted_money[coin_name] * coins[coin_name]
    return total


def calculate_change(inserted_money, beverage):
    total = calcuate_total(inserted_money)
    change = total + beverage["money"]
    return round(change, 2)


def money_sufficient(inserted_money, beverage):
    if calculate_change(inserted_money, beverage) >= 0:
        return True
    return False


def resources_sufficient(beverage):
    global resources
    sufficient_flag = True
    if resources["water"] < beverage["water"]:
        print("not enough water")
        sufficient_flag = False
    if resources["milk"] < beverage["milk"]:
        print("not enough milk")
        sufficient_flag = False
    if resources["coffee"] < beverage["coffee"]:
        print("not enough coffee")
        sufficient_flag = False
    return sufficient_flag


# def order_beverage:


def start_coffee_machine():
    global resources
    beverage_name = input("What would you like? (espresso/latte/cappuccino):")

    if beverage_name == "report":
        print(report())

    else:
        if resources_sufficient(beverages[beverage_name]):
            amount_pennies = int(input("How many pennies:"))
            amount_nickels = int(input("How many nickels:"))
            amount_dimes = int(input("How many dimes:"))
            amount_quarters = int(input("How many quarters:"))
            inserted_money = {
                "penny": amount_pennies,
                "nickel": amount_nickels,
                "dime": amount_dimes,
                "quarter": amount_quarters
            }
            if money_sufficient(inserted_money, beverages[beverage_name]):
                change = calculate_change(inserted_money, beverages[beverage_name])
                resources = set_resources(beverages[beverage_name])
                print(f"Your change is {change}. Enjoy your {beverage_name} {emoticons['hot_beverage']}")
            else:
                print("The money you inserted is not sufficient")

    start_coffee_machine()


start_coffee_machine()
