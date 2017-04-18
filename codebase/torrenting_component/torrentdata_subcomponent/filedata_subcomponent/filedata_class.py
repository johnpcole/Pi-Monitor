
class DefineFileItem:

	def __init__(self, fileid, path, size):

		self.fileid = fileid

		self.path = path

		pathsplit = self.path.split('/')
		self.shortpath = pathsplit[len(pathsplit)-1]

		self.size = size

		self.filetype = "NONE"
		self.updatefiletype()

		self.episode = ""

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

		return self.path

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

		self.filetype = outcome
