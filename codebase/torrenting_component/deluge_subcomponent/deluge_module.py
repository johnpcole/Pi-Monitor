from . import deluge_class as DelugeInterfaceClass
from . import dummy_class as DummyInterfaceClass



# ---------------------------------------------
# Builds a DelugeRPCClient object
# ---------------------------------------------

def createinterface(address, port, username, password):
	return DelugeInterfaceClass.DefineDelugeInterface(address, port, username, password)



def createdummy():
	return DummyInterfaceClass.DefineDelugeInterface()
