from filesystem_subcomponent import filesystem_module as FileSystem
from . import fileprocesing_class as FileManagerClass

# =========================================================================================

def createmanager(connectioncredentials):
	return FileManagerClass.DefineLibraryManager(connectioncredentials['Mountpoint'],
													connectioncredentials['Address'],connectioncredentials['Username'],
													connectioncredentials['Password'])

# =========================================================================================

def gettorrentconnectionconfig():
	credentials = FileSystem.readfromdisk('./data/torrentconnection.cfg')
	outcome = { 'Address': credentials[0],
				'Port': int(credentials[1]),
				'Username': credentials[2],
				'Password': credentials[3]}
	return outcome

# =========================================================================================

def getlibraryconnectionconfig():
	credentials = FileSystem.readfromdisk('./data/libraryconnection.cfg')
	outcome = { 'Mountpoint': credentials[0],
				'Address': credentials[1],
				'Username': credentials[2],
				'Password': credentials[3]}
	return outcome

# =========================================================================================

def saveconfigs(outputlist):
	FileSystem.writetodisk('./data/torrentconfigs.db', outputlist)

# =========================================================================================

def loadconfigs():
	return FileSystem.readfromdisk('./data/torrentconfigs.db')

# =========================================================================================

def getwebhostconfig():
	publicmode = FileSystem.readfromdisk('./data/webhost.cfg')
	if publicmode[0] == "Public":
		outcome = True
	else:
		outcome = False
	return outcome
