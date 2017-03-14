from flask import Flask as Webserver
#from flask import render_template as Webpage

website = Webserver(__name__)
from views import
#==================================================

@website.route('/')
def indexpage():
	return Webpage('index.html')

#-----------------------------------------------

@website.route('/<location>')
def namepage(location):
	return Webpage('name.html', name=location)

#==================================================

if __name__ == '__main__':
	website.run(debug=True, host='0.0.0.0')
