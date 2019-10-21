#cteated by ahmad on 11-06-2019
name = input("Enter a message  :")
def a():
   for r in range(9):
     print("")
     for c in range(6):
        if (r==0 and 0<c<5) or (r==4) or (c==0 and 8>r>0) or (c==5 and 8>r>0):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def b():
    for r in range(9):
      print("")
      for c in range(6):
        if (r==0 and c!=5) or (r==3 and c<5) or (c==0 and r<7) or (c==5 and (0<r<7 ) and r!=3) or (r==7 and c<5):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def c():
    for r in range(9):
      print("")
      for c in range(6):
        if (r==0 and 0<c<5) or (r==7 and 0<c<5) or (c==0 and 0<r<7) or(c==5 and (0<r<7 and (r==6 or r==1))):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def d():
    for r in range(9):
      print("")
      for c in range(6):
        if (r==0 and c!=5) or (c==0 and r<7) or (c==5 and 0<r<7) or (r==7 and c<5):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print("")
def e():
    for r in range(10):
      print("")
      for c in range(6):
        if (r==4 or r==4) or (c==0 and r<9)or (r==0 and r<9) or r==8:
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def f():
    for r in range(10):
      print("")
      for c in range(6):
        if (r==4) or (c==0 and r<9)or (r==0):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def g():
    for r in range(9):
      print("")
      for c in range(6):
        if (r==0 and 0<c<5) or (r==7 and 0<c<5) or (c==0 and 0<r<7) or(c==5 and (0<r<7 and (r==6 or r==1 or r==5 ))) or (r==5 and c>2):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def h():
   for r in range(9):
      print("")
      for c in range(6):
        if (r==4) or (c==0 and r<8) or (c==5 and r<8):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def i():
    for r in range(9):
      print("")
      for c in range(5):
        if (r==0) or (r==7) or (c==2 and r<8):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def j():
     for r in range(9):
      print("")
      for c in range(6):
        if (r==0 and c<5) or (r==7 and 0<c<2) or (c==2 and (r<7)) or (c==0 and r==6):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def k():
    for r in range(9):
      print("")
      for c in range(6):
        if (c==0 and r<8) or r+c==5 or (r-c==2 and c>1):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def l():
    for r in range(9):
      print("")
      for c in range(6):
        if (c==0 and r<8) or r==7:
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def m():
    for r in range(9):
      print("")
      for c in range(6):
        if (c==5 and r<8) or (c==0 and r<8) or (r==c and r<3) or(r+c+1==6 and r<3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
#print()
def n():
    for r in range(10):
      print("")
      for c in range(6):
        if (c==0 and r<9) or (c==4 and r<9) or r-c+1==c+1:
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def o():
    for r in range(9):
      print("")
      for c in range(6):
        if (r==0 and 0<c<5) or (r==7 and 0<c<5) or (c==0 and 0<r<7) or (c==5 and 0<r<7):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def p():
    for r in range(10):
      print("")
      for c in range(6):
        if (r==4 and c<5) or (c==0 and r<9)or (r==0 and c<5) or (c==5 and 0<r<4):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def q():
    for r in range(10):
      print("")
      for c in range(6):
        if (r==0 and 0<c<5) or (r==7 and 0<c<5) or (c==0 and 0<r<7) or (c==5 and 0<r<7) or (r-c==3 and c>2):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def r():
    for r in range(10):
      print("")
      for c in range(6):
        if (r==4 and c<5) or (c==0 and r<9)or (r==0 and c<5) or (c==5 and 0<r<4)or r-c==3:
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def s():
    for r in range(10):
      print("")
      for c in range(6):
        if (r==0 and 0<c<5) or (r==8 and 0<c<5) or (c==0 and 0<r<4) or(c==5 and 4<r<8)or (r==4 and 0<c<5) or (r==1 and c==5)or (r==7 and c==0):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def t():
    for r in range(9):
      print("")
      for c in range(7):
        if (r==0) or (c==3 and r<8):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def u():
    for r in range(9):
      print("")
      for c in range(6):
        if (r==7 and 0<c<5) or (c==0 and r<7) or (c==5 and r<7):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def v():
    for r in range(9):
      print("")
      for c in range(7):
        if (c==0 and r<5)or(c==6 and r<5) or (r-c==4 and r<8) or (r+c==10 and r<8):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def w():
    for r in range(9):
      print("")
      for c in range(6):
        if (c==5 and r<8) or (c==0 and r<8)or (r+c==7 and r>4)or (r-c==2 and r>4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
#print()
def x():
    for r in range(10):
      print("")
      for c in range(5):
        if r-c==2 or r+c==6 or (c==0 and (3>r or 9>r>6) ) or (c==4 and (3>r or 9>r>6)):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def y():
    for r in range(9):
      print("")
      for c in range(5):
        if (r==0 and (c==0 or c==4)) or (r-c==1 and r<4) or (r+c==5 and r<3) or (c==2 and 8>r>3):
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def z():
    for r in range(8):
      print("")
      for c in range(5):
        if r==0 or r==6 or r+c==5:
            print("* ",end="")
        else:
            print(" ",end=" ")
#print()
def L0():
   for r in range(8):
     print("")
     for c in range(7):
        if (r==0 and 0<c<6 and c!=3) or (r==1 and c==3) or (r==4 and (c==5 or c==1)) or   (c==0 and 4>r>0) or (c==6 and 4>r>0) or (r==5 and (c==4 or c==2)) or (r==6 and (c==3)) :
            print("* ",end="")
        else:
            print(" ",end=" ")
            
def space():
 #   for r in range(5):
      print("")
      
      print('    *    ')
      print('*  ***  *')
      print(' ******* ')
      print('  *****  ')
      print(' *** *** ')
      print('*       *')
      #for c in range(6):
      #   if r<4:
       #     print("# ",end="")
#print()
def default():
    print("invalid")
#h()
#i()
#space()
for index in range(len(name)):
    if name[index]=="a" or name[index]=="A":
        a()
    elif name[index]=="b" or name[index]=="B":
        b()
    elif name[index]=="c" or name[index]=="C":
        c()
    elif name[index]=="d" or name[index]=="D":
        d()
    elif name[index]=="e" or name[index]=="E":
        e()
    elif name[index]=="f" or name[index]=="F":
        f()
    elif name[index]=="g" or name[index]=="G":
        g()
    elif name[index]=="h" or name[index]=="H":
        h()
    elif name[index]=="i" or name[index]=="I":
        i()
    elif name[index]=="j" or name[index]=="J":
        j()
    elif name[index]=="k" or name[index]=="K":
        k()
    elif name[index]=="l" or name[index]=="L":
        l()
    elif name[index]=="m" or name[index]=="M":
        m()
    elif name[index]=="n" or name[index]=="N":
        n()
    elif name[index]=="o" or name[index]=="O":
        o()
    elif name[index]=="p" or name[index]=="P":
        p()
    elif name[index]=="q" or name[index]=="Q":
        q()
    elif name[index]=="r" or name[index]=="R":
        r()
    elif name[index]=="s" or name[index]=="S":
        s()
    elif name[index]=="t" or name[index]=="T":
        t()
    elif name[index]=="u" or name[index]=="U":
        u()
    elif name[index]=="v" or name[index]=="V":
        v()
    elif name[index]=="w" or name[index]=="W":
        w()
    elif name[index]=="x" or name[index]=="X":
        x()
    elif name[index]=="y" or name[index]=="Y":
        y()
    elif name[index]=="z" or name[index]=="Z":
        z()
    elif name[ index]=="•":
    	L0()
    elif name[index]==" ":
        space()
    else:
        default()
    index+=1