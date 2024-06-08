import string

text = input('Enter any text:')

for check in string.punctuation:
    text = text.replace(check, '')

words = text.split()

n = [word[0].upper() + word[1:].lower() for word in words if len(word) > 0]

hashtag = ''.join(n)

b = '#' + hashtag

if len(b) > 140:
 print(b[:140])
else:
 print(b)