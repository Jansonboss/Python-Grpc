# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: square_root.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11square_root.proto\"\x17\n\x06Number\x12\r\n\x05input\x18\x01 \x01(\x05\"\x19\n\x06Result\x12\x0f\n\x07resulta\x18\x01 \x01(\x05\x32\x33\n\x11SquareRootService\x12\x1e\n\nsquareRoot\x12\x07.Number\x1a\x07.Resultb\x06proto3')



_NUMBER = DESCRIPTOR.message_types_by_name['Number']
_RESULT = DESCRIPTOR.message_types_by_name['Result']
Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'square_root_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  })
_sym_db.RegisterMessage(Number)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'square_root_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  })
_sym_db.RegisterMessage(Result)

_SQUAREROOTSERVICE = DESCRIPTOR.services_by_name['SquareRootService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NUMBER._serialized_start=21
  _NUMBER._serialized_end=44
  _RESULT._serialized_start=46
  _RESULT._serialized_end=71
  _SQUAREROOTSERVICE._serialized_start=73
  _SQUAREROOTSERVICE._serialized_end=124
# @@protoc_insertion_point(module_scope)