#Create a program that ask user to input 2 numbers. Print the lower number.

def smaller_number(firstnumber, secondnumber):
    lowest = firstnumber

    if secondnumber < lowest:
        lowest = secondnumber

    print("The lowest number is: ",lowest)


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

smaller_number(firstnumber, secondnumber)