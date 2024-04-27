with open('test.txt', 'w+') as fh:
    symbols_written = fh.write('hello!')
    print(fh.tell())
    #fh.seek(1)


    fh.write('first line\nsecond line\nthird line')
    fh.seek(0)
    print(fh.read())
    fh.seek(0)
    lines = fh.readlines()
    print(lines)
