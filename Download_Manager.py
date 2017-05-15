from codebase.torrenting_component import torrenting_module as TorrentManager
from codebase.fileprocessing_component import fileprocessing_module as FileManager
from flask import Flask as Webserver
from flask import render_template as Webpage
from flask import jsonify as Jsondata
from flask import request as Webpost


librarymanager = FileManager.createmanager(FileManager.getlibraryconnectionconfig())
torrentmanager = TorrentManager.createmanager(FileManager.gettorrentconnectionconfig())
torrentmanager.refreshtorrentlist()
torrentmanager.setconfigs(FileManager.loadconfigs())



website = Webserver(__name__)



#===============================================================================================
# Load the Torrents List as new page
#===============================================================================================

@website.route('/')
def initialiselistpage():

	torrentmanager.refreshtorrentlist()
	return Webpage('index.html', torrentlist = torrentmanager.gettorrentlistdata("initialise"))



#===============================================================================================
# Refresh Torrents List on existing page, after performing a bulk action if required
#===============================================================================================

@website.route('/UpdateTorrentsList', methods=['POST'])
def updatelistpage():

	rawdata = Webpost.get_json()
	bulkaction = rawdata["bulkaction"]
	if (bulkaction == "Start") or (bulkaction == "Stop"):
		torrentmanager.bulkprocessalltorrents(bulkaction)
	elif bulkaction != "Refresh":
		print "Unknown Torrents List Update Action ", bulkaction
	torrentmanager.refreshtorrentlist()
	return Jsondata(torrents=torrentmanager.gettorrentlistdata("refresh"))



#===============================================================================================
# Load a Torrent with Network & Configuration Data as new page
#===============================================================================================

@website.route('/Torrent=<torrentid>')
def initialisetorrentpage(torrentid):

	if torrentmanager.validatetorrentid(torrentid) == True:
		torrentmanager.refreshtorrentdata(torrentid)
		return Webpage('torrent.html', selectedtorrent = torrentmanager.gettorrentdata(torrentid, "initialise"))
	else:
		torrentmanager.refreshtorrentlist()
		return Webpage('index.html', torrentlist = torrentmanager.gettorrentlistdata("initialise"))



#===============================================================================================
# Refresh an existing Torrent page with Network Data, after performing an action if required
#===============================================================================================

@website.route('/UpdateTorrent=<torrentid>', methods=['POST'])
def updatetorrentpage(torrentid):

	if torrentmanager.validatetorrentid(torrentid) == True:
		rawdata = Webpost.get_json()
		torrentaction = rawdata['torrentaction']
		if (torrentaction == "Start") or (torrentaction == "Stop"):
			torrentmanager.processonetorrent(torrentid, torrentaction)
		elif torrentaction == "Copy":
			librarymanager.copyfiles(torrentmanager.getcopyactions(torrentid, "Test"))
		elif torrentaction != "Refresh":
			print "Unknown Torrent Update Action ", torrentaction
		torrentmanager.refreshtorrentdata(torrentid)
		return Jsondata(selectedtorrent=torrentmanager.gettorrentdata(torrentid, "refresh"))
	else:
		print "Updating unknown torrent ", torrentid



# ===============================================================================================
# Refresh an existing Torrent page with Configuration Data, after saving new instructions
# ===============================================================================================

@website.route('/ReconfigureTorrent=<torrentid>', methods=['POST'])
def reconfiguretorrentconfiguration(torrentid):

	if torrentmanager.validatetorrentid(torrentid) == True:
		rawdata = Webpost.get_json()
		torrentmanager.reconfiguretorrent(torrentid, rawdata)
		FileManager.saveconfigs(torrentmanager.getconfigs())
		return Jsondata(selectedtorrent = torrentmanager.gettorrentdata(torrentid, "reconfigure"))
	else:
		print "Reconfiguring unknown torrent ", torrentid



# ===============================================================================================
# Refresh an existing Torrent page with Configuration Data used to populate edit fields
# ===============================================================================================

@website.route('/EditTorrent=<torrentid>')
def edittorrentconfiguration(torrentid):

	if torrentmanager.validatetorrentid(torrentid) == True:
		return Jsondata(selectedtorrent=torrentmanager.gettorrentdata(torrentid, "prepareedit"),
													listitems=librarymanager.getdropdownlists())
	else:
		print "Edit unknown torrent ", torrentid



# ===============================================================================================
# Refresh an existing Torrent page with Configuration Data used to populate the Season edit field
# ===============================================================================================

@website.route('/GetTVShowSeasons=<showname>')
def updatetvshowseasonslist(showname):

	return Jsondata(seasons=librarymanager.gettvshowseasons(showname))



# ===============================================================================================
# Performs a Torrent Addition, and returns the new Torrent Data (to be displayed on a new Page)
# ===============================================================================================

@website.route('/AddTorrent', methods=['POST'])
def addnewtorrent():

	rawdata = Webpost.get_json()
	newid = torrentmanager.addnewtorrenttoclient(rawdata['newurl'])
	#torrentmanager.refreshtorrentlist()
	return Jsondata(newid=newid)

#-----------------------------------------------



if FileManager.getwebhostconfig() == True:
	website.run(debug=False, host='0.0.0.0')
else:
	website.run(debug=True)
