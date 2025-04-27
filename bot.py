# example.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    a = 10
    b = 5

    print(f"Addition {a} + {b} = {add(a, b)}")
    print(f"Subtraction {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication {a} * {b} = {multiply(a, b)}")
    print(f"Division {a} / {b} = {divide(a, b)}")

if __name__ == "__main__":
    main()

