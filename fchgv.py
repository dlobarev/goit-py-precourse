op = None
b = 0
while True:
    try:
        a = input("dig: ")
        b = float(a)
        break
    except ValueError:
        print(f"{a} is not a num, reenter:")

while True:
        op = input("Oper: ")
        while not op in ('+', '-', '*', '/', '='):
            op = input("Oper: ")
        if op == '=':
            print(b)
            break
        elif op == '+':
            while True:
                try:
                    a = input("dig: ")
                    b = b + float(a)
                    break
                except ValueError:
                    print(f"{a} is not a num, reenter:")
        elif op == '-':
            while True:
                try:
                    a = input("dig: ")
                    b = b - float(a)
                    break
                except ValueError:
                    print(f"{a} is not a num, reenter:")
        elif op == '*':
            while True:
                try:
                    a = input("dig: ")
                    b = b * float(a)
                    break
                except ValueError:
                    print(f"{a} is not a num, reenter:")
        elif op == '/':
            while True:
                try:
                    a = input("dig: ")
                    b = b / float(a)
                    break
                except ValueError:
                    print(f"{a} is not a num")
                except ZeroDivisionError:
                    print(f"{a} div occured:")           
print(b)
            
