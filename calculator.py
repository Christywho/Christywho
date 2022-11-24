inp = input("Insert only one operator at a time(+ or - or / ot *): ")
inp.replace(' ', '')
# Addition
if '+' in inp:
    a = inp.split('+')
    print(int(a[0])+int(a[1]))
# Subtraction
elif '-' in inp:
    s = inp.split('-')
    print(int(s[0]) - int(s[1]))
# Division
elif '/' in inp:
    d = inp.split('/')
    print(int(d[0]) / int(d[1]))
# Multiplication
elif '*' in inp:
    m = inp.split('*')
    print(int(m[0]) * int(m[1]))
else:
    print("Error 69.....Insert only one operator at a time(+ or - or / ot *)")
