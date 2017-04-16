from filesystem_subcomponent import filesystem_module as FileSystem


def gettorrentconnectionconfig():
	credentials = FileSystem.readfromdisk('./data/torrentconnection.cfg')
	outcome = { 'Address': credentials[0],
				'Port': int(credentials[1]),
				'Username': credentials[2],
				'Password': credentials[3]}
	return outcome


def getlibraryconnectionconfig():
	credentials = FileSystem.readfromdisk('./data/libraryconnection.cfg')
	outcome = { 'Mountpoint': credentials[0],
				'Address': credentials[1],
				'Port': int(credentials[2]),
				'Username': credentials[3],
				'Password': credentials[4]}
	return outcome

