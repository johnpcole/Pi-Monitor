#!/usr/bin/python2

from deluge.ui.client import client
from twisted.internet import reactor

d = client.connect()

def on_connect_success(result):
    print "Connection was successful!"
    def on_get_torrent_value(value):

        for torrent in value:
                print "%s: %s" % (torrent, value[torrent]["name"])
        
        client.disconnect()
        reactor.stop()
        
    client.core.get_torrents_status({}, ["name"]).addCallback(on_get_torrent_value)

d.addCallback(on_connect_success)

def on_connect_fail(result):
    print "Connection failed!"
    print "result:", result

d.addErrback(on_connect_fail)

reactor.run()