#split_lists = [original_data[x:x+3] for x in range(0, len(original_data), 3)]
big_list =[i for i in range(100)]
#creat list with function range from 100 numbers
print (big_list)
split_lists = [big_list[x:x+10] for x in range(0,len(big_list),10)]
#creat 10 sublists of 10 numbers in every list
print(split_lists)