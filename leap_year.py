#divisible by 4
#do not divisible by 100
#divisible by 4000

date= int(input())

if date%4==0 and date%100!=0 :
	print('leap year')
if  date%400==0:
	print('leap year')