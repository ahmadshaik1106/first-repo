print('--------ALL COMBINATIONS OF A WORD--------')
print('__________________________________________')

print()
def strdata(str):
	if len(str)==0:
		return['  ']
	prlst=strdata(str[1:len(str)])
	nxtlst=[]
	for i in range(0,len(prlst)):
		for j in range(0,len(str)):
			newstr=prlst[i][0:j]+str[0]+prlst[i][j:len(str)-1]	
			if newstr not in nxtlst:
				nxtlst.append(newstr)
	return nxtlst

strdata

def c(a,lenght=None,firlet=None):
		ln=lenght
		ft=firlet
		bl=[]
		bl.append(a)
		ii=0
		while bl[-1]!='':	
			a=bl[ii]
			for i in range(len(a)):
				l=[]
				for j in range(len(a)):
					if i!=j :
						l.append(a[j])
				el=''.join(l)
				bl.append(el)
			ii+=1
		fl=[]
		for i in range(len(bl)):
			if len(bl[i])!=1 and bl[i]!='':
					fl.append(bl[i])		
		print()		
		k=(bl[0])
		for i in range(len(k)):
			fl.append(k[i])	
		fn1=[]
		for i in range(len(fl)):
			k =fl[i]
			# print(k)
			b=sorted(strdata(k))
			for i in range(len(b)):
				if ln ==None:
					print('     ',b[i])
				elif len(b[i])==ln:
					if ft == None:
						print('     ',b[i])
					elif bl[i][0] == firlet:
						print('     ', b[i])

			
a=input('Enter the letters of word        : ')
a=a.upper()
c1=input("Do you want to enter length ? :")
lengt=None
if c1=="y":
	lengt =int(input('Enter no.of letters in the word  : '))
c(a,lengt)


	