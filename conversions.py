# created by ahmad on 17-07-2019
# last updated on 21-07-2019

from decimal import Decimal
print('''
example:-
Enter a number :20
Enter base of number :4
Enter the base of resulting number :3
--------------------------------------------------------
''')

def fromTen():
    global fin
    fin = num
    nnum = num
    base = base2
    if count == 1:
        nnum = sum(milst) + sum(mdlst)
    Ipart = int(nnum)
    Dpart = Decimal(nnum - Ipart)
    strDpart = str(Dpart)
    Ilist = []
    Dlist = []
    print("digits before . (dot) is {} ".format(Ipart))
    if strDpart == "0":
        print("digits after . (dot) is 0")
    else:
        print("digits after . (dot) is  {}".format(strDpart[2:]))  # base+2
    print(" --------------------------------------------------")
    print("|                 INTEGRAL PART                    |")
    print(" --------------------------------------------------")
    print("  {}|_{}".format(base, Ipart))
    while nnum >= base:
        rem = int(nnum % base)
        srem = str(rem)
        nnum = int(nnum / base)
        Ilist.append(rem)
        if nnum >= base:
            print("  {}|_".format(base) + str(nnum) + "    --->{}".format(srem))
        else:
            print("     " + str(nnum) + "    --->{}".format(srem))
            Ilist.append(nnum)
            print("-----------------------------------------------------------------------")
    IIlist = Ilist
    for i in range(len(IIlist)):
        try:
            a = int(IIlist[i]) + 55
            if a > 64:
                IIlist[i] = chr(a)
        except:
            pass
    print(IIlist)
    print()
    print(Ilist[::-1])
    print()
    print(" --------------------------------------------------")
    print("|                  DECIMAL PART                    |")
    print(" --------------------------------------------------")
    k = 0
    while k < (len(strDpart) - 2) * 2:
        print("{} x {} = ".format(Dpart, base), end='')
        a = Dpart * base
        Dpart = a - int(a)
        print(a)
        a1 = int(a)
        Dlist.append(a1)
        k = k + 1

    print(" --------------------------------------------------")
    print("integer part:")
    print(Ilist[::-1])
    print("decimal part:")
    print(Dlist)
    dot = ["dot"]
    print("Final Answer = ", Ilist[::-1] + dot + Dlist)


########################################################################################################

def toTen():
    mnum = num
    mbase = base1
    global fin
    mdnum = mnum - int(mnum)
    minum = int(mnum)

    strmdnum = str(mdnum)[2:]
    mdlen = len(strmdnum)

    strminum = str(minum)[::-1]
    milen = len(strminum)
    strnum = strmdnum + strminum
    con = 0
    for i in range(len(strnum)):
        a = int(strnum[i])
        if a >= mbase:
            con = con + 1
    if con == 0:
        p = 0
        global milst, mdlst
        milst = []
        mdlst = []
        print(" --------------------------------------------------")
        print("|                 INTEGRAL PART                    |")
        print(" --------------------------------------------------")
        for ii in range(milen):
            minum = int(strminum[ii])
            power1 = pow(mbase, p)
            print("""{} power {} is  "{}" """.format(mbase, p, power1),
                  "    -->    {} x {} = {}".format(power1, minum, minum * power1))
            p = p + 1
            milst.append(minum * power1)
        print("__________________________________________________________________________________")
        print()
        print("ADDITION OF INTEGRAL PART ===>   ", end='')
        for i in range(milen):
            if (i + 1) < (milen):
                print(" {} +".format(milst[i]), end='')
            if i + 1 == milen:
                print("{} = ".format(milst[i]), end='')
        print(sum(milst))
        print()
        print("__________________________________________________________________________________")
        # ----------------------------------------------------------------------------------------------------------------------
        print("-----------------------------------------------------------------------")
        print(" --------------------------------------------------")
        print("|                  DECIMAL PART                    |")
        print(" --------------------------------------------------")
        print()
        mbase = Decimal(mbase)
        print("-----------------------------------------------------------------------------------------")
        for jj in range(mdlen):
            q = Decimal(pow(mbase, -(jj + 1)))
            print("{} power {}  = {}   --->        ".format(mbase, -(jj + 1), q))  # ,end='')
            print("                                     ", strmdnum[jj], "  x  ", q, "  =  ", q * int(strmdnum[jj]))
            mdlst.append(float(q * int(strmdnum[jj])))
            print("-----------------------------------------------------------------------------------------")
        print(sum(mdlst))
        print("__________________________________________________________________________________")
        print()
        print("ADDITION OF DECIMAL PART ===>   ", end='')
        for i in range(mdlen):
            if (i + 1) < (mdlen):
                print(" {} +".format(mdlst[i]), end='')
            if i + 1 == mdlen:
                print("{} = ".format(mdlst[i]), end='')
        print(sum(mdlst))
        print("__________________________________________________________________________________")
        print()
        print("********************************************************************************")
        print("FINAL ANSWER ===> {} + {} = ".format(sum(milst), sum(mdlst)), sum(milst) + sum(mdlst))
        print("********************************************************************************")
    else:
        print("--------------------------------------------------------------------------")
        print("               ---------------------")
        print("              |       INVALID        |")
        print("               ---------------------")
        print()
        print("all the digits should be less than the base ")
        print("The base of {} should not be {}".format(mnum, mbase))


def forBoth():
    toTen()
    global count
    count = 1
    fromTen()


def main():
    global num, base1, base2, count, fin
    count = 0
    num = Decimal(input("Enter a number :"))
    base1 = int(input("Enter base of {} :".format(num)))
    base2 = int(input("Enter the base of resulting number:"))
    if base1 == 10:
        fromTen()
    elif base2 == 10:
        toTen()
    else:
        forBoth()


s = 1
if s == 1:
    main()
    s = s + 1
while True:
    print("\n")
    condition = input("Do you want to continue ?   (y/n):")
    if condition == "y":
        main()
    elif condition == "n":
        print()
        print(
            "<*****************************************<|  PROGRAM TERMINATED  |>*****************************************>")
        quit()
    else:
        print("Invalid input")
