def courseamount():
      print('NAME: RAJI MUSTAPHA ADEMOLA \nPROJECT: GP CALCULATOR \nEMAIL: rajimustapha30@gmail.com \nCONTACT: 08087427344')
      print('')
      print('')
      j=int(input("How many Courses Did You Offer? "))
      gc={"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}
      u=[] 
      g=[]
      s=[]
      for i in range(0,j):
            u.append(int(input("How many unit is course " + str(i+1)+ ": ")))
            g.append(gc[input("What is the Grade? ").upper()])
            s.append((u[i]*g[i]))
      t=sum(u)
      v=sum(s)
      gp=(v/t)
      print("Your GP is ",round(gp,2))

      if gp>=4.50:
          print("YOU ARE ON FIRST CLASS")
          print("COMMENT: KEEP IT UP")
      elif gp>=4.00:
             print("YOU ARE ON SECOND CLASS UPPER")
             print("COMMENT: YOU NEED TO PUT IN A LITTLE BIT OF EFFORT NEXT SEMESTER")
      elif gp>=3.00:
          if gp>=3.50:
              print("YOU ARE ON SECOND CLASS UPPER")
          else:
              print("YOU ARE ON SECOND CLASS LOWER")
              print("COMMENT: THERE IS STILL HOPE WORK HARDER")
      elif gp>=2.00:
          if gp>=2.50:
             print('YOU ARE ON SECOND CLASS LOWER')
          else:
             print("YOU ARE ON THIRD CLASS ")
             print("COMMENT: JUST GO AND LOGDE AT THE LIBRARY AND READ YOUR ASS OUT")
      elif gp>=1.50:
         print("YOU ARE ON THIRD CLASS")
         print("COMMENT: SINCERELY I WILL ADVICE YOU TO WITHDRAW SCHOOLING IS NOT YOUR WAY")
      else: 
            print("COMMMENT: HOW DID YOU EVEN GAIN ADMISSION IN THE FIRST PLACE")
courseamount()
input("press enter")    
