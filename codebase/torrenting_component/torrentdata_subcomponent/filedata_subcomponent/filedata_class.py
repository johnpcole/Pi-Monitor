
class DefineFileItem:

	def __init__(self, fileid, path, size):

		self.fileid = fileid

		self.path = path

		pathsplit = self.path.split('/')
		self.shortpath = pathsplit[len(pathsplit)-1]

		self.size = size

		self.filetype = "NONE"

		self.episode = -99999

# =========================================================================================

	def updatefilepurpose(self, episode, filetype):

		self.filetype = filetype

		self.episode = episode

# =========================================================================================

	def getepisode(self):

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
