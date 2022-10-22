#Unpacking * and ** for list,dictionary and string
'''
lis = [1,2,3]
print (" print normaly list: ",lis)
print ("print unpacking valus(only values): ",*lis)
print ("print unpacking *lis : ",type("*lis"))
'''
'''
def sum(x,y,z):
    print( x+y+z)
# list has 3 values
lis = [1,2,3]
# here use unpacking list
sum(*lis)
'''
'''
def sum(*args):
    # function take unlimited number of arguments
    s=0
    for i in args:
        s +=i
    print(s)

lis1 = [1,2,3]
lis2 = [4,5,6]
lis3 = [7,8,9]
# function use unpacking lists
sum(*lis1,*lis2,*lis3)
'''
'''
lis = [1,2,3,4,5,6,7,8,9]
a,b,*c,d =lis
print("print first elemet of list: ",a)
print("print the second elements of list: ",b)
print("print the rest elements of list except last elemtent: ",c)
print("print the last element of list: ",d)


lis1 = [1,2,3]
lis2 = [4,5,6]
lis3 = [7,8,9]
merg_lis =[*lis1,*lis2,*lis3]
print ("print unpackin for every list in new list: ",merg_lis)
'''

dict1 = {1:"a",2:"b"}
dict2 = {3:"c",4:"d"}
dict3 = {5:"e",6:"g"}
merge_dict = {*dict1,*dict2,*dict3} # unpacking only keys
print("unpacking only keys: ",merge_dict)
merge_dict = {**dict1,**dict2,**dict3} # unpacking keys and values
print("unpacking keys and values: ",merge_dict)


























