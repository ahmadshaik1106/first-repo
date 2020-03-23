#created by ahmad on 27-feb-2020
#last modified on 23-mar-2020
# for pydroid preferable console font size is 16
import time
import os

from pyfiglet import Figlet
#==================================
class Figlt:
	def fig():
		f = Figlet(font='bubble')
		print('\033[36m' )
		print (f.renderText('TIC TAC TOE'))
		print('''-----------------------------------------
      	      Player 1 : X
              Player 2 : O
-----------------------------------------''');print('\033[37m' )

#===================================
class Clr:
	def clear():
		try:
			os.system('clear')
		except:
			os.system('cls')
#===================================
class Invld:
	def invalid():
		print('\033[31m' +'  \n        Invalid input!  '+'\033[37m' )
		print('only 1 to 9 numbers are allowed\n')
#===================================
Clr.clear()
def tic_tac_toe():	
	def r(q1):
		global k
		global k_indices
		k_indices=[]
		k=[]
		
		for i in range(3):
			for j in range(3):
				if i==q1:
					k.append(l[i][j])
					k_indices.append([i,j])
		return k
#===================================
	def cl(q1):
		global k
		global k_indices
		k_indices=[]
		k=[]
		for i in range(3):
			for j in range(3):
				if j==q1:
					k.append(l[i][j])
					k_indices.append([i,j])
		return k	#===================================
	def dg1():
		global k
		global k_indices
		k_indices=[]
		k=[]
		for i in range(3):
			for j in range(3):
				if j==i:
					k.append(l[i][j])
					k_indices.append([i,j])
		return k
#===================================
	def dg2():
		global k
		global k_indices
		k_indices=[]
		k=[]
		for i in range(3):
			for j in range(3):
				if j+i==2:
					k.append(l[i][j])
					k_indices.append([i,j])
		return k
#===================================
	def req(q1):
		global bl
		if q1[0]==q1[1] and q1[1]==q1[2] and q1[0]!='-':
			l[k_indices[0][0]][k_indices[0][1]]='\033[32m'+l[k_indices[0][0]][k_indices[0][1]]+'\033[37m'
			l[k_indices[1][0]][k_indices[1][1]]='\033[32m'+l[k_indices[1][0]][k_indices[1][1]]+'\033[37m'
			l[k_indices[2][0]][k_indices[2][1]]='\033[32m'+l[k_indices[2][0]][k_indices[2][1]]+'\033[37m'
			
			
			Clr.clear()
			Figlt.fig()

			for i in range(3):		
				print('\t\t\t',end='')
				for j in range(3):		
					print(l[i][j],end=' ')
				print()
							
			if q1[0]=='X':
				print('\n\t   \033[32m       ---:PLAYER 1 WINS:--- \033[37m')
			else:
				print('\n\t   \033[32m       ---:PLAYER 2 WINS:--- \033[37m')
			return '1'
#===================================
	def notmt(e):
		print("\033[33m {} was already filled \033[37m ".format(str(loc)))
#===================================
	def display():
		for e in l:
			print('\t\t\t',end='')
			for i in range(1,4):
				print(e[i-1],end=' ')
				if i%3==0:
					print()
#===================================
	Figlt.fig()	
	l=[['-','-','-'],['-','-','-'],['-','-','-']]
	ki=0
	display()		
	while 1:
		global bl	
		bl=[]
		count=0
		if ki%2==0:
			c='X'
			loc=(input('\n\033[36mPlayer 1 : '))
			print(('\033[37m' ))
			try:
				loc = int(loc)
			except:
				pass
		else:
			c='O'
			loc=(input('\n\033[36mPlayer 2 : '))
			print(('\033[37m' ))
			try:
				loc =int(loc)
			except:
				pass
		Clr.clear()
		filled=False
		if isinstance(loc,int) and 0<loc<10:
			Figlt.fig()
			if loc < 10:
				num=1
				for i in range(3):
					for j in range(3):
						if loc == num:
							if l[i][j]=='-':
								l[i][j]=c
							else:
								ki-=1
								filled=True
						num+=1
			else:
				ki-=1
			for i in range(3):		
				print('\t\t\t',end='')
				for j in range(3):		
					print(l[i][j],end=' ')
				print()
			
			r1=req(r(0))
			r2=req(r(1))
			r3=req(r(2))

			c1=req(cl(0))
			c2=req(cl(1))
			c3=req(cl(2))
	
			d1=req(dg1())
			d2=req(dg2())
			
			if filled:
				notmt(loc)
				filled=False
	
			if r1 =='1' or r2=='1' or r3=='1' or c1=='1' or c2=='1' or c3=='1' or d1=='1' or d2=='1':
				break
			for i in range(3):
				for j in range(3):
					if l[i][j]=='-':
						count+=1
			if count==0:
				print('\n\t  \033[35m          ---:TIE:--- \033[37m')
				break
			ki=ki+1	
		else:
			Figlt.fig()
			display()
			Invld.invalid()
			pass
c="y"
while True:
		if c=="y" or c=="Y":
			tic_tac_toe()
		elif c=='n' or c== "N":
			
			break
		else:
			Figlt.fig()
			Invld.invalid()
		print()
		c=input('Play Again (y/n) ?:')
		Clr.clear()
		if c=='n' or c=='N':
			f = Figlet(font='bubble')
			print('\033[36m' )
			print (f.renderText('TIC TAC TOE'))
			print('\033[37m' )
			print()
			print('\033[36m' )
			print(f.renderText('   THANK YOU'))
			print('\033[37m' )
			time.sleep(2)
			Clr.clear()
		print()


