from urllib.request import urlopen as GetWebPage
from urllib.request import Request as GenerateWebRequest
from urllib.request import URLError as WebError
#from json import loads as DecodeJson



class DefineConnector:

	def __init__(self, assetname):

		self.urlendpoint = "http://1.1.1.33:5000/Pi-Monitor/Report=" + assetname

		self.assetname = assetname

		self.maximumtrieslimit = 3


	def reporttohub(self, requestdata):

		if requestdata == "":
			webrequest = GenerateWebRequest(self.urlendpoint)
		else:
			webrequest = GenerateWebRequest(self.urlendpoint, data=requestdata.encode('ascii', 'ignore'))

		tries = 0
		outcome = ""

		while tries < self.maximumtrieslimit:
			try:

				outcome = GetWebPage(webrequest)
				tries = 99999

			except WebError as errorobject:
				tries = tries + 1
				print("Error accessing Hub: ", errorobject.reason)

		if tries == 99999:
			outcome = outcome.read()
			outcome = outcome.decode('utf-8', 'ignore')

		else:
			print("Gave up accessing Hub")

		return outcome




print("Application Started")
HubConnector = DefineConnector("TestAsset")
print(HubConnector.reporttohub("TestString"))
print("Application Ended")

