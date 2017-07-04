from ...fileprocessing_component.filesystem_subcomponent import filesystem_module as FileSystem
import os as OperatingSystem

def gettemperature():
    if FileSystem.concatenatepaths(" ", " ") == " / ":
        result = OperatingSystem.popen('vcgencmd measure_temp').readline()
        outcome = float(result[5:-3])
    else:
        outcome = 45.0
    return outcome


