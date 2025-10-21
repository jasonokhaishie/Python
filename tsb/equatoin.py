# simple_calculator.py

def get_number(prompt):
    """Prompt the user and return a float. Re-prompts on invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Try again.")

def calculate(a, b, op):
    """Perform arithmetic using an if/elif/else ladder."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif op == "%":
        if b == 0:
            return "Error: Modulo by zero"
        return a % b
    elif op == "**":
        return a ** b
    else:
        return f"Error: Unsupported operator '{op}'"

def main():
    print("Welcome! Simple calculator. Type 'q' anytime to quit.")
    while True:
        first = input("Enter first number (or 'q' to quit): ").strip()
        if first.lower() == "q":
            break
        # validate first
        try:
            a = float(first)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        second = input("Enter second number (or 'q' to quit): ").strip()
        if second.lower() == "q":
            break
        try:
            b = float(second)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        op = input("Choose operator (+, -, *, /, %, **): ").strip()
        if op.lower() == "q":
            break

        result = calculate(a, b, op)
        print("Result:", result)
        print("-" * 30)

    print("Goodbye!")

if __name__ == "__main__":
    main()
