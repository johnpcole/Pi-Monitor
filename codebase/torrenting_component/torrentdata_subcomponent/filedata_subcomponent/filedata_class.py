

class DefineFileItem:

	def __init__(self, fileid, path):

		self.fileid = fileid

		self.path = path

		self.purpose = "NONE"

# =========================================================================================

	def updatefilepurpose(self, purpose):

		self.purpose = purpose

# =========================================================================================

	def getpurpose(self):

		return self.purpose

# =========================================================================================

	def getid(self):

		return self.fileid

# =========================================================================================

	def getpath(self):

		return self.path
