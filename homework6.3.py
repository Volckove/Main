

number = int(input("Enter:"))
def function_main(n):
  def function(number):
    product = 1
    while number > 0:
        product *= number % 10
        number //= 10
    return product
  while n > 9:
     n = function(n)
  return n

result = function_main(number)
print(result)









