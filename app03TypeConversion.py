birth_year = input("Enter your birth here: ")
age = 2023 - int(birth_year) #convert string into int
print(age)

# convert a value into : int()
# convert a value into : float()
# convert a value into : bool()
# convert a value into : str()
#EXERCISE: a basic calculator

num_one = input("Enter the first number: ")
num_two = input("Enter the second number: ")
sum = float(num_one) + float(num_two)
print("sum: " + str(sum)) #to be able # to concatenate a str with a float

#I can do the same:

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
multiple = first * second
print("sum: " + str(multiple))
