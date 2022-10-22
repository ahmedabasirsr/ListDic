lop=["+","-","*","/"]
br1 = float(input("unesi 1 broj "))
br2 = float(input("unesi 2 broj "))
uz = input("unesi znak opracije ")


if uz==lop[0]:
    zb=br1+br2
    print ("rezultat ",br1,"+",br2,"= ",zb)
else:
    if uz==lop[1]:
        od=br1-br2
        print ("rezultat ",br1,"-",br2,"= ",od)
    else:    

        if uz==lop[2]:
            mn=br1*br2
            print ("rezultat ",br1,"*",br2,"= ",mn)
            
        else:
            if uz==lop[3]:
                de=br1/br2
                print ("rezultat ",br1,"/",br2,"= ",de)
        
    
