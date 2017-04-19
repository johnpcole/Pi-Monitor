from filesystem_subcomponent import filesystem_module as FileSystem

class DefineLibraryManager:

	def __init__(self, mountpoint, networkpath, username, password):

		self.tvshows = {}

		self.mountpoint = mountpoint

		self.networkpath = networkpath

		self.username = username

		self.password = password

		self.discovertvshows()

	# =========================================================================================

	def discovertvshows(self):

		self.tvshows = {}
		FileSystem.mountnetworkdrive(self.mountpoint, self.networkpath, self.username, self.password)
		rootfolder = FileSystem.concatenatepaths(self.mountpoint, "TV Shows")
		rootlisting = FileSystem.getfolderlisting(rootfolder)
		for rootitem in rootlisting:
			if rootlisting[rootitem] == "Folder":
				subfolder = FileSystem.concatenatepaths(rootfolder, rootitem)
				sublisting = FileSystem.getfolderlisting(subfolder)
				seasonlist = []
				for subitem in sublisting:
					if sublisting[subitem] == "Folder":
						seasonlist.append(subitem)
				self.tvshows[rootitem] = seasonlist
		FileSystem.unmountnetworkdrive(self.mountpoint)

	# =========================================================================================

	def gettvshowlists(self):

		return self.tvshows

	# =========================================================================================

	def gettvshows(self):

		return sorted(self.tvshows.keys())

	# =========================================================================================

	def gettvshowseasons(self, tvshowname):

		if tvshowname in self.tvshows:
			outcome = sorted(self.tvshows[tvshowname])
		else:
			outcome = []
		return outcome

