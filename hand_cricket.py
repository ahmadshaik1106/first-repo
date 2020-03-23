#created by ahmad on 13-mar-2020
#last modified on 23-mar-2020
def oddOrEven(a):
    a=int(a)
    if a%2==0:
        return "Even"
    else:
        return "Odd"
 
def invalid():
	print(' '*10,'(input must be less than 7 and greater than 0)')

import os    
from numpy import random as r
from pyfiglet import Figlet
import getpass

def playagain():
	heading=Figlet(font="standard")
	print(heading.renderText("HAND CRICKET"))  
	print('-'*67)
	
	while True:
		one_or_2=input('''1 --» one player 
2 --» two players 
                  ''')
		if one_or_2=='1' or one_or_2=='2':
			one_or_2=int(one_or_2)
			break
		print('Invalid Input')
		
		

	p1=input("Enter name of Player 1 (optional) : ").strip()
	if one_or_2==1:
		p2='computer'
	else:
		p2=input("Enter name of Player 2 (optional) : ").strip()

	if p1=='':
		p1='player 1'
	if p2=='':
		p2='player 2'
	p1,p2=p1.upper(),p2.upper()
	print()
	print("Player 1 : ",p1)
	print("Player 2 : ",p2)
	toss=r.randint(0,2)
	print()
	if toss==0:
	    print(p1)
	    while True:
	    	ask=(input('      select 1 --» odd , 2 --» even >> '))
	    	if ask=='1' or ask=='2':
	    		break
	    	else:
	    		print('Invalid input\nYou can choose 1 or 2')
	    ore=oddOrEven(ask)
	    plr=p1
	    plr0=p2
	    print(plr," selected ",ore)
	else:
   	 print(p2)
   	 while True:
   	 	if one_or_2==1:
   	 		ask=r.randint(0,2)
   	 		break
	    	ask=(input('     select 1 --» odd , 2 --» even >> '))
	    	if ask=='1' or ask=='2':
	    		break
	    	else:
	    		print('Invalid input\nYou can choose 1 or 2')
   	 ore=oddOrEven(ask)
   	 plr=p2
   	 plr0=p1
   	 print(plr," selected ",ore)
	print()
	plrcon=oddOrEven(ask)
	while True:
		p1ask=str(getpass.getpass(prompt="{} enter a number from 1 to 6 : ".format(p1.upper())))
		try:
			p1ask=int(p1ask)
			if p1ask>0 and p1ask<7:
				print()
				break
		except:
				pass
	while True:
		if one_or_2==1:
			p2ask=r.randint(1,7)
			print(p2,'entered',p2ask,'\n')
			break
		p2ask=getpass.getpass(prompt="{} enter a number from 1 to 6 : ".format(p2.upper()))
	
		try:
			p2ask=int(p2ask)
			if p2ask>0 and p2ask<7:
				print()
				break
		except:
				pass
		
	
	asksum=int(p1ask)+int(p2ask)
	print(p1ask,'+',p2ask,'=',asksum,'\n')
	c2=oddOrEven(asksum)
	condition=(plrcon==c2)
	if condition:
		print(plr)
		while True:
			if plr=='COMPUTER':
				bob=r.randint(1,3)
				break
			bob=int(input('     select 1 --» Batting , 2 --» Bowling >> '))
			if bob==1 or bob==2:
				break
			else:
				print('Invalid input\nYou can choose 1 or 2')
		
	else:
		print(plr0)
		plr=plr0
		while True:
			if plr=='COMPUTER':
				bob=r.randint(1,3)
				break
			bob=int(input('     select 1 --» Batting , 2 --» Bowling >> '))
			if bob==1 or bob==2:
				break
			else:
				print('Invalid input\nYou can choose 1 or 2')
		
	if bob==1:
		b="Batting"
	else:
		b="Bowling"
	pl1=plr
	if plr==p2:
		pl2=p1
	else:
		pl2=p2
	print(pl1,' selected ',b)
	print(p2)
	print('pl1 ',pl1)
	global computer_status
	computer_status='blank'

	if pl1==p1 and one_or_2==1:
		computer_status='Bowling'
	else:
		computer_status='Batting'
	#elif pl1!=p1 and one_or_2==1:
	if one_or_2==1 and bob==2:
		computer_status='Batting'
	print(computer_status)
	def game(p1,p2,s=None):
		global computer_status
		print('-'*67)
		print(' '*15,"    --:{} Batting :--    ".format(p1.upper()),'\n')
		score=0
		hat_trick=[]
		while 1:
			while 1:
				#print(computer_status)
				if computer_status=='Batting':
					x=r.randint(1,7)
					print(p1,'entered the number')
					#print(x)
				elif computer_status!='Batting':
					while 1:
						x=(getpass.getpass(prompt='{} enter a number : '.format(p1.upper())))
						try:
							x=int(x)
							break
						except:
							pass
					
						
				if computer_status=='Bowling':
					y=r.randint(1,7)
					print(p2,'entered the number')
				elif computer_status!='Bowling':
					while 1:
						y=(getpass.getpass(prompt='{} enter a number : '.format(p2.upper())))
						try:
							y=int(y)
							break
						except:
							pass
				print('    {} -» {}'.format(p1,x))
				print('    {} -» {}'.format(p2,y))
				hat_trick.append(x)
				if len(hat_trick)>3:
					hat_trick=hat_trick[-3:]
				try:
					if hat_trick[0]==hat_trick[1] and hat_trick[1]==hat_trick[2]:
						if hat_trick[0]==4 or hat_trick[0]==6:
							print(' '*30,'HAT-TRICK')
							hat_trick=[]
				except:
					pass
				
				if 0<x<7 and 0<y<7:
					break
				if (x==0 or x>6) and (y==0 or y>6):
					print(' '*30,'NO BALL AND NO SCORE')
					invalid()
				elif x==0 or x>6:
					print(' '*30,'NO SCORE')
					invalid()
				elif y==0 or y>6:
					print(' '*30,'NO BALL')
					invalid()
					score+=x
				
			if x==y :
				print('\n SCORE OF {} IS {}'.format(p1,score))
				
				if computer_status=='Batting':
					computer_status='Bowling'
					hat_trick=[]
					break
				elif computer_status=='Bowling':
					computer_status='Batting'
					hat_trick=[]
					break
				if computer_status=='blank':
					print('-'*67)
					break
					
			score+=x
			if s!=None:
				s=int(s)
				if s<score:
					print('\n SCORE OF {} IS {}'.format(p1.upper(),score))
					print('-'*67)
					break
			print('score of {} is {}'.format(p1.upper(),score))
			
		return score
	def winner(s1,s2,pl1,pl2):
		if s1>s2:
			print(f'\n{pl1} wins\n')
		elif s2>s1:
			print(f'\n {pl2} wins \n')
		else:
			print('\n Draw match\n')
	if b=="Batting":
		s1=game(pl1,pl2)
		s2=game(pl2,pl1,s1)
		winner(s1,s2,pl1,pl2)
	else:
		s1=game(pl2,pl1)
		s2=game(pl1,pl2,s1)
		winner(s1,s2,pl2,pl1)
		
c="y"
while True:
	if c=="y" or c=="Y":
		os.system('clear')
		playagain()
	elif c=='n' or c== "N":
		break
	else:
		print('Invalid input  !!!     \n')
	c=input('Do you want to continue (y/n) ?:')
	if c=='y' or c=='Y':
		os.system('clear')
	if c=='n' or c=='N':
		exit()
