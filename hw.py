result = None
operand = None
operator = None
wait_for_number = True

operand = input("Num: ")
while not result:
    try:
        result = int(operand)
    except ValueError:
        operand = input(f"{operand} is not a num? reenter: ")

while wait_for_number == True:
    operator = input("Oper: ")
    while not operator in ('+', '-', '*', '/', '='):
        operator = input("Oper: ")
    if operator == '+':
        operand = input("Num: ")
        while not result:
            try:
            result = int(operand)
            except ValueError:
            operand = input(f"{operand} is not a num? reenter: ")
        result = result + operand
        print(result)
    elif operator == '-':    
        result = result - operand
        print(result)
    elif operator == '*':    
        result = result * operand
        print(result)
    elif operator == '/':    
        result = result - operand
        print(result)
    else:
        wait_for_number = False
        print(result)
        break