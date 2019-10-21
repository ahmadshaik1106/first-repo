def c1(x):
	a=x
	k1=min(a)
	k2=max(a)
	for i in range(len(a)):
		if a[i]==k1:
			a[i]=1
		elif a[i]==k2:
			a[i]=3
		else:
			a[i]=2

a=int(input())
bla,ble=[],[]
for i in range(a):
	l=list(map(int,input().split()))
	lage=l[0:3]
	bla.append(lage)
	leidi=l[3:6]
	ble.append(leidi)

for i in range(a):
	#print(bla[i],"    ",ble[i])
	#for j in range(3):
	lage=bla[i]
	leidi=ble[i]
	c1(lage)
	c1(leidi)
	
	if lage==leidi:
		print("FAIR")
	else:
		print("NOT FAIR")
