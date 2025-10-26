def calculations():
    while True:
        try:
            s = int(
                input(
                    "Please choose either:\n"
                    "1. Direct Calculation (enter full expression)\n"
                    "Any other number to exit\n"
                )
            )
            if s == 1:
                direct_calculation()
            else:
                break
        except ValueError:
            print("Please enter the correct number\n")
def outpt():
    out= input("\nWhat do you want to do next?\n"
                "Y - Continue Calculations\n"
                "H - View History\n"
                "C - Clear History\n"
                "Any other key - Exit\n").lower()
    return (out)

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
            
            out = outpt()
            if out == "y":
                break
            elif out == "h":
                print("\n📜 Calculation History:")
                if not history:
                    print("No calculations yet!\n")
                else:
                    for item in history:
                        print(item)
                continue
            elif out == "c":
                history.clear()
                print("History cleared!\n")
                continue
            else:
                return
history=[]
calculations()
