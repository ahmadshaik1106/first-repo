def fun():
	t = int(input("which table ?  : "))
	print()
	for i in range(10):
 	   print('                ',t,' x',i+1,' =',t*(i+1))

	print('---------------------------------------------')		
	print()
c='y'
c="y"
while True:
	if c=="y" or c=="Y":
		fun()
	elif c=='n' or c== "N":
		print('احمد created by')
		break
	else:
		print('Invalid input  !!!     \n')
	c=input('Do you want to continue (y/n) ?:')
	print()