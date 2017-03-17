from deluge_subcomponent import deluge_module as DelugeClient
from torrentdata_subcomponent import torrentdata_module as TorrentData

class DefineTorrentManager:

	def __init__(self, address, port, username, password):

		self.delugeclient = DelugeClient.createinterface(address, port, username, password)

		#self.laststatustime = ???

		self.torrents = []

# =========================================================================================

	def refreshtorrentlist(self):

		outcome = self.delugeclient.openconnection()

		torrentidlist = self.delugeclient.gettorrentlist()
		for torrentiditem in torrentidlist:
			existingtorrent = self.gettorrent(torrentiditem)

			if existingtorrent is None:
				existingtorrent = self.addtorrent(torrentiditem)

			self.refreshtorrentdata(existingtorrent)

		outcome = self.delugeclient.closeconnection()
		print "Connection closed: ", self.delugeclient.delugeinterface.connected

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

		return self.gettorrent(torrentid)

# =========================================================================================

	def gettorrent(self, torrentid):

		outcome = None
		for existingtorrent in self.torrents:
			if existingtorrent.getid() == torrentid:
				outcome = existingtorrent

		return outcome

# =========================================================================================

	def refreshtorrentdata(self, torrentobject):

		torrentdata = self.delugeclient.gettorrentdata(torrentobject.getid())
		print "Refreshing Torrent ", torrentobject.getid()
		torrentobject.updateinfo(torrentdata)

	# =========================================================================================

	def configuretorrent(self, torrentid, stuff):

		temp = stuff


	# =========================================================================================

	def gettorrentdata(self):

		return self.torrents
