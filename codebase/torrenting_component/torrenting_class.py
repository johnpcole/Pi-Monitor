from deluge_subcomponent import deluge_module as DelugeClient
from torrentdata_subcomponent import torrentdata_module as TorrentData
from ..functions_component import functions_module as Functions
from operator import attrgetter

class DefineTorrentManager:

	def __init__(self, address, port, username, password):

		if address == "dummy":
			self.delugeclient = DelugeClient.createdummy()
		else:
			self.delugeclient = DelugeClient.createinterface(address, port, username, password)

		self.torrents = []

		self.sessiondata = {'uploadspeed':0, 'downloadspeed':0, 'freespace':0}

# =========================================================================================

	def getstats(self):

		outcome = {}
		outcome['d'] = Functions.getlogmeterdata(self.sessiondata['downloadspeed'], 67, 124, 1.0, 1.0)
		outcome['u'] = Functions.getlogmeterdata(self.sessiondata['uploadspeed'], 67, 124, 0.6, 1.0)
		outcome['s'] = Functions.getlogmeterdata(self.sessiondata['freespace'], 67, 124, 1.0, 3.0)

		return outcome

# =========================================================================================

	def refreshtorrentlist(self):

		outcome = self.delugeclient.openconnection()

		self.sessiondata = self.delugeclient.getsessiondata()

		torrentidlist = self.delugeclient.gettorrentlist()
		for torrentiditem in torrentidlist:

			if self.validatetorrentid(torrentiditem) == False:
				newtorrentobject = self.addtorrentobject(torrentiditem)

			self.refreshtorrentdata(torrentiditem)

		outcome = self.delugeclient.closeconnection()
		#print "Connection closure attempted - Connection State = ", outcome

		cleanlist = []

		for existingtorrent in self.torrents:
			foundflag = False
			for torrentiditem in torrentidlist:
				if torrentiditem == existingtorrent.getid():
					cleanlist.append(existingtorrent)
					foundflag = True

			if foundflag == False:
				print "Removing Torrent from Download-Manager: ", existingtorrent.getid()

		self.torrents = sorted(cleanlist, key=attrgetter('dateadded'), reverse=True)

# =========================================================================================

	def addtorrentobject(self, torrentid):

		self.torrents.append(TorrentData.createitem(torrentid))
		print "Adding Torrent to Download-Manager", torrentid

		return self.gettorrentobject(torrentid)

# =========================================================================================

	def validatetorrentid(self, torrentid):

		outcome = False
		for existingtorrent in self.torrents:
			if existingtorrent.getid() == torrentid:
				outcome = True
		return outcome

# =========================================================================================

	def gettorrentobject(self, torrentid):

		outcome = None
		for existingtorrent in self.torrents:
			if existingtorrent.getid() == torrentid:
				outcome = existingtorrent

		return outcome

# =========================================================================================

	def refreshtorrentdata(self, torrentid):

		torrentobject = self.gettorrentobject(torrentid)
		outcome = self.delugeclient.openconnection()

		torrentdata = self.delugeclient.gettorrentdata(torrentid)
		torrentobject.updateinfo(torrentdata)

		outcome = self.delugeclient.closeconnection()
		#print "Connection closure attempted - Connection State = ", outcome


# =========================================================================================

	def gettorrentlistdata(self, datamode):

		outcome = []

		for torrentitem in self.torrents:
			outcome.append(torrentitem.getheadlinedata(datamode))

		return outcome

# =========================================================================================

	def gettorrentdata(self, torrentid, datamode):

		torrentobject = self.gettorrentobject(torrentid)

		return torrentobject.getextendeddata(datamode)

# =========================================================================================

	def reconfiguretorrent(self, torrentid, newconfig):

		torrentobject = self.gettorrentobject(torrentid)
		torrentobject.reconfiguretorrent(newconfig)

# =========================================================================================

	def getconfigs(self):

		outcome = []
		for torrentitem in self.torrents:
			newrows = torrentitem.getsavedata()
			for newrow in newrows:
				outcome.append(newrow)
		return outcome

# =========================================================================================

	def setconfigs(self, datalist):

		for dataitem in datalist:
			datavalues = dataitem.split("|")
			torrentobject = self.gettorrentobject(datavalues[0])
			if torrentobject is not None:
				torrentobject.setsavedata(datavalues)
			else:
				print "Ignoring Saved Config for Torrent ", datavalues[0]

# =========================================================================================

	def addnewtorrenttoclient(self, newurl):

		outcome = self.delugeclient.openconnection()
		newid = self.delugeclient.addtorrentlink(newurl)
		newobject = self.addtorrentobject(newid)
		self.refreshtorrentdata(newid)
		outcome = self.delugeclient.closeconnection()

		return newid

# =========================================================================================

	def bulkprocessalltorrents(self, bulkaction):

		if bulkaction == "Stop":
			outcome = self.delugeclient.openconnection()
			self.delugeclient.pausetorrent("ALL")
			outcome = self.delugeclient.closeconnection()
		elif bulkaction == "Start":
			outcome = self.delugeclient.openconnection()
			self.delugeclient.resumetorrent("ALL")
			outcome = self.delugeclient.closeconnection()
		else:
			print "Unknown Bulk Torrent Request ", bulkaction

# =========================================================================================

	def processonetorrent(self, torrentid, action):

		if action == "Stop":
			outcome = self.delugeclient.openconnection()
			self.delugeclient.pausetorrent(torrentid)
			outcome = self.delugeclient.closeconnection()
		elif action == "Start":
			outcome = self.delugeclient.openconnection()
			self.delugeclient.resumetorrent(torrentid)
			outcome = self.delugeclient.closeconnection()
		elif action == "Delete":
			outcome = self.delugeclient.openconnection()
			#self.delugeclient.pausetorrent(torrentid)
			self.delugeclient.deletetorrent(torrentid)
			outcome = self.delugeclient.closeconnection()
		else:
			print "Unknown Single Torrent Request ", action

# =========================================================================================

	def getcopyactions(self, torrentid):

		torrentobject = self.gettorrentobject(torrentid)
		if torrentobject.getfinished() == 'Completed':
			outcome = torrentobject.getcopyactions()
		else:
			outcome = []

		return outcome

