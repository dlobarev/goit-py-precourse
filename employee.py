def write_employees_to_file(employee_list, path):
    fh = open(path,'w')
    el = employee_list
    for i in el:
        if ',' not in i:
            for y in i:
                fh.write(y)
                fh.write('\n')
        else:
            fh.write(i)
            fh.write('\n')
    fh.close()

write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],'employee.txt')