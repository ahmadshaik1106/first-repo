#created by ahmad on 17-07-2019
from decimal import Decimal
def callIt():
    num = Decimal(input("Enter the number with base 10 :"))
    base=int(input("Enter the base to be converted :"))

    Ipart=int(num)
    Dpart=Decimal(num-Ipart)
    strDpart=str(Dpart)
    print(strDpart)
    Ilist=[]
    Dlist=[]
    print("digits before . (dot) is {} ".format(Ipart))
    if strDpart=="0":
        print("digits after . (dot) is 0")
    else:
        print("digits after . (dot) is  {}".format(strDpart[2:]))#base+2
    print(" --------------------------------------------------")
    print("|                 INTEGRAL PART                    |")
    print(" --------------------------------------------------")
    print("  {}|_{}".format(base, Ipart))
    while num>=base:
        rem = int(num % base)
        srem = str(rem)
        num = int(num/base)
        Ilist.append(rem)
        if num<=base:
            Ilist.append(num)
        if num>=base:             #   32964.4769
            print( "  {}|_".format(base)+str(num)+"    --->{}".format(srem))
        else:
            print("     "+str(num)+"    --->{}".format(srem))
            print("-----------------------------------------------------------")
    print(" --------------------------------------------------")
    print("|                  DECIMAL PART                    |")
    print(" --------------------------------------------------")
    k=0
    while k < (len(strDpart)-2)*2:
        print("{} x {} = ".format(Dpart,base),end='')
        a = Dpart * base
        Dpart = a - int(a)
        print(a)
        a1 = int(a)
        Dlist.append(a1)
        k = k + 1
    #     boom=1
    #     if boom == 1:
    #         print("{} x {} = ".format(Dpart, base), a)
    #
    #
    #     else:
    #         print("{} x {} = ".format(kpart,base),a)
    #     a1=int(a)
    #     Dlist.append(a1)
    #     k = k + 1
    # boom = 2
    print(" --------------------------------------------------")
    print("integer part:")
    print(Ilist[::-1])
    print("decimal part:")
    print(Dlist)
    dot=["dot"]
    print("Final Answer = ",Ilist[::-1]+dot+Dlist)
s =1
if s==1:
    callIt()
    s=s+1
while True:
    condition=input("do you want to continue y/n:")
    if condition =="y":
        callIt()
    elif condition=="n":
        quit()
    else:
        print("Invalid input")
