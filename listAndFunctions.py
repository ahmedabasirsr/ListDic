# create Lists

colors=["black","white","green","red","orange","pink","blue"]
numbers=[5,9,6,9,8,12,9,200]
mixlist=["m",3,"n",9,"y",4,"r"]

#Accessing vlues in list
#[del,len(),index(),insert(),append(),count(),pop(),reverse(),remove()

print(colors[0],numbers[1],mixlist[4])
colors[2]="orange" # add new parmeter in list colors
print(colors)
del numbers[2]
print(numbers) # delete third parmetre of list numbers

# Built-in list methods
'''
print (len(colors),len(numbers),len(mixlist)) # numbers of parmetrs lists
print (colors.index("red"))
numbers.insert(3,500)
print(numbers)
colors.append("yellow") # add parmeter to end list
print(colors)
print (numbers.count(9)) # how many number 9 in list numbers
colors.pop()             # remove the last item in list
print(colors)
numbers.reverse()
print(numbers)
numbers.remove(200)
print(numbers)
'''
#Math with lists
newlist=numbers+mixlist
print(newlist)
print(mixlist*2)
