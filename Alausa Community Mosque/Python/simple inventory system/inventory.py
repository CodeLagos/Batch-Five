"""
LOLA'S BOOKSHOP
sells books, and hold
in a bookshop, there will be different aisle for the genres, in lola's bookshop sells 5 genres;novels:romance,children storybooks:Age considering,religious and motivational,relationship,leadership
ask the user what genre of book he wants considering the genres available
in each genre, it will be subdivided into authors, quantity, and price tag
when a book is bought, subtract from the count and save it as the new number of books availabe. when some one else wants to buy, it will recall that the new original value

"""
import main
print("This is Lola's bookshop inventory!")
choice=str(input('Do you want to \na.store \nb.check-in \na book in the inventory? Pick either A/B.'))
if (choice.lower()=="b"):
    author=str(input('Enter the name of the author:'))
    if (author.lower()=='barbara wallace') or (author.lower()=='barbara') or (author.lower()== 'wallace') or (author.lower()=='wallace barbara'):
        print('These are Barbara Wallace books\n',main.BARBARA)
        title=str(input('Enter your title choice:'))
        if (title.lower()=='peppermints in the parlor'):
           price = '500 naira'
           number = '20 copies'
           print('PRICE=',price,'\n',number,'are available')
        else:
            price = '500 naira'
            number = '20 copies'
            print('PRICE=',price,'\n',number,'are available')
    elif (author.lower()=='siobhan vivian') or (author.lower()=='siobhan') or (author.lower()=='vivian') or (author.lower()=='vivian siobhan'):
       print('These are Siobhan Vivian books\n',main.VIVIAN)
       title=str(input('Enter your title choice:'))
       if (title.lower()=='same difference'):
           price = '600 naira'
           number = '10 copies'
           print('PRICE=',price,'\n',number,'are available')
       else:
            price = '600 naira'
            number = '20 copies'
            print('PRICE=',price,'\n',number,'are available')
    elif (author.lower()=='tanya michaels') or (author.lower()=='tanya')or (author.lower()=='michaels') or (author.lower()=='michaels tanya'):
        print('These are Tanya Michaels books\n',main.TANYA)
        title=str(input('Enter your title choice:'))
        if (title.lower()=='mistletoe baby'):
           price = '550 naira'
           number = '15 copies'
           print('PRICE=',price,'\n',number,'are available')
        else:
            price = '500 naira'
            number = '5 copies'
            print('PRICE=',price,'\n',number,'are available')
    else:
        print("This author's book is unavailable")

elif (choice.lower()=="a"):
    author=str(input('Enter the name of the author:'))
    if(author.lower()=="barbara wallace") or (author.lower()=='barbara'):
        count=0
        title=str(input('Enter the title of the novel:'))
        price=int(input('Enter the price allocated for the book:'))
        number=int(input('How many copies are being stored:'))
        count=count+number
        print('The book',title,'has',count,'copies. It is being sold for',price,'naira.')
        
    elif(author.lower()=='siobhan vivian') or (author.lower()=='vivian'):
        count=0
        title=str(input('Enter the title of the novel:'))
        price=int(input('Enter the price allocated for the book:'))
        number=int(input('How many copies are being stored:'))
        count=count+number
        print('The book',title,'has',count,'copies. It is being sold for',price,'naira.')

    elif(author.lower()=='tanya michaels') or (author.lower()=='tanya'):
        count=0
        title=str(input('Enter the title of the novel:'))
        price=int(input('Enter the price allocated for the book:'))
        number=int(input('How many copies are being stored:'))
        count=count+number
        print('The book',title,'has',count,'copies. It is being sold for',price,'naira.')

    else:
        print("This author's book is not available")
        new = str(input("Do you want to store this book in the system?\n(Yes/No)\n"))

        if (new.lower()== 'yes'):
            author = str(input("Enter the author's name\n"))
            title = str(input('Enter the title of the book:'))
            price=int(input('Enter the price allocated for the book:'))
            number=int(input('How many copies are being stored:'))
            print('This book has been added to the inventory.')
            #author==[title], this will be added to the main program's database.

        else:
            print('Exit the program.')
else:
    print('Invalid choice')

#end of program
