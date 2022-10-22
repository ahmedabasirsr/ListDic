li = [1,"None","www2","www3","None"]

print(li)


for i in li:
    if i == "None":
        li.remove(i)

print(li)
print(len(li))




