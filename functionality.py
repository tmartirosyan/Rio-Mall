import cv2
from matplotlib import pyplot as plt
import numpy as np
import RioDatas as RD


def imgShow(windowName:str,img):
	cv2.imshow(windowName, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def drawRect(path, coordsXY: tuple, coordsX1Y1: tuple, color: tuple, thickness: int=2):
    cv2.rectangle(path, coordsXY, coordsX1Y1, color, thickness)

def detetctFirstAndLastPoints():
	try:
		startPoint = int(input("vortex eq gtnvum : "))
		finishPoint = input("vortex eq gnum : ")
		finishPoint = finishPoint.upper()
		for shopName in RD.shopsWithCoordinates1Stage.keys():
			if finishPoint == shopName:
				finishPoint = RD.shopsWithCoordinates1Stage[shopName]
				break
	except:
		print("tvov nsheq vortex eq gtnvum, greq xanuti anun@ te vortex petq e gnaq")
		detetctFirstAndLastPoints()
	
	return [RD.pointRectanglesWayFirstStage[startPoint-1][0],
			RD.pointRectanglesWayFirstStage[startPoint-1][1],
			finishPoint]

