from deluge_client import DelugeRPCClient as DelugeDaemonInterface

class DefineDelugeInterface:

	def __init__(self, address, port, username, password):

		self.delugeinterface = DelugeDaemonInterface(address, port, username, password)

# =========================================================================================

	def openconnection(self):

		self.delugeinterface.connect()
		return self.delugeinterface.connected

# =========================================================================================

	def closeconnection(self):

		self.delugeinterface.disconnect()
		return self.delugeinterface.connected

# =========================================================================================

	def gettorrentlist(self):

		return self.delugeinterface.call('core.get_session_state')

# =========================================================================================

	def gettorrentdata(self, torrentid):

		return self.delugeinterface.call('core.get_torrent_status', torrentid, self.getdelugekeys)

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

