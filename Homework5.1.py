
import keyword

name = input("Enter:")

def variable(name):

    if '0' <= name[0] <= '9':
        return False

    for find in name:
        if not (find.islower() or '0' <= find <= '9' or find == '_'):
            return False


    if name in keyword.kwlist:
        return False


    if name.count('_') > 1:
        return False

    return True

print(variable(name))

































