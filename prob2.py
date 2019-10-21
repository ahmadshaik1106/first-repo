p=int(input('principle amount = '))
i=float(input('interest = '))
i=i/100
k=int(input('constant amount = '))
print('-----------------------------------------')
pi=p*(i)
ki=pi
c=0
while True: 
	if c%3==0 and c>0:
		p=p-3*(k+l)
		print()
	if p<0:
		break
	pi=p*i
	l=ki-pi
	print('   ',c+1,'»',int(p),'   ',int(pi),'    ',int(k+l)) #int(k) ,'+',int(l),'=',int(k+l))
#	print(round(p,2),'   ',round(pi,2),'    ',round(k,2) ,'+',round(l,2),'=',round(k+l,2))
	#print('       ',l)

	c+=1
#while True:
#	pass