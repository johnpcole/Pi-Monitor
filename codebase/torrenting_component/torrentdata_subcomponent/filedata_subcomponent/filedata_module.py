from . import filedata_class as FileDataClass


def createitem(fileid, path):
	return FileDataClass.DefineFileItem(fileid, path)

