from codebase import torrenting_module as TorrentManager
from flask import Flask as Webserver
from flask import render_template as Webpage
from flask import jsonify as Jsondata
#from flask import request as Webpost



torrentmanager = TorrentManager.createmanager('12.13.14.44', 58847, 'delugeweb_public', 'publicpassword')
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

	# elif Webpost.method == 'POST':
	#
	# 	print "Received Data", Webpost.form['moviename']
	# 	print "Received Data", Webpost.form['buttons']
	# 	return Webpage('index.html', torrentlist = torrentmanager.getalltorrentdata())
	#
	# else:
	# 	print "Unknown Web request"

#-----------------------------------------------

@website.route('/UpdateTorrent=<torrentid>=<action>')
def updatetorrentpage(torrentid, action):
	torrentobject = torrentmanager.gettorrent(torrentid)
	if torrentobject is not None:
		if action == "Refresh":
			refreshmode = "refresh"
			print "REFRESH!"
		elif action == "Stop":
			refreshmode = "refresh"
			print "STOP!"
		elif action == "Start":
			refreshmode = "refresh"
			print "START!"
		elif action == "Copy":
			print "COPY!"
			refreshmode = "refresh"
		elif action == "Delete":
			refreshmode = "refresh"
			print "DELETE!"
		elif action[:12] == "Reconfigure|":
			print "EDIT!"
			refreshmode = "reconfigure"
			rawactionlist = action[12:]
			actionlist = rawactionlist.split("|")
			torrentobject.updateinfo({ 'torrenttype' : actionlist[0] })
			torrentobject.updateinfo({ 'moviename' : actionlist[1] })
			torrentobject.updateinfo({ 'year' : actionlist[2] })
		else:
			print "Unknown action for torrent ", torrentid
			refreshmode = "refresh"
		if refreshmode == "refresh":
			torrentmanager.refreshtorrentdata(torrentobject)
		return Jsondata(selectedtorrent=torrentobject.getextendeddata(refreshmode))
	else:
		print "Unknown AJAX request for torrent ", torrentid



website.run(debug=True) #, host='0.0.0.0')
