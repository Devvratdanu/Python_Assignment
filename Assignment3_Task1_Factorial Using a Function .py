def Factorial(Number):
    if Number <2:
        return 1
    else:
        return Number * Factorial(Number - 1)
Number = int(input("Enter a number : "))
print("Factorial of", Number, "is", Factorial(Number))
# This code defines a function to calculate the factorial of a number using recursion.


    