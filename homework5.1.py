import keyword

name = input("Enter:")

def variable(name):

    if '0' <= name[0] <= '9':
        return False
    underscore = 0
    for find in name:
        if not (find.islower() or '0' <= find <= '9' or find == '_'):
            return False
        if find == '_':
            underscore += 1
            if underscore > 1:
              return False
        else:
            underscore = 0

    if name in keyword.kwlist:
        return False

    return True

print(variable(name))


