from . import torrenting_class as TorrentManagerClass


def createmanager(address, port, username, password):
	return TorrentManagerClass.DefineTorrentManager(address, port, username, password)

