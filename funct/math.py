def format_string(string, length=0):
    return (string) if len(string)>=length else (((length - len(string)) // 2*' ')+string)
print(format_string(length=7,string='Петро'))