from filedata_subcomponent import filedata_module as FileData
from .. import functions_module as Functions


class DefineTorrentItem:

	def __init__(self, torrentid):

		self.torrentname = "!UNKNOWN!"

		self.torrentid = torrentid

		self.size = "!UNKNOWN!"

		self.status = "!UNKNOWN!"

		self.location = "!UNKNOWN!"

		self.progress = -99999

		self.finished = False

		self.files = []

		self.torrenttype = "movie" #"unknown"

		self.movieorshowname = "My First Film" #""

		self.seasonoryear = "2016" #""

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

	def updatefiledata(self, filedata):

		for fileitem in filedata:
			foundflag = False
			for existingfile in self.files:
				if existingfile.getid() == fileitem['index']:
					foundflag = True
			if foundflag == False:
				self.files.append(FileData.createitem(fileitem['index'], fileitem['path'], Functions.sanitisesize(fileitem['size'])))

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

		return self.progress

# =========================================================================================

	def getfinished(self):

		return self.finished

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

	def getsizeeta(self):

		if self.status == "downloading":
			outcome = self.size + " (~" + self.eta + ")"
		else:
			outcome = self.size
		return outcome

# =========================================================================================

	def getsanitisedname(self):

		outcome = self.movieorshowname
		if self.seasonoryear != "":
			outcome = outcome + "   (" + self.seasonoryear + ")"
		return outcome

# =========================================================================================

	def getheadlinedata(self, datamode):

		if datamode == "initialise":
			outcome = { 'torrentid': self.torrentid,
						'torrentname': self.torrentname,
						'torrenttype': self.torrenttype,
						'status': self.status,
						'progress': self.progress,
						'finished': self.finished,
						'sizeeta': self.getsizeeta()}
		elif datamode == "refresh":
			outcome = { 'torrentid': self.torrentid,
						'status': self.status,
						'progress': self.progress,
						'finished': self.finished,
						'sizeeta': self.getsizeeta()}
		else:
			assert 1==0, datamode
		return outcome

# =========================================================================================

	def getextendeddata(self, datamode):

		if datamode == "initialise":
			outcome = { 'torrentid': self.torrentid,
						'torrentname': self.torrentname,
						'torrenttype': self.torrenttype,
						'status': self.status,
						'progress': self.progress,
						'finished': self.finished,
						'sizeeta': self.getsizeeta(),
						'files': self.files,
						'sanitisedname': self.getsanitisedname()}
		elif datamode == "refresh":
			outcome = { 'status': self.status,
						'progress': self.progress,
						'sizeeta': self.getsizeeta()}
		elif datamode == "reconfigure":
			outcome = { 'torrentname': self.torrentname,
						'torrenttype': self.torrenttype,
						'sanitisedname': self.getsanitisedname()}
		else:
			assert 1 == 0, datamode
		return outcome

