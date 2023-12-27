#def functions: add, subtract, multiply, divide
#print options
#ask for values
#call the functions
#while loop to continue program until user exit

#def functions
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def subtract(a, b):
    answer = a - b
    print (str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiply(a, b):
    answer = a * b
    print (str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def divide (a, b):
    answer = a / b
    print (str(a) + " / " + str(b) + " = " + str(answer) + "\n")

#print options, while loop
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("Enter your selection: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int (input("Enter second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print ("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        subtract(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    elif choice == "e" or choice == "E":
        print("Program Ended.")
        quit()

