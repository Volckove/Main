
first_list = []
if first_list ==[]:
 print(0)

a = []
for i in range(0, len(first_list), 2):
 a.append(first_list[i])

summa = 0
for element in a:
    summa += element

if first_list != []:
 print(summa*(first_list[-1]))


























