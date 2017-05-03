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

#-----------------------------------------------

@website.route('/')
def initialiselistpage():
	torrentmanager.refreshtorrentlist()
	return Webpage('index.html', torrentlist = torrentmanager.gettorrentlistdata("initialise"))

#-----------------------------------------------

@website.route('/UpdateTorrentsList=<bulkaction>')
def updatelistpage(bulkaction):
	if (bulkaction == "Start") or (bulkaction == "Stop"):
		torrentmanager.bulkprocessalltorrents(bulkaction)
	elif bulkaction != "Refresh":
		print "Unknown Torrents List Update Action ", bulkaction
	torrentmanager.refreshtorrentlist()
	return Jsondata(torrents=torrentmanager.gettorrentlistdata("refresh"))

#-----------------------------------------------

@website.route('/Torrent=<torrentid>')
def initialisetorrentpage(torrentid):

	torrentobject = torrentmanager.gettorrentobject(torrentid)
	if torrentobject is not None:
		torrentmanager.refreshtorrentdata(torrentobject)
		return Webpage('torrent.html', selectedtorrent = torrentobject.getextendeddata("initialise"),
										tvshowlist = librarymanager.gettvshows())
	else:
		torrentmanager.refreshtorrentlist()
		return Webpage('index.html', torrentlist = torrentmanager.gettorrentlistdata("initialise"))

#-----------------------------------------------

@website.route('/RefreshTorrent=<torrentid>')
def updatetorrentpage(torrentid):
	torrentobject = torrentmanager.gettorrentobject(torrentid)
	if torrentobject is not None:
		torrentmanager.refreshtorrentdata(torrentobject)
		return Jsondata(selectedtorrent=torrentobject.getextendeddata("refresh"))
	else:
		print "Refreshing unknown torrent ", torrentid

#-----------------------------------------------

@website.route('/ReconfigureTorrent=<torrentid>', methods=['POST'])
def updatetorrentconfiguration(torrentid):
	torrentobject = torrentmanager.gettorrentobject(torrentid)
	if torrentobject is not None:
		torrentobject.reconfiguretorrent(Webpost.get_json())
	else:
		print "Reconfiguring unknown torrent ", torrentid
	FileManager.saveconfigs(torrentmanager.getconfigs())
	return Jsondata(selectedtorrent=torrentobject.getextendeddata("reconfigure"))

#-----------------------------------------------

@website.route('/GetTVShowSeasons=<showname>')
def updatetvshowseasonslist(showname):
	return Jsondata(seasons=librarymanager.gettvshowseasons(showname))

#-----------------------------------------------

@website.route('/AddTorrent', methods=['POST'])
def addnewtorrent():
	rawdata = Webpost.get_json()
	newidval = torrentmanager.addnewtorrenttoclient(rawdata['newurl'])
	#torrentmanager.refreshtorrentlist()
	return Jsondata(newid=newidval)



website.run(debug=True)#, host='0.0.0.0')
