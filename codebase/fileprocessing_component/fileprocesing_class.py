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

		self.copyactions = []

		self.connectionstatus = 0

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

	def getdropdownlists(self, tvshowname):

		outcome = {}
		outcome['tvshows'] = self.gettvshows()
		outcome['episodes'] = self.episodes
		outcome['subtitles'] = self.subtitles
		outcome['tvshowseasons'] = self.gettvshowseasons(tvshowname)
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

	def queuefilecopy(self, copyactions):

		if copyactions == []:
			print "No copy actions to perform this time"
		else:
#			FileSystem.mountnetworkdrive(self.mountpoint, self.networkpath, self.username, self.password)
			for action in copyactions:
				copysource = FileSystem.createpathfromlist(action['source'])
				rawtarget = FileSystem.createpathfromlist(action['target'])
				copytarget = FileSystem.concatenatepaths(self.mountpoint, rawtarget)
				copyinstruction = {'source': copysource, 'target': copytarget, 'description': rawtarget, 'status': 'Queued'}
				self.copyactions.append(copyinstruction)
#				FileSystem.copyfile(copysource, copytarget)
#			FileSystem.unmountnetworkdrive(self.mountpoint)


# =========================================================================================

	def getcopystate(self):

		copystates = []
		if self.connectionstatus < 0:
			description = "Connected to File Server"
		else:
			description = "Connecting to File Server..."
		copystate = {'description': description, 'status': "("+str(self.connectionstatus)+")"}
		copystates.append(copystate)
		for copyaction in self.copyactions:
			copystate = {'description': copyaction['description'], 'status': copyaction['status']}
			copystates.append(copystate)
		copystate = {'description': "Disconnect File Server", 'status': "-"}
		copystates.append(copystate)

		return copystates



# =========================================================================================

	def processfilecopy(self):

		outcome = False
		if self.connectionstatus > -1:
			self.attempttomount()
			outcome = True
		else:
			for copyitem in self.copyactions:
				if copyitem['status'] == "Copying...":
					copyitem['status'] = "Copied!"
			anycopy = False
			for copyitem in self.copyactions:
				if anycopy == False:
					if copyitem['status'] == "Queued":
						anycopy = True
						copyitem['status'] = "Copying..."
						FileSystem.copyfile(copyitem['source'], copyitem['target'])
			if anycopy == False:
				FileSystem.unmountnetworkdrive(self.mountpoint)
			else:
				outcome = True
		return outcome


	def attempttomount(self):

		self.connectionstatus = self.connectionstatus + 1
		outcome = FileSystem.mountnetworkdrive(self.mountpoint, self.networkpath, self.username, self.password)
		if outcome == 0:
			self.connectionstatus = 0 - self.connectionstatus

