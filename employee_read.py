def read_employees_from_file(record,path):
    fh = open(path, 'a')
    l = record
    fh.write(f'{l}\n')
    #print(a)
    #x = a.split('\n')
    #print(x[-1])
    #if x[-1] == '': print(x.pop())
    #print(x)
    fh.close()
    #return x 
read_employees_from_file("Drake Mikelsson,19",'employee.txt')
    