#Create a program that ask user to input 2 numbers. Print the bigger number.

def bigger_number(firstnumber, secondnumber):
    highest = firstnumber

    if secondnumber > highest:
        highest = secondnumber

    print("The bigger number is: ",highest)


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

bigger_number(firstnumber, secondnumber)