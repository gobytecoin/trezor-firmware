# Automatically generated by pb2py
from .. import protobuf as p


class ApplySettings(p.MessageType):
    FIELDS = {
        1: ('language', p.UnicodeType, 0),
        2: ('label', p.UnicodeType, 0),
        3: ('use_passphrase', p.BoolType, 0),
        4: ('homescreen', p.BytesType, 0),
        5: ('passphrase_source', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 25