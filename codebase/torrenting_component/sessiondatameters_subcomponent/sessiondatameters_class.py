from . import sessiondatameters_privatefunctions as MeterFunctions



class DefineSessionDataMeters:

	def __init__(self):

		self.uploadspeed = 0

		self.downloadspeed = 0

		self.freespace = 0

		self.temperature = 0

		self.downloadcount = 0

		self.activedownloads = 0

		self.uploadcount = 0

		self.activeuploads = 0




	# =========================================================================================

	def updateactivitycounts(self, torrentset):

		self.downloadcount = 0
		self.activedownloads = 0
		self.uploadcount = 0
		self.activeuploads = 0

		for existingtorrent in torrentset:

			newcount = existingtorrent.getconnectiondata()

			for indexkey in newcount:
				if indexkey == 'downloadcount':
					self.downloadcount = self.downloadcount + newcount[indexkey]
				elif indexkey == 'activedownloads':
					self.activedownloads = self.activedownloads + newcount[indexkey]
				elif indexkey == 'uploadcount':
					self.uploadcount = self.uploadcount + newcount[indexkey]
				elif indexkey == 'activeuploads':
					self.activeuploads = self.activeuploads + newcount[indexkey]
				else:
					print("Unexpected torrent data: ", indexkey)

# =========================================================================================

	def updatesessionstats(self, delugesessiondata, temperaturedata):

		self.temperature = temperaturedata

		for indexkey in delugesessiondata:

			if indexkey == 'uploadspeed':
				self.uploadspeed = delugesessiondata[indexkey]
			elif indexkey == 'downloadspeed':
				self.downloadspeed = delugesessiondata[indexkey]
			elif indexkey == 'freespace':
				self.freespace = delugesessiondata[indexkey]
			else:
				print("Unexecpted session data: ", indexkey)



# =========================================================================================
# Generates an array of stat numerics, required to draw the meter graphs
# =========================================================================================

	def getstats(self):

		outcome = {}
		outcome['downloadspeed'] = MeterFunctions.getneedlemeterdata(self.downloadspeed, -9999.9, 1.0, "Long")
		outcome['uploadspeed'] = MeterFunctions.getneedlemeterdata(self.uploadspeed, -9999.9, 1.0, "Short")
		outcome['space'] = MeterFunctions.getneedlemeterdata(self.freespace, -9999.9, 3.0, "Long")
		outcome['temperature'] = MeterFunctions.getneedlemeterdata(self.temperature, 32.5, 52.5, "Long")
		outcome['downloadcount'] = MeterFunctions.getblockmeterdata(self.downloadcount, "Outer")
		outcome['activedownloads'] = MeterFunctions.getblockmeterdata(self.activedownloads, "Outer")
		outcome['uploadcount'] = MeterFunctions.getblockmeterdata(self.uploadcount, "Inner")
		outcome['activeuploads'] = MeterFunctions.getblockmeterdata(self.activeuploads, "Inner")

#		index = 30.0
#		for indexcounter in range(1, 11):
#			index = index + 2.5
#			item = Functions.getmeterdata(Functions.getlinmeterangle(index, 32.5, 56.25), 0.7, 0.0)
#			dummyoutcome = '                    <line y1="' + str(item['vo']) + '" x1="' + str(item['ho']) + '" y2="' + str(item['vf']) + '" x2="' + str(item['hf']) + '" />'
#			print(dummyoutcome)

		return outcome


