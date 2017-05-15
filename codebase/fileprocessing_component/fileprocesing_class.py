from filesystem_subcomponent import filesystem_module as FileSystem

class DefineLibraryManager:

	def __init__(self, mountpoint, networkpath, username, password):

		self.tvshows = {}

		self.episodes = []

		self.subtitles = []

		self.mountpoint = mountpoint

		self.networkpath = networkpath

		self.username = username

		self.password = password

		self.discovertvshows()
		self.discoverepisodes()
		self.discoversubtitles()

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

	def getdropdownlists(self):

		outcome = {}
		outcome['tvshows'] = self.gettvshows()
		outcome['episodes'] = self.episodes
		outcome['subtitles'] = self.subtitles
		return outcome

# =========================================================================================

	def gettvshowseasons(self, tvshowname):

		if tvshowname in self.tvshows:
			outcome = self.tvshows[tvshowname]
		else:
			outcome = []
		return outcome

# =========================================================================================

	def discoverepisodes(self):

		for x in range(1, 41):
			self.episodes.append("Episode "+str(x))
		for x in range(1, 40):
			self.episodes.append("Ep. "+str(x)+" & "+str(x+1))
		for x in range(1, 100):
			self.episodes.append("Special "+str(x))

# =========================================================================================

	def discoversubtitles(self):

		self.subtitles.append("Standard")
		self.subtitles.append("English")
		self.subtitles.append("SDH")
		self.subtitles.append("Eng-SDH")

# =========================================================================================

	def copyfiles(self, copyactions):

		if copyactions == []:
			print "No copy actions to perform this time"
		else:
			FileSystem.mountnetworkdrive(self.mountpoint, self.networkpath, self.username, self.password)
			for action in copyactions:
				source = FileSystem.createpathfromlist(action['source'])
				target = FileSystem.concatenatepaths(self.mountpoint, FileSystem.createpathfromlist(action['target']))
				FileSystem.copyfile(source, target)
			FileSystem.unmountnetworkdrive(self.mountpoint)
