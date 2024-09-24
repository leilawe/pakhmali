import csv
import math


def addition(a, b):
    return a + b

def difference(a, b):
    return a - b

def product(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def factorial(a):
    if a < 0:
        return "Error! Factorial of a negative number."
    elif a==0 or a==1:
        return 1
    else:
     return math.factorial(a)


def save_history(operation, result):

    final_result=[operation, result]
   
    
    with open("history.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(final_result)


def display_menu():
    print("\n Calculator Menu:")
    print("1. Addition")
    print("2. Difference")
    print("3. Product")
    print("4. Division")
    print("5. Power")
    print("6. Factorial")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-7): ")

        if choice == "7":
            print("Exiting...")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if choice == "1":
                result = addition(a, b)
                operation = f"{a} + {b}"
            elif choice == "2":
                result = difference(a, b)
                operation = f"{a} - {b}"
            elif choice == "3":
                result = product(a, b)
                operation = f"{a} * {b}"
            elif choice == "4":
                result = division(a, b)
                operation = f"{a} / {b}"
            elif choice == "5":
                result = power(a, b)
                operation = f"{a} ^ {b}"
        elif choice == "6":
              a = int(input("Enter the number: "))
              result = factorial(a)
              operation = f"factorial({a})"

        else:
             print("Invalid choice! Please try again.")
             continue
       
     
        print(f"Result: {result}")
    
      
        save_history( operation, result)


main()
