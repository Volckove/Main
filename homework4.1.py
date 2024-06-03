
first_list = [1,2,0,3,9,0,4,5,6,0,4,5,6,8,0,5,9,8]

a = (first_list.count(0))

first_list = [x for x in first_list if x!=0] + [0] * a

print(first_list)


























