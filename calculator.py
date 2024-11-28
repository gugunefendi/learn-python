x = 1
y = 2

z = x + y
print(z)

firstNumber = input("Input first number: ")
secondNumber = input("Input second number: ")

sum = firstNumber + secondNumber

print(sum) # this will print string

# add int() for convert string to int
repairSum = int(firstNumber) + int(secondNumber)

print(repairSum)

# Float
firstFloat = input("Input first float: ")
secondFloat = input("Input second float: ")

sumFloat = float(firstFloat) + float(secondFloat)

print(sumFloat)

# rounded float
roundedFloat = round(sumFloat)

print(roundedFloat)

# get 2 number after comma
addComma = round(sumFloat, 2)
addCommaSecondWay = f"{sumFloat:.2f}"

print(addComma)
print(addCommaSecondWay)