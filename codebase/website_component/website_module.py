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
	testdata = [{ 'field1' : 'data1' , 'field2' : 'data2'} , { 'field1' : 'data3' , 'field2' : 'data4'}]
	return Webpage('name.html', name = location, testdata = testdata)

#-----------------------------------------------
