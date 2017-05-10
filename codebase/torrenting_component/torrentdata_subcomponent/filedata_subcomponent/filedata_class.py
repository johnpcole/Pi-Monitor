
class DefineFileItem:

	def __init__(self, fileid, path, size):

		self.fileid = fileid

		self.path = path

		pathsplit = self.path.split('/')
		self.shortpath = pathsplit[len(pathsplit)-1]

		self.size = size

		self.filetype = "NOT PROCESSED"
		self.updatefiletype()

		self.episode = "ignore"

# =========================================================================================

	def updatefilepurpose(self, episode):

		self.episode = episode

# =========================================================================================

	def getpurpose(self):

		return self.episode

# =========================================================================================

	def gettype(self):

		return self.filetype

# =========================================================================================

	def getid(self):

		return self.fileid

# =========================================================================================

	def getpath(self):

		return self.path

# =========================================================================================

	def getshortpath(self):

		return self.shortpath

# =========================================================================================

	def getsize(self):

		return self.size

# =========================================================================================

	def updatefiletype(self):

		filenamesplit = self.shortpath.split('.')
		extension = filenamesplit[len(filenamesplit)-1]
		outcome = "NONE"

		if extension == "srt":
			outcome = "SUBTITLE"
		elif extension == "sub":
			outcome = "SUBTITLE"

		elif extension == "avi":
			outcome = "VIDEO"
		elif extension == "divx":
			outcome = "VIDEO"
		elif extension == "m4v":
			outcome = "VIDEO"
		elif extension == "mkv":
			outcome = "VIDEO"
		elif extension == "mov":
			outcome = "VIDEO"
		elif extension == "mp4":
			outcome = "VIDEO"

		self.filetype = outcome.lower()

# =========================================================================================

	def getsavedata(self):

		outcome = str(self.getid()) + "|" + self.getpurpose()
		return outcome

# =========================================================================================

	def gettitle(self):

		outcome = ""
		if self.gettype() != "none":
			if self.getpurpose() == "ignore":
				outcome = "Ignored"
			else:
				rawstring = self.getpurpose()
				rawsplit = rawstring.split("_")
				episodename = rawsplit[0]
				if episodename[:4] == "Ep. ":
					outcome = "Episodes " + episodename[4:]
				else:
					outcome = episodename
				if len(rawsplit) > 1:
					if rawsplit[1] == "":
						outcome = outcome + " Unknown"
					else:
						outcome = outcome + " " + rawsplit[1]
			if self.gettype() == "video":
				outcome = outcome + " Video File"
			elif self.gettype() == "subtitle":
				outcome = outcome + " Subtitle File"
		else:
			outcome = "Ignored File"
		return outcome

# =========================================================================================

	def getoutcome(self):

		outcome = ""
		if self.getpurpose() == "ignore":
			outcome = "ignore"
		else:
			outcome = "copy"
		return outcome

# =========================================================================================

	def getepisodepart(self, part):

		outcome = ""
		rawstring = self.getpurpose()
		rawsplit = rawstring.split("_")
		if part == 0:
			outcome = rawsplit[0]
		elif (part == 1) and (self.gettype() == "subtitle"):
			outcome = "Unknown"
			if len(rawsplit) > 1:
				if rawsplit[1] != "":
					outcome = rawsplit[1]
		return outcome


