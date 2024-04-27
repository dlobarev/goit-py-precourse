def get_cats_info(path):
    cats=[]
    with open(path,'r') as fh:
        while True:
            x = fh.readline()
            if x != '':
                x = x.strip('\n')
                x = x.split(',')
                y = {'id':x[0],'name':x[1],'age':x[2]}
                cats.append(y)
                #print(cats)
            else:
                break
    return cats

get_cats_info('test.txt')