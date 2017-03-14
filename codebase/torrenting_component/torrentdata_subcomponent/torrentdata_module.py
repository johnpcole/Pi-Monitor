from . import torrentdata_class as TorrentDataClass


def createitem(torrentid):
	return TorrentDataClass.DefineTorrentItem(torrentid)

