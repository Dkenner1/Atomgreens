from EventHub import eventHub
import definitions

def setPiID(msg=None):
    definitions.piID = msg

def lineCheck(msg=None):
    prevLine=True