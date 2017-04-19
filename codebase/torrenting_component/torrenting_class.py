from deluge_subcomponent import deluge_module as DelugeClient
from torrentdata_subcomponent import torrentdata_module as TorrentData

class DefineTorrentManager:

	def __init__(self, address, port, username, password):

		if address == "dummy":
			self.delugeclient = DelugeClient.createdummy()
		else:
			self.delugeclient = DelugeClient.createinterface(address, port, username, password)

		self.torrents = []

# =========================================================================================

	def refreshtorrentlist(self):

		outcome = self.delugeclient.openconnection()

		torrentidlist = self.delugeclient.gettorrentlist()
		for torrentiditem in torrentidlist:
			existingtorrent = self.gettorrentobject(torrentiditem)

			if existingtorrent is None:
				existingtorrent = self.addtorrent(torrentiditem)

			self.refreshtorrentdata(existingtorrent)

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
				print "Deleting Torrent ", existingtorrent.getid()

		self.torrents = cleanlist

# =========================================================================================

	def addtorrent(self, torrentid):

		self.torrents.append(TorrentData.createitem(torrentid))
		print "Adding Torrent ", torrentid

		return self.gettorrentobject(torrentid)

# =========================================================================================

	def gettorrentobject(self, torrentid):

		outcome = None
		for existingtorrent in self.torrents:
			if existingtorrent.getid() == torrentid:
				outcome = existingtorrent

		return outcome

# =========================================================================================

	def refreshtorrentdata(self, torrentobject):

		outcome = self.delugeclient.openconnection()

		torrentdata = self.delugeclient.gettorrentdata(torrentobject.getid())
		torrentobject.updateinfo(torrentdata)

		outcome = self.delugeclient.closeconnection()
		#print "Connection closure attempted - Connection State = ", outcome


	# =========================================================================================

	def configuretorrent(self, torrentid, stuff):

		temp = stuff

# =========================================================================================

	def gettorrentlistdata(self, datamode):

		outcome = []

		for torrentitem in self.torrents:
			outcome.append(torrentitem.getheadlinedata(datamode))

		return outcome

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
				print "Ignoring Saved Config for torrent ", datavalues[0]

