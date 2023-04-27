#Create a program that asks you your weight than if its in kg or pounds,when you choose one it give you the weight
weight = float(input("Enter the weight: "))
unit = input("Is it in kilogram (k) or in pound (l)?: ")


if unit.upper == "K":
    converted = weight / 0.45
    print("Your weight in pounds is: " + str(converted))
else:
    converted = weight * 0.45
    print("Your weight in kilograms is: " + str(converted))
        



