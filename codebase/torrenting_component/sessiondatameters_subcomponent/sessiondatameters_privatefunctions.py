import math as Maths


def getneedlemeterdata(datavalue, metermin, metermax, needletype):

	if metermin < -999:
		needleangle = getlogmeterangle(datavalue, metermax)
	else:
		needleangle = getlinmeterangle(datavalue, metermin, metermax)

	decalheight = 68
	decalwidth = 121

	needlepivot = 0.45 #Fraction of decal size the the middle of the needle is missing

	if needletype == "Long":
		needlesize = 0.9
	else:
		needlesize = 0.75

	metersize = 58.0
	verticalorigin = 7.0
	horizontalorigin = decalwidth * 0.5
	needlestart = needlepivot * metersize
	needlefinal = needlesize * metersize
	verticalstart = (needlestart * Maths.sin(needleangle)) + verticalorigin
	horizontalstart = (needlestart * Maths.cos(needleangle)) + horizontalorigin
	verticalfinal = (needlefinal * Maths.sin(needleangle)) + verticalorigin
	horizontalfinal = (needlefinal * Maths.cos(needleangle)) + horizontalorigin

	outcome = {}
	outcome['vo'] = decalheight - verticalstart
	outcome['ho'] = decalwidth - horizontalstart
	outcome['vf'] = decalheight - verticalfinal
	outcome['hf'] = decalwidth - horizontalfinal

	return outcome



def getlogmeterangle(currentval, scale):

	if currentval < 1:
		segment = -1.0
	else:
		segment = scale * Maths.log10(currentval)
		if segment > 7.0:
			segment = 7.0

	outcome = Maths.pi * (segment + 1.0) / 8.0

	return outcome



def getlinmeterangle(currentval, scalemin, scalemax):

	fraction = (currentval - scalemin) / (scalemax - scalemin)

	if fraction < 0.0:
		fraction = 0.0
	if fraction > 1.0:
		fraction = 1.0

	outcome = Maths.pi * fraction

	return outcome



def getblockmeterangle(currentval, anglemax, blocksin180):

	blockanglesize = 180.0 / blocksin180

	blockstart = currentval * blockanglesize

	if blockstart > anglemax:
		blockstart = anglemax

	return blockstart



def getblockmeterdata(counter, metertype):

	endangle = 185.0
	countermax = 9.5

	startangle = getblockmeterangle(counter, endangle, countermax)

	if metertype == "Outer":
		circleradius = 49.5
	else:
		circleradius = 36.5

	circumference = circleradius * Maths.pi * 2.0

	filledangle = (endangle - startangle) / 360.0

	outcome = {}
	outcome['fill'] = filledangle * circumference
	outcome['gap'] = circumference - outcome['fill']
	outcome['offset'] = ((180.0 - startangle) / 360.0) * circumference

	return outcome
