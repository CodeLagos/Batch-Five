while True:
    s = int(input('Make a selection: \n (1) mm - cm   (2) mm - m   (3) mm - km \n (4) cm - mm   (5) cm - m   (6) cm - km \n (7) m - mm   (8) m - cm   (9) m - km \n (10) km - mm   (11) km - cm   (12) km - m \n'))
    if s ==1:
        v = float(input('Enter value in mm:'))
        nv = v/10
        print(str(v) + 'mm','=',str(nv) + 'cm.')
    elif s == 2:
        v = float(input('Enter value in mm:'))
        nv = v/1000
        print(str(v) + 'mm', '=',str(nv) + 'm.')
    elif s == 3:
        v = float(input('Enter value in mm:'))
        nv = v/1000000
        print(str(v) + 'mm','=',str(nv) + 'km.')
    elif s == 4:
        v = float(input('Enter value in cm:'))
        nv = v*10
        print(str(v) + 'cm','=',str(nv) + 'mm.')
    elif s == 5:
        v = float(input('Enter value in cm:'))
        nv = v/100
        print(str(v) + 'cm','=',str(nv) + 'm.')
    elif s == 6:
        v = float(input('Enter value in cm:'))
        nv = v/100000
        print(str(v) + 'cm','=',str(nv) + 'km.')
    elif s == 7:
        v = float(input('Enter value in m:'))
        nv = v*1000
        print(str(v) + 'm','=',str(nv) + 'mm.')
    elif s == 8:
        v = float(input('Enter value in m:'))
        nv = v*100
        print(str(v) + 'm','=',str(nv) + 'cm.')
    elif s == 9:
        v = float(input('Enter value in m:'))
        nv = v/1000
        print(str(v) + 'm','=',str(nv) + 'km.')
    elif s == 10:
        v = float(input('Enter value in km:'))
        nv = v*1000000
        print(str(v) + 'km','=',str(nv) + 'mm.')
    elif s == 11:
        v = float(input('Enter value in km:'))
        nv = v*100000
        print(str(v) + 'km','=',str(nv) + 'cm.')
    elif s == 12:
        v = float(input('Enter value in km:'))
        nv = v*1000
        print(str(v) + 'km','=',str(nv) + 'm.')    
    Answer = input('Do you want to perform another calculation? Yes or No?')
    if Answer == 'Yes':
        continue
    else:
        print('Exit')
#Contact me : ohinzama@gmail.com, 08088867332

              
