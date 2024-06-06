import string

text = input('Enter any text:')

for check in string.punctuation:
    text = text.replace(check,'')
    text = text.replace(' ','')

first_letter = text[0]
c = first_letter.upper()
n = text[1:]

b = '#' + c + n

if len(b) > 140:
 print(b[:140])
else:
 print(b)