def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

n1 = float(input("What is your first number: "))

while True:
    for symbol in operations:
        print(symbol)

    operation = input("Choose an operation: ")
    n2 = float(input("Choose your second number: "))

    calculation_function = operations[operation]
    answer = calculation_function(n1, n2)

    print(f"{n1} {operation} {n2} = {answer}")

    continue_ = input("Type 'y' to continue with this result, or 'n' to start new: ").lower()

    if continue_ == "y":
        n1 = answer
    else:
        break