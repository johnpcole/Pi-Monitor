from codebase.torrenting_component import torrenting_module as TorrentManager
from codebase.fileprocessing_component import fileprocessing_module as FileManager
from flask import Flask as Webserver
from flask import render_template as Webpage
from flask import jsonify as Jsondata
#from flask import request as Webpost


torrentcredentials = FileManager.readfromdisk('./data/connection.cfg')
networkmountpoint = FileManager.readfromdisk('./data/mountpoint.cfg')
#print torrentcredentials[0], torrentcredentials[1], torrentcredentials[2], torrentcredentials[3]
torrentmanager = TorrentManager.createmanager(torrentcredentials[0], torrentcredentials[1], torrentcredentials[2],
																								torrentcredentials[3])
tvshowlist = ['Doctor Who', 'Family Guy', '- New']

website = Webserver(__name__)

#-----------------------------------------------

@website.route('/')
def initialiselistpage():
	torrentmanager.refreshtorrentlist()
	return Webpage('index.html', torrentlist = torrentmanager.gettorrentlistdata("initialise"))

#-----------------------------------------------

@website.route('/UpdateTorrentsList')
def updatelistpage():
	return Jsondata(torrents=torrentmanager.gettorrentlistdata("refresh"))

#-----------------------------------------------

@website.route('/Torrent=<torrentid>')
def initialisetorrentpage(torrentid):

	torrentobject = torrentmanager.gettorrent(torrentid)
	if torrentobject is not None:
		torrentmanager.refreshtorrentdata(torrentobject)
		return Webpage('torrent.html', selectedtorrent = torrentobject.getextendeddata("initialise"), tvshowlist = tvshowlist)
	else:
		torrentmanager.refreshtorrentlist()
		return Webpage('index.html', torrentlist = torrentmanager.gettorrentlistdata("initialise"))

#-----------------------------------------------

@website.route('/RefreshTorrent=<torrentid>')
def updatetorrentpage(torrentid):
	torrentobject = torrentmanager.gettorrent(torrentid)
	if torrentobject is not None:
		print "REFRESH!"
		torrentmanager.refreshtorrentdata(torrentobject)
		return Jsondata(selectedtorrent=torrentobject.getextendeddata("refresh"))
	else:
		print "Refreshing unknown torrent ", torrentid

#-----------------------------------------------

@website.route('/ReconfigureTorrent=<torrentid>=<newdata>')
def updatetorrentconfiguration(torrentid, newdata):
	torrentobject = torrentmanager.gettorrent(torrentid)
	if torrentobject is not None:
		print "RECONFIGURE!"
		actionlist = newdata.split("|")
		torrentobject.updateinfo({ 'torrenttype' : actionlist[0] })
		torrentobject.updateinfo({ 'moviename' : actionlist[1] })
		torrentobject.updateinfo({ 'year' : actionlist[2] })
	else:
		print "Reconfiguring unknown torrent ", torrentid
	torrentmanager.refreshtorrentdata(torrentobject)
	return Jsondata(selectedtorrent=torrentobject.getextendeddata("reconfigure"))



website.run(debug=True) #, host='0.0.0.0')
