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


def minifyseasonepisode(seasonname, episodename):

	if seasonname[:7] == "Season ":
		outcome = "00" + seasonname[7:]
		outcome = "S" + outcome[-2:]
	elif seasonname[:7] == "Special":
		outcome = "S00"
	else:
		outcome = "-"

	prefix = episodename[:4]
	if prefix == "Epis":
		suffix = "00" + episodename[9:]
		outcome = outcome + "E" + suffix[-2:]
	elif prefix == "Ep. ":
		doublet = episodename[5:]
		doubletsplit = doublet.split(" & ")
		suffix = "00" + doublet[0]
		outcome = outcome + "E" + suffix[-2:]
		suffix = "00" + doublet[1]
		outcome = outcome + "E" + suffix[-2:]
	elif prefix == "Spec":
		suffix = "00" + episodename[9:]
		outcome = "S00E" + suffix[-2:]
	else:
		outcome = outcome + "-"

	return outcome



