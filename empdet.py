def sal(salary):
	salary=salary
	tot=0
	for i in range(years):
		print("The salary of employee per month in year {} is {}".format(i+1,salary))
		tot+=salary*12	
		salary+=inc
	if cut_off=="y" or cut_off=="Y":
		print("{} - {}".format(tot,coa))
		tot-=coa
	print ("The total amount paid to this employee is {}".format(tot))
	
salary=int(input("Enter starting salary of an employee : "))
inc=int(input('Enter increment amout per year       : '))
years=int(input("Enter no.of years to find :          : "))
cut_off=input("Any cut off  (y/n)?                  : ")
if cut_off =="y" or cut_off=="Y":
	coa=int(input("Enter cutoff amount                  : "))
sal(salary)
