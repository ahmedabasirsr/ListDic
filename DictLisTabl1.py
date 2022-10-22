dicList = {"name":["job","Salary","Age"],
          "hussan":["it",4000,37],
          "omar":["account", 3000, 45],
          "mustafa":["it",5000,41],

    }

#dicList.update({"omar":[2]})=55        #cant to cahang
#dicList["omar":[2]]=55 cant to cahange
print (dicList)

l = len(dicList)
'''print ("L is dimension of dictionary dictList: ",l)
listn=[]
lk=[]
lv=[]
#for i in range(l):
    
for k,v in dicList.items():
    lk.append(k)
    lv.append(v)
        
print("****************",lk)
print(lv)'''
list3=["","",0,0]
for i in range(l):
    for k,v in dicList.items():
        k = list(dicList.keys())
        v = list (dicList.values())
        list3[0]=k[i]
        list3[1:]=v[i]
    print(list3)      

























































