numbers = range(5)
print(numbers) #we get the range range(0, 5)
#to see all the numbers we use for loop

for number in numbers:
    print(number) #now it prints all the numbers from 0 to 4

#a range that starts from a number till a number
    nums = range(5, 10)
    for num in nums:
        print(num) #it will print from 5 to 9

        #a range that jumps by 2
    numeros = range(5, 10, 2)
    for numero in numeros:
        print(numero) #it will print from 5 7 9

              #call range in the for loop
    chiffres = range(5, 10, 2)
    for chiffre in range(5):
        print(chiffre) #it will print from 0 to 4
