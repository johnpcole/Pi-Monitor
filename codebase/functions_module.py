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
