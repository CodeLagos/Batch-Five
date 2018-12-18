# LANGUAGE TRANSLATOR FOR NIGERIAN LANGUAGES
# #Translator can be extended to cover more languages
# Word register in register.txt file will be updated regularly
# Author: Adekunle Oluwabunmi
# Program: CodeLagos Afternoon Session - Ikeja Sectariat Centre

word = input("Enter (d) to Exit or a word to translate: ").lower()
searchfile = open('register.txt')
for line in searchfile:
    if word in line:
        x = line.rstrip()
searchfile.close()

########################################################
# Following Code is exception handling if supplied word#
# is not in dictionary                                 #
########################################################
try:
    x = x
#    break
except NameError:
    print("Oops!", word.upper(), "is not in my \
register. Try another word...")
    exit()
##########################################################

w = x.split(', ')


def english():
    print(word.upper(), "is in ENGLISH Language ")
    language = input("Select Language to translate \n(a) Yoruba \n(b) Igbo \n(c) Hausa \n(d) Exit \n Enter Option: ")
    if language == 'a':
        print('Yoruba Translation for', word.upper(), 'is', w[1].upper())
    elif language == 'b':
        print('Igbo Translation for', word.upper(), 'is', w[2].upper())
    elif language == 'c':
        print('Hausa Translation for', word.upper(), 'is', w[3].upper())


def yoruba():
    print(word.upper(), "is in YORUBA Language ")
    language = input("Select Language to translate \n(a) English \n(b) Igbo \n(c) Hausa \n(d) Exit \n Enter Option: ")
    if language == 'a':
        print('English Translation for', word.upper(), 'is', w[0].upper())
    elif language == 'b':
        print('Igbo Translation for', word.upper(), 'is', w[2].upper())
    elif language == 'c':
        print('Hausa Translation for', word.upper(), 'is', w[3].upper())


def igbo():
    print(word.upper(), "is in IGBO Language ")
    language = input("Select Language to translate \n(a) English \n(b) Yoruba \n(c) Hausa \n(d) Exit \n Enter Option: ")
    if language == 'a':
        print('English Translation for', word.upper(), 'is', w[0].upper())
    elif language == 'b':
        print('Yoruba Translation for', word.upper(), 'is', w[1].upper())
    elif language == 'c':
        print('Hausa Translation for', word.upper(), 'is', w[3].upper())


def hausa():
    print(word.upper(), "is in HAUSA Language ")
    language = input("Select Language to translate \n(a) English \n(b) Igbo \n(c) Yoruba \n(d) Exit \n Enter Option: ")
    if language == 'a':
        print('English Translation for', word.upper(), 'is', w[0].upper())
    elif language == 'b':
        print('Igbo Translation for', word.upper(), 'is', w[2].upper())
    elif language == 'c':
        print('Yoruba Translation for', word.upper(), 'is', w[1].upper())


if word == w[0]:
    english()
if word == w[1]:
    yoruba()
if word == w[2]:
    igbo()
if word == w[3]:
    hausa()
