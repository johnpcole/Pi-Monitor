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
			self.copyactions = []

			copyinstruction = {'source': '[CONNECT]', 'target': 0, 'description': 'Connect File Server', 'status': 'queued'}
			self.copyactions.append(copyinstruction)

			for action in copyactions:
				copysource = FileSystem.createpathfromlist(action['source'])
				rawtarget = FileSystem.createpathfromlist(action['target'])
				copytarget = FileSystem.concatenatepaths(self.mountpoint, rawtarget)
				copyinstruction = {'source': copysource, 'target': copytarget, 'description': rawtarget, 'status': 'queued'}
				self.copyactions.append(copyinstruction)

			copyinstruction = {'source': '[DISCONNECT]', 'target': 0, 'description': 'Disconnect File Server', 'status': 'queued'}
			self.copyactions.append(copyinstruction)


# =========================================================================================

	def getcopystate(self):

		copystates = []
		for copyaction in self.copyactions:
			outputdescription = copyaction['description']
			if (copyaction['source'])[:1] == "[":
				if copyaction['target'] != 0:
					outputdescription = outputdescription + " (Attempt " + str(copyaction['target']) + ")"
			copystate = {'description': outputdescription, 'status': copyaction['status']}
			copystates.append(copystate)

		return copystates



# =========================================================================================

	def processfilecopy(self):

		continueprocessing = False

		actionoutcome = self.processfilecopyaction()

		startnewitem = True
		for copyitem in self.copyactions:
			if copyitem['status'] == "copying":
				startnewitem = False

		if startnewitem == True:
			for copyitem in self.copyactions:
				if continueprocessing == False:
					if copyitem['status'] == "queued":
						copyitem['status'] = "copying"
						if (copyitem['source'])[-8:] == "CONNECT]":
							copyitem['target'] = copyitem['target'] + 1
						continueprocessing = True

		if actionoutcome == True:
			continueprocessing = True

		return continueprocessing



# =========================================================================================

	def processfilecopyaction(self):

		anychange = False
		for copyitem in self.copyactions:
			if copyitem['status'] == "copying":
				anychange = True

				if copyitem['source'] == "[CONNECT]":
					if FileSystem.mountnetworkdrive(self.mountpoint, self.networkpath, self.username, self.password) == 0:
						copyitem['status'] = "copied"
					else:
						copyitem['target'] = copyitem['target'] + 1

				elif copyitem['source'] == "[DISCONNECT]":
					if FileSystem.unmountnetworkdrive(self.mountpoint) == 0:
						copyitem['status'] = "copied"
					else:
						copyitem['target'] = copyitem['target'] + 1

				else:
					if FileSystem.copyfile(copyitem['source'], copyitem['target']) == 0:
						copyitem['status'] = "copied"
					else:
						copyitem['status'] = "failed"

		return anychange