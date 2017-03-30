from codebase import torrenting_module as TorrentManager
from flask import Flask as Webserver
from flask import render_template as Webpage
from flask import jsonify as Jsondata
#from flask import request as Webpost



torrentmanager = TorrentManager.createmanager('192.168.1.78', 58847, 'piuser', 'pipassword')
website = Webserver(__name__)

#-----------------------------------------------

@website.route('/')
def listpage():
	torrentmanager.refreshtorrentlist()
	return Webpage('index.html', torrentlist = torrentmanager.getalltorrentdata())

#-----------------------------------------------

@website.route('/Torrent=<torrentid>')
def torrentpage(torrentid):

	torrentobject = torrentmanager.gettorrent(torrentid)
	if torrentobject is not None:
		torrentmanager.refreshtorrentdata(torrentobject)
		return Webpage('torrent.html', selectedtorrent = torrentobject.getextendeddata())
	else:
		torrentmanager.refreshtorrentlist()
		return Webpage('index.html', torrentlist = torrentmanager.getalltorrentdata())

	# elif Webpost.method == 'POST':
	#
	# 	print "Received Data", Webpost.form['moviename']
	# 	print "Received Data", Webpost.form['buttons']
	# 	return Webpage('index.html', torrentlist = torrentmanager.getalltorrentdata())
	#
	# else:
	# 	print "Unknown Web request"

#-----------------------------------------------

@website.route('/UpdateTorrentList')
def updatelistdata():
	return Jsondata(torrents=torrentmanager.getalltorrentdataasjson())

#-----------------------------------------------

@website.route('/UpdateTorrent=<action>-<torrentid>')
def updatetorrentdata(action, torrentid):
	torrentobject = torrentmanager.gettorrent(torrentid)
	if torrentobject is not None:
		if action == "Refresh":
			torrentmanager.refreshtorrentdata(torrentobject)
			print "REFRESH!"
		elif action == "Stop":
			torrentmanager.refreshtorrentdata(torrentobject)
			print "STOP!"
		elif action == "Start":
			torrentmanager.refreshtorrentdata(torrentobject)
			print "START!"
		elif action == "Copy":
			print "COPY!"
		elif action == "Edit":
			print "EDIT!"
		elif action == "Delete":
			torrentmanager.refreshtorrentdata(torrentobject)
			print "DELETE!"
		else:
			print "Unknown action for torrent ", torrentid
		return Jsondata(selectedtorrent=torrentobject.getupdatedata())
	else:
		print "Unknown AJAX request for torrent ", torrentid



website.run(debug=True) #, host='0.0.0.0')
