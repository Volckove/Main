while True:
 user_input = input('Ввести 4-х значне число:')
 number = int(user_input)
 if len(user_input) == 4:
    print('Введено правильно')
    break
 else:
  print('Номер 4-х значний не вказан. Спробуйте ще раз')

left, right = divmod(number, 1000)
print(left)

left, right = divmod(right, 100)
print(left)

left, right = divmod(right, 10)
print(left)

left, right = divmod(right, 1)
print(left)












