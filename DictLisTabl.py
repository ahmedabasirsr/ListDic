dicLis = {1:["Name","Age","Salary"],
          2:["Ahmed",33,1200],
          3:["Ali", 27, 1500],
          4:["Husain",31,2000],
          5:["Muna", 25, 1700]
    }
print(dicLis)
print(dicLis[1])
print("\t",dicLis[1][0],"\t ",dicLis[1][1],"\t ",dicLis[1][2])
print("\t",dicLis[2][0],"\t ",dicLis[2][1],"\t ",dicLis[2][2])
print("\t",dicLis[3][0],"\t ",dicLis[3][1],"\t ",dicLis[3][2])
print("\t",dicLis[4][0]," ",  dicLis[4][1],"\t ", dicLis[4][2])
print("\t",dicLis[5][0],"\t ",dicLis[5][1],"\t ",dicLis[5][2])
print("\n")
print("******************************************************")
print("******************************************************")

li=list(dicLis) # convert keys of dictionary in list li
print (li)
lii=list(dicLis.items()) # convert dictionary in list and tuple
print (lii)
print (len(dicLis)) # dimension of dictionaru(numbers of rows)
print("******************************************************")
print("******************************************************")

for i in range(len(dicLis)):
    for x,y in dicLis.items():
        x = list(dicLis.keys())
        y = list(dicLis.values())
    print(x)
    print(y)
print("******************************************************")
print("******************************************************")
# lists of keys and values
lisk=[]
lisv=[]

for k,v in dicLis.items():  # k(1,5): is values of keys, v(1,5) is values of values dictionary
    
    lisk.append(k)          # add element in empty list
    lisv.append(v)
print(" create list of keys dictionary:\n",lisk)
print(" create list of values dictionary:\n",lisv)
print("******************************************************")
print("******************************************************")

for i,j in enumerate(lisv):  # enumerate gives index(i) and value(j)
    print (i)
    print(j)
print("******************************************************")
print("******************************************************")
print("--------------create dictionay from list--------------")
dictnew={}
for i,j in enumerate(lisv):
    list1 = j
    for x in list1:
        dictnew[list1[0]]=list1[1:]
print(dictnew)




























































