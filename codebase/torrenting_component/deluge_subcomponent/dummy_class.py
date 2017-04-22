#from deluge_client import DelugeRPCClient as DelugeDaemonInterface

class DefineDelugeInterface:

	def __init__(self):

		self.delugeinterface = "Dummy Interface Object"

# =========================================================================================

	def openconnection(self):

		#print "Pretending to connect"
		return True

# =========================================================================================

	def closeconnection(self):

		#print "Pretending to disconnect"
		return False

# =========================================================================================

	def gettorrentlist(self):

		return ('dummytorrent1', 'dummytorrent2', 'dummytorrent3')

# =========================================================================================

	def gettorrentdata(self, torrentid):

		return ({'total_size': 1767583673,
				'state': 'Downloading',
				'save_path': '/Torrents/In Progress',
				'progress': 34.4671020508,
				'files': ({'index': 0, 'path': torrentid + '/Hd.mp4', 'offset': 0, 'size': 1767473159}, {'index': 1, 'path': 'Housebound (2014) [1080p]/WWW.YTS.RE.srt', 'offset': 1767473159, 'size': 110514}, {'index': 22, 'path': 'Housebound (2014) [1080p]/WWW.YTS.RE.jpg', 'offset': 1767473159, 'size': 110514}),
				'name': 'Housebound (2014) [1080p]',
				'eta': 824,
				'is_finished': False})

	# =========================================================================================

	def getdelugekeys(self):
		return ["state", "save_path", "name", "total_size", "progress", "eta", "files", "is_finished"]

		# =========================================================================================

	def getalldelugekeys(self):

		return ["state",
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
				"seeding_time" ]

