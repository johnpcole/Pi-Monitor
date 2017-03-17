from filedata_subcomponent import filedata_module as FileData


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

		self.moviename = ""

		self.tvshowname = ""

		self.tvseries = -99999

		self.tvepisode = -99999

		self.eta = -99999

	# =========================================================================================

	def updateinfo(self, datalist):

		for dataitem in datalist:

			if dataitem == "name":
				self.torrentname = datalist[dataitem]

			elif dataitem == "total_size":
				rawsize = datalist[dataitem]
				if rawsize > 1000000000:
					self.size = ("%8.2f" % ( int(rawsize / 10000000) * 0.01)) + " Gb"
				elif rawsize > 1000000:
					self.size = ("%8.2f" % ( int(rawsize / 10000) * 0.01)) + " Mb"
				elif rawsize > 1000:
					self.size = ("%8.2f" % ( int(rawsize / 10) * 0.01)) + " kb"
				else:
					self.size = str(int(rawsize) ) + " b"

			elif dataitem == "state":
				self.status = datalist[dataitem]

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
				#for fileitem in dataitem:
				#	self.files.append(FileData.createitem(fileitem['index'], fileitem['path']))
				print "ignoring file data right now"

			elif dataitem == "moviename":
				self.moviename = datalist[dataitem]

			elif dataitem == "tvshowname":
				self.tvshowname = datalist[dataitem]

			elif dataitem == "tvseries":
				self.tvseries = datalist[dataitem]

			elif dataitem == "tvepisode":
				self.tvepisode = datalist[dataitem]

			elif dataitem == "eta":
				self.eta = datalist[dataitem]

			else:
				outcome = "Unknown Data Label: " + dataitem
				assert 0 == 1, outcome

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

		return self.moviename

# =========================================================================================

	def getshowname(self):

		return self.tvshowname

# =========================================================================================

	def getseries(self):

		return self.tvseries

# =========================================================================================

	def getepisode(self):

		return self.tvepisode

# =========================================================================================

	def geteta(self):

		return self.eta
