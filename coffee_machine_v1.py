import os
import sys
import time


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

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25
change = 0
user_money = 0

def water(user_choice):
    global MENU, resources
    if user_choice == 'espresso':
        if resources['water'] <  MENU['espresso']['ingredients']['water']:
            return False
        else:
            resources['water'] -= MENU['espresso']['ingredients']['water']
    
    elif user_choice == 'latte':
        if resources['water'] <  MENU['latte']['ingredients']['water']:
            return False
        else:
            resources['water'] -= MENU['latte']['ingredients']['water']  

    elif user_choice == 'cappuccino':
        if resources['water'] <  MENU['cappuccino']['ingredients']['water']:
            return False
        else:
            resources['water'] -= MENU['cappuccino']['ingredients']['water']
    return True

def coffee(user_choice):
    global MENU, resources
    if user_choice == 'espresso':
        if resources['coffee'] <  MENU['espresso']['ingredients']['coffee']:
            return False
        else:
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    
    elif user_choice == 'latte':
        if resources['coffee'] <  MENU['latte']['ingredients']['coffee']:
            return False
        else:
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']  

    elif user_choice == 'cappuccino':
        if resources['coffee'] <  MENU['cappuccino']['ingredients']['coffee']:
            return False
        else:
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
    return True


def milk(user_choice):
    global MENU, resources
    if user_choice == 'latte':
        if resources['milk'] <  MENU['latte']['ingredients']['milk']:
            return False
        else:
            resources['milk'] -= MENU['latte']['ingredients']['milk']  

    elif user_choice == 'cappuccino':
        if resources['milk'] <  MENU['cappuccino']['ingredients']['milk']:
            return False
        else:
            resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
    return True


def has_money(user_choice, qt, dm, nk, pn):
    global change, user_money
    user_money = qt*quarter + dm*dime + nk*nickel + pn*penny
    if user_choice == 'espresso':
        change = round(user_money - MENU['espresso']['cost'],2)
        if change >= 0:
            return True
    elif user_choice == 'latte':
        change = round(user_money - MENU['latte']['cost'],2)
        if change >= 0:
            return True
    elif user_choice == 'cappuccino':
        change = round(user_money - MENU['cappuccino']['cost'],2)
        if change >= 0:
            return True
    return False

def switch_off():
    print("Switching off...")
    for _ in range(4):
        time.sleep(1)
        print(".............")
    sys.exit()


def report():
    for key in resources:
        if key == 'water' or key == 'milk':
            print("{}: {} ml".format(key,resources[key]))
        if key == 'coffee':
            print("{}: {} gm".format(key,resources[key]))

def main():
    os.system('clear')
    while True:
        user_choice = input("What would you like? (espresso|latte|cappuccino): ")

        if user_choice == 'off':
            switch_off()

        if user_choice == 'report':
            report()
            continue

        if not water(user_choice):
                print("Not enough water")
                break            
        if not coffee(user_choice):
            print("Not enough coffee")
            break            
        if not milk(user_choice):
            print("Not enough milk")
            break
        
        print("Please insert some coins\n")
        qt = float(input("How many quarters? "))
        dm = float(input("How many dimes? "))
        nk = float(input("How many nickels? "))
        pn = float(input("How many pennies? "))

        if has_money(user_choice,qt,dm,nk,pn):
            print("Here is your: ", user_choice)
            print("Here is your change: ", change)
        else:
            print("You do not have enough money")
            print("Price of {} is {}".format(user_choice,MENU['latte']['cost']))
            print("You have: ", user_money)


if __name__ == "__main__":
    main()
