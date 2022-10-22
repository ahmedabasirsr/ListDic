br1=float (input('unesi prvi broja '))
op= input('unesi znak opracija ')
br2= float(input('unesi drugi broh '))

if op == '+':
    print(br1 + br2)
else:
    if op == '-' :
        print(br1 - br2)
    else:
        if op == '*' :
            print(br1 * br2)
        else:
            if op == '/' :
                print(br1 / br2)
            else:
                print('unali ste pogresna znak opracija')
