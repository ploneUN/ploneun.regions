from collective.grok import gs
from ploneun.regions import MessageFactory as _

@gs.importstep(
    name=u'ploneun.regions', 
    title=_('ploneun.regions import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ploneun.regions.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
