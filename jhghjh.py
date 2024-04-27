def format_ingredients(items):
    suf = ''
    if len(items) > 0:
        suf = items.pop()
    if len(items) > 0:
        suf = str(items.pop()) + ' and ' + suf
        for i in reversed(items):
            suf = i + ', ' + suf
        return suf
    return suf
#    if str(items.pop()) + ' and ' + 
#    text = ''
#   
#    print(f'{text}{suf}')


print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar", "bread", "whiskey", "milk"]))
print(format_ingredients(["milk"]))
print(format_ingredients(["whiskey", "milk"]))
print(format_ingredients([]))
