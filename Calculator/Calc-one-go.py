def calculations():
    while True:
        try:
            s = int(
                input(
                    "Please choose either:\n"
                    "1. Step-by-step Calculations\n"
                    "2. Direct Calculation (enter full expression)\n"
                    "Any other number to exit\n"
                )
            )
            if s == 1:
                basic_calculations()
            elif s == 2:
                direct_calculation()
            else:
                print("Goodbye! Thanks for using the calculator.\n")
                break
        except ValueError:
            print("Please enter the correct number\n")


def sum(a, b):
    print("---------------\n", a, "+", b, "=", a + b, "\n---------------")
    history.append(f"{a}+{b}={a+b}")


def diff(a, b):
    print("---------------\n", a, "-", b, "=", a - b, "\n---------------")
    history.append(f"{a}-{b}={a-b}")


def mul(a, b):
    print("---------------\n", a, "*", b, "=", a * b, "\n---------------")
    history.append(f"{a}*{b}={a*b}")


def div(a, b):
    print("---------------\n", a, "/", b, "=", a / b, "\n---------------")
    history.append(f"{a}/{b}={a/b}")


def power(a, b):
    print("---------------\n", a, "**", b, "=", a**b, "\n---------------")
    history.append(f"{a}**{b}={a**b}")


def floor_division(a, b):
    print("---------------\n", a, "//", b, "=", a // b, "\n---------------")
    history.append(f"{a}//{b}={a//b}")


def modulus(a, b):
    print("---------------\n", a, "%", b, "=", a % b, "\n---------------")
    history.append(f"{a}%{b}={a%b}")


def number():
    while True:
        try:
            number = int(input("Enter the number:\n"))
            break
        except ValueError:
            print("Oops! That's not a valid number. Try again!\n")
    return number


def zero_check_secondnum():
    while True:
        numm = number()
        if numm == 0:
            print("Oops! Cannot divide by zero! Enter a different number.\n")
        else:
            return numm


def output():
    out = input(
        "\nWhat do you want to do next?\n"
        "Y - Continue Calculations\n"
        "H - View History\n"
        "C - Clear History\n"
        "Any other key - Exit\n"
    ).lower()
    return out


def basic_calculations():
    while True:
        num = number()
        while True:
            op = input("Enter which operation: '+', '-', '*', '/','%', '**', '//'\n")
            if op in ["+", "-", "*", "/", "%", "**", "//"]:
                break
            else:
                print("Oops! That's not a valid operation. Try again!\n")
        if op == "/":
            numm = zero_check_secondnum()
            div(num, numm)
        elif op == "//":
            numm = zero_check_secondnum()
            floor_division(num, numm)
        elif op == "%":
            numm = zero_check_secondnum()
            modulus(num, numm)
        else:

            numm = number()

            if op == "**":
                power(num, numm)
            elif op == "+":
                sum(num, numm)
            elif op == "-":
                diff(num, numm)
            elif op == "*":
                mul(num, numm)
        while True:

            out = output()
            if out == "y":
                break
            elif out == "h":
                print("\n📜 Calculation History:")
                if not history:
                    print("No calculations yet!\n")
                else:
                    print("--------------------")
                    for item in history:
                        print(item)
                    print("--------------------\n")
                continue
            elif out == "c":
                history.clear()
                print("History cleared!\n")
                continue
            else:
                return


def direct_calculation():
    while True:
        expr = input("\nEnter your calculation (e.g., 5+3*2):\n")
        try:
            result = eval(expr)
            print("---------------\n", expr, "=", result, "\n---------------")
            history.append(f"{expr}={result}")
        except ZeroDivisionError:
            print("Oops! Cannot divide by zero.")
        except Exception:
            print("Invalid expression. Try again.")
        while True:

            out = output()
            if out == "y":
                break
            elif out == "h":
                print("\n📜 Calculation History:")
                if not history:
                    print("No calculations yet!\n")
                else:
                    print("--------------------")
                    for item in history:
                        print(item)
                    print("--------------------\n")
                continue
            elif out == "c":
                history.clear()
                print("History cleared!\n")
                continue
            else:
                return


def main():
    print("Hi! Welcome to the Calculator")
    calculations()


history = []
main()