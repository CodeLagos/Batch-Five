print('KUYE MONSURU ADEWALE')
print('kuye365@gmail.com\n\n')
def decor(func):
    def wrap():
        print('***************************************************')
        func()
        print('***************************************************')
    return wrap


@decor
def decorated():
    print('\t\t THIS IS A DICTIONARY')

decorated()

print('\n\n')
data= open('dictio.txt')
data.readline()
word= input('please enter a word\n')
word=word[0].upper()+word[1:]
for item in data:
    try:
        (query,answer)= item.split('......',1)
        if word in query:
            print(query,':', answer)
    except:
        pass
