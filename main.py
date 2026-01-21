from sum import add
from difference import subtract
from product import multiply
from division import divide

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Sum of {a} and {b} is: {add(a, b)}")
    print(f"Difference of {a} and {b} is: {subtract(a, b)}")
    print(f"Product of {a} and {b} is: {multiply(a, b)}")
    print(f"Division of {a} by {b} is: {divide(a, b)}")

if __name__ == "__main__":
    main()