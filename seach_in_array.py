from array import *
a=int(input("Enter the size of array : "))
b=array("i",[])
for i in range(a):
	x=int(input("Enter number at index {}  :  ".format(i)))
	b.append(x)
print("--------------------------------------------------------")
y=int(input("Enter a value to check   :  "))
print("--------------------------------------------------------")
count=0
for i in range(a):
	if b[i]==y:
		print("{} is found at index {} ".format(y,i))
		count=1
		break
if count ==0:
	print("{} is not found".format(y))
print("--------------------------------------------------------")