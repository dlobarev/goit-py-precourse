def total_salary(path):
    fh = open(path,'r')
    s = float()
    while True:
        x = fh.readline()
        if len(x) == 0:
            break
        else:
            if '\n' in x:
                s = s + float(x[x.find(',')+1:x.find('\n')])
            else:
                s = s + float(x[x.find(',')+1:])
    fh.close()
    return s
print(total_salary('test.txt'))
    
    
