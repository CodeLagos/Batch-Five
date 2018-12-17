birthdays = {'Toyosi': 'Apr 22', 'Simi': 'Oct 29', 'Taiwo': 'Apr 18', 'Deji': 'Jun 4',}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')



"""PROJECT BY OLISA SODIQ IBIKUNLE
leoskillz@gmail.com
08102038772"""
