
while True:
 a = int(input("First number:"))
 c = (input("perform an action:"))
 b = int(input("Second number:"))


 if c == '+':
    result = a+b
    print(result)
 if c == '-':
    result2 = a-b
    print(result2)
 if c == '*':
    result3 = a*b
    print(result3)
 if c == '/' and b == 0:
    print("cannot be divided by 0")
 if c == '/' and b != 0:
    result4 = a/b
    print(result4)
 d = input("Do you want again?:")
 if d != "yes" and d != "y":
  break
