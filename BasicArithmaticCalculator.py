# This project is a simple Arithmatic Calculator

#Asking  user the operation
op = input("Enter the Arithmatic Operator ( / , *  , + , - ) : ")

#Performing Addition along with Input Validation
if op == "+":
    firstNumber = input("Enter First Number :")
    secondNumber = input("Enter Second Number :")

    if firstNumber == "":
        print("First Number is Missing! Can't perform Addition")
    else:
        firstNumber = float(firstNumber)

    if secondNumber == "":
        print("Second Number is Missing! Can't Perform Addition")
    else:
        secondNumber = float(secondNumber)

    if firstNumber and secondNumber != "":
        print("Addition is : ",firstNumber+secondNumber )

#Performing Subtraction along with Input Validation
elif op == "-":
    firstNumber = input("Enter First Number :")
    secondNumber = input("Enter Second Number :")

    if firstNumber == "":
        print("First Number is Missing! Can't perform Subtraction")
    else:
        firstNumber = float(firstNumber)

    if secondNumber == "":
        print("Second Number is Missing! Can't Perform Subtraction")
    else:
        secondNumber = float(secondNumber)

    if firstNumber and secondNumber != "":
        print("Subtraction is : ",firstNumber-secondNumber )

#Performing Multiplication along with Input Validation
elif op == "*":
    firstNumber = input("Enter First Number :")
    secondNumber = input("Enter Second Number :")

    if firstNumber == "":
        print("First Number is Missing! Can't perform Multiplication")
    else:
        firstNumber = float(firstNumber)

    if secondNumber == "":
        print("Second Number is Missing! Can't Perform Multiplication")
    else:
        secondNumber = float(secondNumber)

    if firstNumber and secondNumber != "":
        print("Multiplication is : ",firstNumber*secondNumber )

#Performing Division along with Input Validation
elif op == "/":
    firstNumber = input("Enter First Number :")
    secondNumber = input("Enter Second Number :")

    if firstNumber == "":
        print("First Number is Missing! Can't perform Division")
    else:
        firstNumber = float(firstNumber)

    if secondNumber == "":
        print("Second Number is Missing! Can't Perform Division")
    else:
        secondNumber = float(secondNumber)

#Validating Zero Division Error
    if firstNumber !="" and secondNumber != "":
        try:
            result = firstNumber/secondNumber
        except ZeroDivisionError:
            print("Can't Divide by Zero")
        else:
            print("The Division is : ", firstNumber/secondNumber)

else:
    print("Invalid Operator!")