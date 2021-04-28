import RioDatas as RD

def Go():
	try:
		startPoint = int(input("vortex eq gtnvum : "))
		finishPoint = input("vortex eq gnum : ")
		for finish in RD.pointsInFrontOfShops:
			finishPoints = RD.pointsInFrontOfShops[finish]
			if len(finishPoint) == 0:
				raise Exception
	except:
		print("tvov nsheq vortex eq gtnvum, greq xanuti anun@ te vortex petq e gnaq")
		Go()
	

