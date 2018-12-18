#AUTHOR: OSOBA SAMUEL OLUWASEUN
#Mathemagics is a game of cards. Enjoy!

print("Welcome to my project!\n\n\t\tMathemagics!")
menu = input("\n\n\t\t*Menu*\n\tStart Game>>>   (Press 'S' key to start!) \n\tHelp>>> \t(Press H)\n\tAbout>>> \t(Press A)\n\tExit>>> \t(Press E)\n\n")
while True:
    if menu == "S":
        print("\n\nPlease choose a number between 1-31\n(Tell no man. Its a secret!)\n\t\t    (A)\n\t1\t3\t5\t7\n\t9\t11\t13\t15\n\t17\t19\t21\t23\n\t25\t27\t29\t31")
        print("\n\t\t    (B)\n\t2\t3\t6\t7\n\t10\t11\t14\t15\n\t18\t19\t22\t23\n\t26\t27\t30\t31")
        print("\n\t\t    (C)\n\t4\t5\t6\t7\n\t12\t13\t14\t15\n\t20\t21\t22\t23\n\t28\t29\t30\t31")
        print("\n\t\t    (D)\n\t8\t9\t10\t11\n\t12\t13\t14\t15\n\t24\t25\t26\t27\n\t28\t29\t30\t31")
        print("\n\t\t    (E)\n\t16\t17\t18\t19\n\t20\t21\t22\t23\n\t24\t25\t26\t27\n\t28\t29\t30\t31")
        magic_no = input("Enter the containing tables' labels:\n")
        if magic_no == "A":
            print("Mathemagician: 'The number you chose is = 1'")
        elif magic_no == "B":
            print("Mathemagician: 'The number you chose is = 2'")
        elif magic_no == "AB":
            print("Mathemagician: 'The number you chose is = 3'")
        elif magic_no == "C":
            print("Mathemagician: 'The number you chose is = 4'")
        elif magic_no == "AC":
            print("Mathemagician: 'The number you chose is = 5'")
        elif magic_no == "BC":
            print("Mathemagician: 'The number you chose is = 6'")
        elif magic_no == "ABC":
            print("Mathemagician: 'The number you chose is = 7'")
        elif magic_no == "D":
            print("Mathemagician: 'The number you chose is = 8'")
        elif magic_no == "AD":
            print("Mathemagician: 'The number you chose is = 9'")
        elif magic_no == "DB":
            print("Mathemagician: 'The number you chose is = 10'")
        elif magic_no == "ABD":
            print("Mathemagician: 'The number you chose is = 11'")
        elif magic_no == "DC":
            print("Mathemagician: 'The number you chose is = 12'")
        elif magic_no == "ADC":
            print("Mathemagician: 'The number you chose is = 13'")
        elif magic_no == "DBC":
            print("Mathemagician: 'The number you chose is = 14'")
        elif magic_no == "ABCD":
            print("Mathemagician: 'The number you chose is = 15'")
        elif magic_no == "E":
            print("Mathemagician: 'The number you chose is = 16'")
        elif magic_no == "AE":
            print("Mathemagician: 'The number you chose is = 17'")
        elif magic_no == "EB":
            print("Mathemagician: 'The number you chose is = 18'")
        elif magic_no == "ABE":
            print("Mathemagician: 'The number you chose is = 19'")
        elif magic_no == "EC":
            print("Mathemagician: 'The number you chose is = 20'")
        elif magic_no == "AEC":
            print("Mathemagician: 'The number you chose is = 21'")
        elif magic_no == "EBC":
            print("Mathemagician: 'The number you chose is = 22'")
        elif magic_no == "ABCE":
            print("Mathemagician: 'The number you chose is = 23'")
        elif magic_no == "DE":
            print("Mathemagician: 'The number you chose is = 24'")
        elif magic_no == "ADE":
            print("Mathemagician: 'The number you chose is = 25'")
        elif magic_no == "DBE":
            print("Mathemagician: 'The number you chose is = 26'")
        elif magic_no == "ABDE":
            print("Mathemagician: 'The number you chose is = 27'")
        elif magic_no == "EDC":
            print("Mathemagician: 'The number you chose is = 28'")
        elif magic_no == "ADCE":
            print("Mathemagician: 'The number you chose is = 29'")
        elif magic_no == "DBCE":
            print("Mathemagician: 'The number you chose is = 30'")
        elif magic_no == "ABCDE":
            print("Mathemagician: 'The number you chose is = 31'")
        else:
            break

    elif menu == "H":
        print("Mathemagician wants to reveal a secret number. Choose a number between 1-31. There are four tables. Check each table for that number\nNote down the letters of the tables in which you find the number. Input the letters which are - A, B, C, D and E\nand Mathemagician will tell you the number you chose. Pretty simple, right?")
        break
    
    elif menu == "A":
        print("Mathemagician a magic game that reveals any secret number between 1-31.\n\n\t\tWritten by Osoba Samuel Oluwaseun (Code Lagos Final Project)")
        break
    
    elif menu == "E":
        print("Please try it once. Then you can exit manually. Mathemagician is not happy. But one short game will do. Thank you!")
        break
    break
#Written by Osoba Samuel Oluwaseun
