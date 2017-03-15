#from torrenting_component import torrenting_module as TorrentManager
from website_component import website_module as WebService

def runapplication():

	WebService.website.run(debug=True) #, host='0.0.0.0')

	#torrentmanager = TorrentManager.createmanager('192.168.1.78', 58846, 'piadmin', 'mypi')


