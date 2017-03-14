#!/usr/bin/python

#from deluge.log import LOG as log
from deluge.ui.client import client as DelugeClient
import deluge.component as component
from twisted.internet import reactor as NetworkRunner
from twisted.internet import defer as NetworkListener
import time

delugeclientconnection = DelugeClient.connect()


status_keys = ["state",
        "save_path",
        "tracker",
        "tracker_status",
        "next_announce",
        "name",
        "total_size",
        "progress",
        "num_seeds",
        "total_seeds",
        "num_peers",
        "total_peers",
        "eta",
        "download_payload_rate",
        "upload_payload_rate",
        "ratio",
        "distributed_copies",
        "num_pieces",
        "piece_length",
        "total_done",
        "files",
        "file_priorities",
        "file_progress",
        "peers",
        "is_seed",
        "is_finished",
        "active_time",
        "seeding_time"
        ]

count = 0
torrent_ids = []



def printSuccess(successmessage):
	print "[i]", successmessage



def printError(errormessage):
	print "[e]", errormessage



def endSession(endsessionresult):
	if endsessionresult:
		print endsessionresult
	else:
		DelugeClient.disconnect()
		printSuccess("Deluge Client disconnected.")
	NetworkRunner.stop()



def printReport(reportresult):
	printSuccess("TOTAL TORRENTS: %i" % (count))
	endSession(None)



def on_torrents_status(torrents):
    global filtertime
    tlist=[]
    for torrent_id, status in torrents.items():
        printSuccess("Current torrent id is: %s" % (torrent_id))
        printSuccess("--Torrent name is: %s" % (status["name"]))
        printSuccess("--Torrent state is: %s" % (status["state"]))
        printSuccess("--Torrent ratio is: %s" % (status["ratio"]))
        printSuccess("--Torrent DL rate is: %s" % (status["download_payload_rate"]))
        printSuccess("--Torrent UL rate is: %s" % (status["upload_payload_rate"]))
        printSuccess("--Torrent tracker is: %s" % (status["tracker_status"]))
        global count
        count += 1
    NetworkListener.DeferredList(tlist).addCallback(printReport)



def on_session_state(result):
    DelugeClient.core.get_torrents_status({"id": result}, status_keys).addCallback(on_torrents_status)



def on_connect_success(result):
    printSuccess("Connection was successful!")
    curtime = time.time()
    printSuccess("Current unix time is %i" % (curtime))
    DelugeClient.core.get_session_state().addCallback(on_session_state)



delugeclientconnection.addCallbacks(on_connect_success, endSession, errbackArgs=("Connection failed: check settings and try again."))

NetworkRunner.run()