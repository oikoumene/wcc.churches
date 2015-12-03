from zope.interface import Interface
from zope import schema

class IProductSpecific(Interface):
    pass


class IWccChurchSettings(Interface):
    
    openmapquest_api_key = schema.TextLine(
        title=u'Open Map Quest API Key',
        default=u''
    )
