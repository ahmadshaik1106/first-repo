def growing_plant(upSpeed, downSpeed, desiredHeight):
    us=upSpeed
    ds=downSpeed
    dh=desiredHeight
    s=0
    i=1
    print(dh)
    while  True:
    	s+=us
    	print('After day ',i,' --> ',s)
    	s-=ds
    	if s>=dh-1:	break
    	print('After night',i,' --> ',s)
    	i+=1
growing_plant(10,1,91)
    	