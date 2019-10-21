def findNeedle(find_needle):
	lst=find_needle
	for i in range(len(lst)):
		if lst[i]=="needle":
			print("found the needle at position ",i)		
findNeedle(['hay', 'junk', 'hay', 'hay', 'moreJunk','hay', 'needle', 'randomJunk'])
