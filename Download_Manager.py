from codebase.torrenting_component import torrenting_module as TorrentManager
from flask import Flask as Webserver
from flask import render_template as Webpage

torrentmanager = TorrentManager.createmanager('192.168.1.78', 58846, 'piuser', 'pipassword')
website = Webserver(__name__)

#-----------------------------------------------

@website.route('/')
def indexpage():
	torrentmanager.refreshtorrentlist()
	return Webpage('index.html', torrentlist = torrentmanager.gettorrentdata())

#-----------------------------------------------

@website.route('/<location>')
def namepage(location):
	testdata = [{ 'field1' : 'data1' , 'field2' : 'data2'} , { 'field1' : 'data3' , 'field2' : 'data4'}]
	return Webpage('name.html', name = location, testdata = testdata)

#-----------------------------------------------

website.run(debug=True) #, host='0.0.0.0')
