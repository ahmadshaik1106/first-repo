p=int(input('principle amount = '))
i=float(input('interest = '))
i=i/100
k1=int(input('payment per month = '))
h=int(input('principle amount should be reduced in months : '))
print('-----------------------------------------')
pi=p*(i)
ki=pi
c=0

while True:
	
	
	l=k1-p*i
	if c%h==0 and c>0:
		p=p-h*(l)
		print()
	pi=p*i
	l=k1-p*i
	if p<k1:
		break
	print('  ',c+1,'»',int(p),'   ',int(pi),'   ',int(l),'  ',int(pi+l))
	c+=1