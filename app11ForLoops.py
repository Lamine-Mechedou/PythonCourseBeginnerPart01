numbers = [1, 2, 3, 4, 5]
print(numbers)

for item in numbers: # in iteration variable will be 1 in the second 2,..etc
    print(item) #now i see each item in a new line

 #I can do the same with while but the code would be a bit longer

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1   
