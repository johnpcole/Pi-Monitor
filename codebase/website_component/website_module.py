from flask import Flask as Webserver
from flask import render_template as Webpage

website = Webserver(__name__)

#-----------------------------------------------

@website.route('/')
def indexpage():
	return Webpage('index.html')

#-----------------------------------------------

@website.route('/<location>')
def namepage(location):
	return Webpage('name.html', name=location)

#-----------------------------------------------
