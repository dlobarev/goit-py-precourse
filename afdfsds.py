result = None
operand = None
operator = None
wait_for_number = True

while wait_for_number:
    try:
        operand = input()
        result = float(operand)
        wait_for_number = False
    except ValueError:
        print(f"{operand} is not a number")
while operator != '=':
    operator = input()
    if operator == '=':
        print(f"Result: {result}")
    elif operator == '+':
        wait_for_number = True
        while wait_for_number:
            try:
                operand = input()
                result = result + float(operand)
                wait_for_number = False
            except ValueError:
                print(f"{operand} is not a number")
    elif operator == '-':
        wait_for_number = True
        while wait_for_number:
            try:
                operand = input()
                result = result - float(operand)
                wait_for_number = False
            except ValueError:
                print(f"{operand} is not a number")
    elif operator == '*':
        wait_for_number = True
        while wait_for_number:
            try:
                operand = input()
                result = result * float(operand)
                wait_for_number = False
            except ValueError:
                print(f"{operand} is not a number")
    elif operator == '/':
        wait_for_number = True
        while wait_for_number:
            try:
                operand = input()
                result = result / float(operand)
                wait_for_number = False
            except ValueError:
                print(f"{operand} is not a number")
    else:
        print(f"{operator} is not in - + * or /")
    
        
    
        
            
        
            
            
        
        
            
        
            
                
            
                
            
                
            
                
    
        
                
                
                
                
        
            
        
            

        
            
        
            