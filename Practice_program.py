def smaller_number(firstnumber, secondnumber):
    if firstnumber < secondnumber:
        return firstnumber
    else:
        return secondnumber

def bigger_number(firstnumber, secondnumber):
    if firstnumber > secondnumber:
        return firstnumber
    else:
        return secondnumber

while True:
    try:
        firstnumber = int(input("Please input 2 numbers: "))
        break
    except:
        print("Input error, try again")
while True:
    try:
        secondnumber = int(input("Please enter your second number: "))
        break
    except:
        print("Input error, try again")

if firstnumber == secondnumber:
    print("Equal")
    print("The sum of both numbers are: ", firstnumber + secondnumber)
    print("The difference of both numbers are: 0")
    print("The product of both numbers are: ", firstnumber * secondnumber)
    print("The quotient of both numbers are: 1 or 1.0")
    print("The remainder of both numbers are: 0")
    print("The result when the first number is raised to the second number: ", secondnumber ** firstnumber)
else:
    print("Not Equal")
    print("The bigger number is: ", bigger_number(firstnumber, secondnumber))
    print("The lower number is: ", smaller_number(firstnumber, secondnumber))
    print("The sum of both numbers are: ", firstnumber + secondnumber)
    print("The difference of both numbers are: ", firstnumber - secondnumber)
    print("The product of both numbers are: ", firstnumber * secondnumber)
    print("The quotient of both numbers are: ", firstnumber // secondnumber, "or", firstnumber / secondnumber)
    print("The remainder of both numbers are: ", firstnumber % secondnumber)
    print("The result when the first number is raised to the second number: ", secondnumber ** firstnumber)

