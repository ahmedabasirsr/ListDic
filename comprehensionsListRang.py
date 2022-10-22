# Comperhensions
# create list of square numbers from 1 to 100
lis = []
for i in range(1,11):
    lis.append(i**2)
print(lis)


# 1) create lis = [vlaue for in range(1,11)]
lis = [i**2 for i in range(1,11)]
print(lis)

# 2) create lis = [from i value in range(1,11) if Condition ]
lis = [i for i in range(1,11) if i%2==0]
print (lis)


lis = [i  if i%2==0 else "odd" for i in range(1,11) ]
print (lis)

