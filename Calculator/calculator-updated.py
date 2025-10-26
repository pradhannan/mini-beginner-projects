def calculations():
    while True:
        try:
            s = int(
                input(
                    "Please choose either \n1.To go ahead with calculations or\nType any else number to exit\n"
                )
            )
            if s == 1:
                basic_calculations()
            else:
                break
        except ValueError:
            print("please enter the correct number\n")


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

def outpt():
    out= input("\nWhat do you want to do next?\n"
                "Y - Continue Calculations\n"
                "H - View History\n"
                "C - Clear History\n"
                "Any other key - Exit\n").lower()
    return (out)
    

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


def basic_calculations():
    while True:
        num = number()
        while True:
            op = input(
                "Enter which operation: '+', '-', '*', '/','%', '**', '//'\n"
            )
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
            
            out = outpt()
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
                continue    # show menu again after history
            elif out == "c":
                history.clear()
                print("History cleared!\n")
                continue  # go back to ask again
            else:
                return  # exit calculations cleanly


def main():
    print("Hi! Welcome to the Calculator")
    calculations()


history = []
main()