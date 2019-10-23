for r in range(7):
     print("")
     for c in range(7):
        if (r==0 and 0<c<6 and c!=3) or (r==1 and(c==0 or c==6 or c==3)) or (r==2 and(c==0 or c==6) )or (r==3 and(c==1 or c==5)) or (r==4 and(c==2 or c==4) or (r==5 and(c==3 )) ):
            print("* ",end="")
        else:
            print(" ",end=" ")