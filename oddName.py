__author__ = 'Cue'
is_valid = False
while not is_valid:
    name = input('Enter your name:')
    if name.isspace() or name == '':
        print('Error!')
    else:
        is_valid = True
print(name)