from . import torrenting_class as TorrentManagerClass


# ---------------------------------------------
# Builds a DelugeRPCClient object
# ---------------------------------------------

def createmanager(address, port, username, password):
	return TorrentManagerClass.DefineTorrentManager(address, port, username, password)

