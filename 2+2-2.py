while True:
    s = input("Знак (+,-,*,/):")
    if s == '0': break
    if s in ('+','-','*','/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
            if y != 0 and (x/y)%1 != 0:
                print(x/y)
            elif:
                print(int(x/y))
            else:
                print("Ты как из детсада сбежал, дошколёнок? еще раз на ноль поделишь - я тебя на ноль помножу!")