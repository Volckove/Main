
import string

a = str(input("Enter:"))
def function(str_input):
    first_letter,second_letter = str_input.split('-')
    result = string.ascii_letters[string.ascii_letters.index(first_letter):string.ascii_letters.index(second_letter) +1]
    return result

print(function(a))
