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
				seasonlist = {}
				for subitem in sublisting:
					if sublisting[subitem] == "Folder":
						if subitem[:7] == "Season ":
							seasonindex = ("000" + subitem[7:])[-2:]
							seasonlist[seasonindex] = subitem
						elif subitem[:7] == "Special":
							seasonlist["000"] = subitem
				orderedlist = []
				for key in sorted(seasonlist, reverse = True):
					orderedlist.append(seasonlist[key])
				self.tvshows[rootitem] = orderedlist
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
			outcome = self.tvshows[tvshowname]
		else:
			outcome = []
		return outcome

