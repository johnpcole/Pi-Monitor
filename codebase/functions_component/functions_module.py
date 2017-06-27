import math as Maths

def sanitisesize(rawsize):

	if rawsize > 1000000000:
		outcome = ("%8.2f" % (int(rawsize / 10000000) * 0.01)) + " Gb"
	elif rawsize > 1000000:
		outcome = ("%8.2f" % (int(rawsize / 10000) * 0.01)) + " Mb"
	elif rawsize > 1000:
		outcome = ("%8.2f" % (int(rawsize / 10) * 0.01)) + " kb"
	else:
		outcome = str(int(rawsize)) + " b"

	return outcome


def sanitisetime(rawtime):

	if rawtime > 86400:
		outcome = ("%8.1f" % (int(rawtime / 8640) * 0.1)) + " d"
	elif rawtime > 3600:
		outcome = ("%8.1f" % (int(rawtime / 360) * 0.1)) + " h"
	elif rawtime > 60:
		outcome = ("%8.1f" % (int(rawtime / 6) * 0.1)) + " m"
	elif rawtime > 1:
		outcome = str(rawtime) + "s"
	else:
		outcome = "-"

	return outcome



def minifyseason(seasonname, episodename):

	episodesplit = episodename.split(" ")

	if episodesplit[0] == "Special":
		outcome = "s00"
	else:
		seasonsplit = seasonname.split(" ")
		if seasonsplit[0] == "Season":
			s = "00" + seasonsplit[1]
			outcome = "s" + s[-2:]
		elif seasonname[:7] == "Special":
			outcome = "s00"
		else:
			outcome = "-"

	return outcome



def minifyepisode(episodename):

	episodesplit = episodename.split(" ")
	if len(episodesplit) > 1:
		if episodesplit[0] == "Ep.":
			f = "00" + episodesplit[1]
			f = "e" + f[-2:]
			g = "00" + episodesplit[3]
			g = "e" + g[-2:]
			e = f + g
		else:
			e = "00" + episodesplit[1]
			e = "e" + e[-2:]
	else:
		e = episodename
	return e


def getinitial(name):

	namesplit = name.split(" ")
	if len(namesplit) > 1:
		firstword = namesplit[0]
		firstword = firstword.lower()
		if (firstword == "the") or (firstword == "a") or (firstword == "an"):
			noun = namesplit[1]
		else:
			noun = namesplit[0]
	else:
		noun = name
	outcome = noun[:1]
	return outcome.upper()



def getlogmeterdata(currentval, decalheight, decalwidth, needlesize, scale):

	# Assumes the decal image is 688 x 1236 pixels big, scaled
	# Needle length is 564 at 100% scaling

	verticalratio = decalheight / 688.0
	horizontalratio = decalwidth / 1236.0
	verticalneedlelength = verticalratio * 554.0 * needlesize
	horizontalneedlelength = horizontalratio * 544.0 * needlesize
	verticalorigin = verticalratio * 74.0
	horizontalorigin = horizontalratio * 618.0

	if currentval < 1:
		segment = -1.0
	else:
		segment = scale * Maths.log10(currentval)
		if segment > 7.0:
			segment = 7.0

	angle = Maths.pi * (segment + 1.0) / 8.0

	verticalfinal = (verticalneedlelength * Maths.sin(angle)) + verticalorigin
	horizontalfinal = (horizontalneedlelength * Maths.cos(angle)) + horizontalorigin

	outcome = {}
	outcome['vo'] = decalheight - verticalorigin
	outcome['ho'] = decalwidth - horizontalorigin
	outcome['vf'] = decalheight - verticalfinal
	outcome['hf'] = decalwidth - horizontalfinal

	return outcome
