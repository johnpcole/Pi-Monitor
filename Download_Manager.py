from codebase.torrenting_component import torrenting_module as TorrentManager
from flask import Flask as Webserver
from flask import render_template as Webpage

torrentmanager = TorrentManager.createmanager('192.168.1.78', 58846, 'piuser', 'pipassword')
website = Webserver(__name__)

#-----------------------------------------------

@website.route('/')
def indexpage():
	torrentmanager.refreshtorrentlist()
	return Webpage('index.html', torrentlist = torrentmanager.getalltorrentdata())

#-----------------------------------------------

@website.route('/Torrent=<torrentid>')
def namepage(torrentid):
	torrentobject = torrentmanager.gettorrent(torrentid)
	if torrentobject is not None:
		torrentmanager.refreshtorrentdata(torrentobject)
		return Webpage('torrent.html', selectedtorrent = torrentobject)
	else:
		torrentmanager.refreshtorrentlist()
		return Webpage('index.html', torrentlist = torrentmanager.getalltorrentdata())

#-----------------------------------------------


website.run(debug=True) #, host='0.0.0.0')
