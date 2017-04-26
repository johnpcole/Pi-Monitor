from filedata_subcomponent import filedata_module as FileData
from ...functions_component import functions_module as Functions


class DefineTorrentItem:

	def __init__(self, torrentid):

		self.torrentname = ""

		self.torrentid = torrentid

		self.size = "!UNKNOWN!"

		self.status = "!UNKNOWN!"

		self.location = "!UNKNOWN!"

		self.progress = -99999

		self.finished = False

		self.files = []

		self.torrenttype = "unknown"

		self.movieorshowname = ""

		self.seasonoryear = ""

		self.eta = "!UNKNOWN!"

	# =========================================================================================

	def updateinfo(self, datalist):

		for dataitem in datalist:

			if dataitem == "name":
				self.torrentname = datalist[dataitem]

			elif dataitem == "torrenttype":
				self.torrenttype = datalist[dataitem]

			elif dataitem == "total_size":
				self.size = Functions.sanitisesize(datalist[dataitem])

			elif dataitem == "state":
				temp = datalist[dataitem]
				self.status = temp.lower()

			elif dataitem == "save_path":
				self.location = datalist[dataitem]

			elif dataitem == "progress":
				self.progress = str(int(datalist[dataitem])) + "%"

			elif dataitem == "is_finished":
				if datalist[dataitem] == True:
					self.finished = "Completed"
				else:
					self.finished = "In Progress"

			elif dataitem == "files":
				self.updatefiledata(datalist[dataitem])

			elif (dataitem == "moviename") or (dataitem == "tvshowname"):
				self.movieorshowname = datalist[dataitem]

			elif (dataitem == "year") or (dataitem == "season"):
				self.seasonoryear = datalist[dataitem]

			elif dataitem == "eta":
				self.eta = Functions.sanitisetime(datalist[dataitem])

			else:
				outcome = "Unknown Data Label: " + dataitem
				assert 0 == 1, outcome

# =========================================================================================

	def getfileobject(self, fileid):

		outcome = None

		for existingfile in self.files:
			if existingfile.getid() == fileid:
				outcome = existingfile

		return outcome

# =========================================================================================

	def updatefiledata(self, filedata):

		for fileitem in filedata:
			existingfile = self.getfileobject(fileitem['index'])
			if existingfile is None:
				self.files.append(FileData.createitem(fileitem['index'], fileitem['path'],
																			Functions.sanitisesize(fileitem['size'])))

# =========================================================================================

	def getid(self):

		return self.torrentid

# =========================================================================================

	def getname(self):

		return self.torrentname

# =========================================================================================

	def getsize(self):

		return self.size

# =========================================================================================

	def getstatus(self):

		return self.status

# =========================================================================================

	def getlocation(self):

		return self.location

# =========================================================================================

	def getprogress(self):

		if self.progress == "100%":
			outcome = ""
		else:
			outcome = self.progress
		return outcome

# =========================================================================================

	def getfinished(self):

		return self.finished


# =========================================================================================

	def getfullstatus(self):

		if self.status == "queued":
			if self.finished == True:
				outcome = "seeding_queued"
			else:
				outcome = "downloading_queued"
		elif self.status == "paused":
			if self.finished == True:
				outcome = "seeding_paused"
			else:
				outcome = "downloading_paused"
		elif self.status == "downloading":
			outcome = "downloading_active"
		elif self.status == "seeding":
			outcome = "seeding_active"
		else:
			outcome = self.status
		return outcome

# =========================================================================================

	def getfiles(self):

		return self.files

# =========================================================================================

	def getmoviename(self):

		return self.movieorshowname

# =========================================================================================

	def getshowname(self):

		return self.movieorshowname

# =========================================================================================

	def getseason(self):

		return self.seasonoryear

# =========================================================================================

	def getyear(self):

		return self.seasonoryear

# =========================================================================================

	def geteta(self):

		return self.eta

# =========================================================================================

	def gettype(self):

		return self.torrenttype

# =========================================================================================

	def getprogresssizeeta(self):

		outcome = self.getprogress()
		if outcome != "":
			outcome = outcome + " of "
		outcome = outcome + self.size
		if self.getfullstatus() == "downloading_active":
			outcome = outcome + " (~" + self.eta + ")"
		return outcome

# =========================================================================================

	def getsanitisedname(self):

		outcome = self.movieorshowname
		if self.seasonoryear != "":
			outcome = outcome + "   (" + self.seasonoryear + ")"
		return outcome

# =========================================================================================

	def getheadlinename(self):

		if self.torrenttype == "movie":
			outcome = self.movieorshowname
		elif self.torrenttype == "tvshow":
			outcome = self.movieorshowname
		else:
			outcome = "New Unspecified Torrent"
		return outcome

# =========================================================================================

	def getheadlinesubname(self):

		if self.torrenttype == "movie":
			outcome = self.seasonoryear
		elif self.torrenttype == "tvshow":
			outcome = self.seasonoryear
		else:
			outcome = ""
		return outcome



		# =========================================================================================

	def getheadlinedata(self, datamode):

		if datamode == "initialise":
			outcome = { 'torrentid': self.torrentid,
						'torrenttitle': self.getheadlinename(),
						'torrentsubtitle': self.getheadlinesubname(),
						'torrentname': self.torrentname,
						'torrenttype': self.torrenttype,
						'status': self.getfullstatus(),
						'progress': self.progress}
		elif datamode == "refresh":
			outcome = { 'torrentid': self.torrentid,
						'status': self.getfullstatus(),
						'progress': self.progress}
		else:
			assert 1==0, datamode
		return outcome

# =========================================================================================

	def getextendeddata(self, datamode):

		if datamode == "initialise":
			outcome = { 'torrentid': self.torrentid,
						'torrenttitle': self.getheadlinename(),
						'torrentsubtitle': self.getheadlinesubname(),
						'torrentname': self.torrentname,
						'torrenttype': self.torrenttype,
						'status': self.getfullstatus(),
						'progress': self.getprogresssizeeta(),
						'files': self.files}
		elif datamode == "refresh":
			outcome = { 'status': self.getfullstatus(),
						'progress': self.getprogresssizeeta()}
		elif datamode == "reconfigure":
			outcome = { 'torrenttitle': self.getheadlinename(),
						'torrentsubtitle': self.getheadlinesubname(),
						'torrenttype': self.torrenttype}
		else:
			assert 1 == 0, datamode
		return outcome

# =========================================================================================

	def getsavedata(self):

		outcome = self.getid() + "|-"
		outcome = outcome + "|" + self.getname()
		outcome = outcome + "|" + self.gettype()
		outcome = outcome + "|" + self.getmoviename()
		outcome = outcome + "|" + self.getyear()
		outcomelist = []
		outcomelist.append(outcome)
		for fileitem in self.files:
			outcome = self.getid() + "|" + fileitem.getsavedata()
			outcomelist.append(outcome)
		return outcomelist

# =========================================================================================

	def setsavedata(self, dataarray):

		if dataarray[1] == "-":
			self.updateinfo({"name": dataarray[2], "torrenttype": dataarray[3], "moviename": dataarray[4],
																								"year": dataarray[5]})
		else:
			existingfile = self.getfileobject(int(dataarray[1]))
			if existingfile is not None:
				existingfile.updatefilepurpose(dataarray[2])
			else:
				print "Ignoring Saved File Config for torrent ", dataarray[0], ", file ",dataarray[1]



