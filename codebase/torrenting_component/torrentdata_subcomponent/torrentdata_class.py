from filedata_subcomponent import filedata_module as FileData
from ...functions_component import functions_module as Functions
from operator import itemgetter, attrgetter, methodcaller


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
		self.files = sorted(self.files, key=attrgetter('filetype', 'shortpath'), reverse=True)

# =========================================================================================

	def updatefilepurpose(self, fileid, filepurpose):

		existingfile = self.getfileobject(int(fileid))
		if existingfile is not None:
			existingfile.updatefilepurpose(filepurpose)
		else:
			print "Cannot identify file"

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
			if self.finished == "Completed":
				outcome = "seeding_queued"
			else:
				outcome = "downloading_queued"
		elif self.status == "paused":
			if self.finished == "Completed":
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

	def getfileobjects(self):

		return self.files

# =========================================================================================

	def getmoviename(self):

		if self.torrenttype == "movie":
			outcome = self.movieorshowname
		else:
			outcome = ""
		return outcome

# =========================================================================================

	def getshowname(self):

		if self.torrenttype == "tvshow":
			outcome = self.movieorshowname
		else:
			outcome = ""
		return outcome

# =========================================================================================

	def getseason(self):

		if self.torrenttype == "tvshow":
			outcome = self.seasonoryear
		else:
			outcome = ""
		return outcome

# =========================================================================================

	def getyear(self):

		if self.torrenttype == "movie":
			outcome = self.seasonoryear
		else:
			outcome = ""
		return outcome

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

	def gettorrenttitle(self):

		outcome = self.getmoviename() + self.getshowname()
		if outcome == "":
			outcome = "New Unspecified Torrent"
		suffix = self.getyear() + self.getseason()
		if suffix != "":
			outcome = outcome + " - " + suffix

		suffix = ""
		if self.gettype() == "tvshow":
			for file in self.files:
				if file.getoutcome() == "copy":
					episodename = file.getepisodepart(0)
					if episodename != "":
						if suffix == "":
							suffix = episodename
						else:
							if suffix != episodename:
								suffix = "(Multiple Episodes)"
		if suffix != "":
			outcome = outcome + " " + suffix

		return outcome

# # =========================================================================================
#
# 	def gettorrenttilename(self):
#
# 		if (self.torrenttype == "movie") or (self.torrenttype == "tvshow"):
# 			outcome = self.movieorshowname
# 		else:
# 			outcome = "New Unspecified Torrent"
# 		return outcome
#
# # =========================================================================================
#
# 	def gettorrenttileseasonyear(self):
#
# 		if (self.torrenttype == "movie") or (self.torrenttype == "tvshow"):
# 			outcome = self.seasonoryear
# 		else:
# 			outcome = ""
# 		return outcome
#
# # =========================================================================================
#
# 	def gettorrenttileseasonyearjoiner(self):
#
# 		outcome = ""
# 		if (self.torrenttype == "movie") or (self.torrenttype == "tvshow"):
# 			if self.seasonoryear != "":
# 				outcome = " - "
# 		return outcome

# =========================================================================================

	def getheadlinedata(self, datamode):

		if datamode == "initialise":
			outcome = { 'torrentid': self.torrentid,
						'torrenttitle': self.gettorrenttitle(),
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
						'torrenttitle': self.gettorrenttitle(),
						'torrentname': self.torrentname,
						'torrenttype': self.torrenttype,
						'status': self.getfullstatus(),
						'progress': self.getprogresssizeeta(),
						'files': self.getextendedfiledata(datamode)}
		elif datamode == "refresh":
			outcome = { 'status': self.getfullstatus(),
						'progress': self.getprogresssizeeta()}
		elif datamode == "reconfigure":
			outcome = { 'torrenttitle': self.gettorrenttitle(),
						'torrenttype': self.torrenttype,
						'files': self.getextendedfiledata(datamode)}
		elif datamode == "prepareedit":
			outcome = { 'moviename': self.getmoviename(),
						'movieyear': self.getyear(),
						'tvshowname': self.getshowname(),
						'tvshowseason': self.getseason(),
						'torrenttype': self.gettype(),
						'files': self.getextendedfiledata(datamode)}
		else:
			assert 1 == 0, datamode
		return outcome


# =========================================================================================

	def getextendedfiledata(self, datamode):
		outcome = []
		for file in self.files:
			if (file.gettype() != "none") or (datamode != "prepareedit"):
				filedata = {}
				filedata["fileid"] = file.getid()
				if datamode == "initialise":
					filedata["filename"] = file.getshortpath()
					filedata["filetype"] = file.gettype()
					filedata["size"] = file.getsize()
					filedata["filetitle"] = self.getfiletitle(file)
					filedata["outcome"] = file.getoutcome()
				elif datamode == "reconfigure":
					filedata["filetitle"] = self.getfiletitle(file)
					filedata["outcome"] = file.getoutcome()
				elif datamode == "prepareedit":
					filedata["outcome"] = file.getoutcome()
					filedata["filetype"] = file.gettype()
					filedata["episodeselector"] = file.getepisodepart(0)
					filedata["subtitleselector"] = file.getepisodepart(1)
				else:
					assert 1 == 0, datamode
				outcome.append(filedata)
		return outcome

		# =========================================================================================

	def getfiletitle(self, fileobject):

		outcome = fileobject.gettitle()
		if self.gettype() == "tvshow":
			if outcome[:6] != "Ignore":
				prefix = self.getseason()
				if prefix != "":
					outcome = prefix + " " + outcome
		return outcome


# =========================================================================================

	def reconfiguretorrent(self, instructions):
		for indexkey in instructions:
			if indexkey == "files":
				files = instructions[indexkey]
				for fileindexkey in files:
					self.updatefilepurpose(fileindexkey, files[fileindexkey])
			else:
				self.updateinfo({indexkey: instructions[indexkey]})

# =========================================================================================

	def getsavedata(self):

		outcome = self.getid() + "|-"
		outcome = outcome + "|" + self.gettype()
		outcome = outcome + "|" + self.getmoviename() + self.getshowname()
		outcome = outcome + "|" + self.getyear() + self.getseason()
		outcomelist = []
		outcomelist.append(outcome)
		for fileitem in self.files:
			outcome = self.getid() + "|" + fileitem.getsavedata()
			outcomelist.append(outcome)
		return outcomelist

# =========================================================================================

	def setsavedata(self, dataarray):

		if dataarray[1] == "-":
			self.updateinfo({"torrenttype": dataarray[2], "moviename": dataarray[3], "year": dataarray[4]})
		else:
			existingfile = self.getfileobject(int(dataarray[1]))
			if existingfile is not None:
				existingfile.updatefilepurpose(dataarray[2])
			else:
				print "Ignoring Saved File Config for torrent ", dataarray[0], ", file ",dataarray[1]
