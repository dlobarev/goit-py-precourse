def f6(a=10, *c, **d):
    print('a = ',a)
    for x in c:
        print('*c = ',x)
    for y1,y2 in d.items():
        print('**d.item1 = ',y1,' **d.item2 = ',y2)

f6(10, 6, 'a', 2, 3, Jack=1123, John=2231, Inge=1560)