"""
Programmer: Zach Hidalgo
Program: starbucksSCP
Program Version: 3.10.2
Created On: 10/21/2022 08:58:00
Last Modified: 10/21/2022 08:58:00
"""

def espresso(quantity, coffee, water):
    '''
    :param quantity: number of orders of espresso
    :param coffee: parameter keeping track of total coffee
    :param water: parameter keeping track of total water
    :return: updated resources after serving quantity*espresso servings
    '''
    coffee = coffee - (quantity * 8)
    water = water - (quantity * 1.5)

def americano(quantity, size, coffee, water):
    '''
    : Americano mix : 1 shot of espresso and 3 oz. of hot water
    :param quantity: number of orders of americano
    :param size: serving size (Tall / grande / venti / trenta)
    :param coffee: keeping track of total coffee powder
    :param water: parameter of keeping track of total water
    :return: updated resources after serving quantity * size * americano servings
    '''

    coffee = coffee - quantity*((size/4)*1)
    water = water - quantity*((size/4)*3)


print("Program to keep track of Starbucks supply chain")
print("Enter the quantities of the raw materials at the beginning of the day")

coffee = float(input("Enter coffee the quantity: \t"))
milk = float(input("Enter milk the quantity: \t"))
water = float(input("Enter water the quantity: \t"))
icecream = float(input("Enter icecream the quantity: \t"))
Whiskey = float(input("Enter whiskey the quantity: \t"))
chocolate = float(input("Enter chocolate the quantity: \t"))

# setting different serving size values
tall = 12
grande = 16
venti = 24
trenta = 31

espresso(2, coffee, water)
americano(2, venti, coffee, water)

print("Remaining Supplies")
print("The leftover coffee powder is", coffee)
print("The remaining water is", water)


