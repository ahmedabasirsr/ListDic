br1 = float(input("unesi prvi broja "))
zo = input("unesi oznka opracija ")
br2 = float(input("unesi drugi broja "))
print(type(zo))
if zo == "+" :
    r=br1+br2
    print("Rezultat je ",br1," + ",br2," = ",r)
else:
    if zo == "-" :
        r = br1-br2
        print("Rezultat je ",br1," - ",br2," = ",r)
    else:
        if zo == "*" :
            r = br1 * br2
            print("Rezultat je ",br1," * ",br2," = ",r)
        else :
            if zo == "/" :
                r = br1 / br2
                print("Rezultat je ",br1," / ",br2," = ",r)
