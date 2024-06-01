first_list = [1,2,3,4,5,6,7,9]

a = first_list
if (len(a) > 2) and (len(a) < 11):
  x = a[0]
  y = a[2]
  z = a[-2]

  second_list = [x,y,z]
  print(second_list)