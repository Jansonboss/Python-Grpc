# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ice_cream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fice_cream.proto\"1\n\x0fIceCreamRequest\x12\x0e\n\x06scoops\x18\x01 \x01(\x05\x12\x0e\n\x06\x66lavor\x18\x02 \x01(\t\"#\n\x10IceCreamResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2@\n\x08IceCream\x12\x34\n\rOrderIceCream\x12\x10.IceCreamRequest\x1a\x11.IceCreamResponseb\x06proto3')



_ICECREAMREQUEST = DESCRIPTOR.message_types_by_name['IceCreamRequest']
_ICECREAMRESPONSE = DESCRIPTOR.message_types_by_name['IceCreamResponse']
IceCreamRequest = _reflection.GeneratedProtocolMessageType('IceCreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _ICECREAMREQUEST,
  '__module__' : 'ice_cream_pb2'
  # @@protoc_insertion_point(class_scope:IceCreamRequest)
  })
_sym_db.RegisterMessage(IceCreamRequest)

IceCreamResponse = _reflection.GeneratedProtocolMessageType('IceCreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _ICECREAMRESPONSE,
  '__module__' : 'ice_cream_pb2'
  # @@protoc_insertion_point(class_scope:IceCreamResponse)
  })
_sym_db.RegisterMessage(IceCreamResponse)

_ICECREAM = DESCRIPTOR.services_by_name['IceCream']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ICECREAMREQUEST._serialized_start=19
  _ICECREAMREQUEST._serialized_end=68
  _ICECREAMRESPONSE._serialized_start=70
  _ICECREAMRESPONSE._serialized_end=105
  _ICECREAM._serialized_start=107
  _ICECREAM._serialized_end=171
# @@protoc_insertion_point(module_scope)
