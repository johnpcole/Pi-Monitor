#!/usr/bin/env python
# Import the client module
from deluge.ui.client import client
# Import the reactor module from Twisted - this is for our mainloop
from twisted.internet import reactor
from deluge.log import setupLogger
setupLogger()

# This is a sample script to add a magnet link to a running instance of deluge

# Connect to a daemon running on the localhost
# We get a Deferred object from this method and we use this to know if and when
# the connection succeeded or failed.
d = client.connect(host='127.0.0.1',port=58846,username='yourusername',password='yourpassword')

# We create a callback function to be called upon a successful connection
def on_connect_success(result):
    print "Connection was successful!"
    print "result:", result
    # Disconnect from the daemon once we successfully connect
   
    def on_added_torrent(value, key):
        print "got something..."
        print "%s: %s" % (key, value)
        client.disconnect()
        reactor.stop()
   
   
    magnetlink = "a magnet link here, in the form of magnet:?*"
    client.core.add_torrent_magnet(magnetlink, {}).addCallback(on_added_torrent, magnetlink)
   
   
    #client.core.get_config_value("download_location").addCallback(on_get_config_value, "download_location")
    # Stop the twisted main loop and exit

# We add the callback to the Deferred object we got from connect()
d.addCallback(on_connect_success)

# We create another callback function to be called when an error is encountered
def on_connect_fail(result):
    print "Connection failed!"
    print "result:", result
    reactor.stop()

# We add the callback (in this case it's an errback, for error)
d.addErrback(on_connect_fail)

# Run the twisted main loop to make everything go
reactor.run()
