nos =int(input("Enter no.of subjects : "))
bl=[]
for i in range(nos):
	a = int(input("Enter marks in subjects {} : ".format(i+1)))
	bl.append(a)
print(((sum(bl))/(len(bl)*100))*100,"%")