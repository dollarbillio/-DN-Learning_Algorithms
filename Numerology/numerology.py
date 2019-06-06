# Pythagorean
letter = {'a':1, 'j':1, 's':1, 
          'b':2, 'k':2, 't':2,
          'c':3, 'l':3, 'u':3,
          'd':4, 'm':4, 'v':4,
          'e':5, 'n':5, 'w':5,
          'f':6, 'o':6, 'x':6,
          'g':7, 'p':7, 'y':7,
          'h':8, 'q':8, 'z':8,
          'i':9, 'r':9}

birthday = input ("What is your birthday? >>> ")
name = input ("What is your name? >>> ")

# Main
def numerology(birthday, name):
    ''' Modify name'''
    name = name.lower().replace(' ', '')
    newName = ''
    for i in range(len(name)):
        newName += str (letter[name[i]])
    
    def main_numerology(birthday, newName):
        '''Calculate numbers'''
        if len(birthday) == 1 and len(newName) == 1:
            return (birthday, newName)
        else:
            birthday = str (sum([int(i) for i in birthday]))
            newName = str (sum([int(i) for i in newName]))
            return main_numerology(birthday, newName)
    
    return main_numerology(birthday, newName)

print (numerology(birthday, name))


	

