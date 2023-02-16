# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PbPathPlan.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import PbConsts_pb2 as PbConsts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PbPathPlan.proto',
  package='pb',
  syntax='proto3',
  serialized_pb=_b('\n\x10PbPathPlan.proto\x12\x02pb\x1a\x0ePbConsts.proto\"\x1b\n\x07PPInput\x12\x10\n\x08reserved\x18\x01 \x01(\x05\"\xf4\x01\n\x08PPOutput\x12$\n\x0b\x63leanFinish\x18\x01 \x01(\x0e\x32\r.pb.PbToggleTH\x00\x12#\n\nmoveFinish\x18\x02 \x01(\x0e\x32\r.pb.PbToggleTH\x01\x12#\n\nrectFinish\x18\x03 \x01(\x0e\x32\r.pb.PbToggleTH\x02\x12\x30\n\rppMotionState\x18\x04 \x01(\x0e\x32\x17.pb.PathPlanningMotionTH\x03\x42\x10\n\x0ehasCleanFinishB\x0f\n\rhasMoveFinishB\x0f\n\rhasRectFinishB\x12\n\x10hasPPMotionStateB\x02H\x03\x62\x06proto3')
  ,
  dependencies=[PbConsts__pb2.DESCRIPTOR,])




_PPINPUT = _descriptor.Descriptor(
  name='PPInput',
  full_name='pb.PPInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reserved', full_name='pb.PPInput.reserved', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=67,
)


_PPOUTPUT = _descriptor.Descriptor(
  name='PPOutput',
  full_name='pb.PPOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cleanFinish', full_name='pb.PPOutput.cleanFinish', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moveFinish', full_name='pb.PPOutput.moveFinish', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rectFinish', full_name='pb.PPOutput.rectFinish', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ppMotionState', full_name='pb.PPOutput.ppMotionState', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='hasCleanFinish', full_name='pb.PPOutput.hasCleanFinish',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasMoveFinish', full_name='pb.PPOutput.hasMoveFinish',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasRectFinish', full_name='pb.PPOutput.hasRectFinish',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasPPMotionState', full_name='pb.PPOutput.hasPPMotionState',
      index=3, containing_type=None, fields=[]),
  ],
  serialized_start=70,
  serialized_end=314,
)

_PPOUTPUT.fields_by_name['cleanFinish'].enum_type = PbConsts__pb2._PBTOGGLET
_PPOUTPUT.fields_by_name['moveFinish'].enum_type = PbConsts__pb2._PBTOGGLET
_PPOUTPUT.fields_by_name['rectFinish'].enum_type = PbConsts__pb2._PBTOGGLET
_PPOUTPUT.fields_by_name['ppMotionState'].enum_type = PbConsts__pb2._PATHPLANNINGMOTIONT
_PPOUTPUT.oneofs_by_name['hasCleanFinish'].fields.append(
  _PPOUTPUT.fields_by_name['cleanFinish'])
_PPOUTPUT.fields_by_name['cleanFinish'].containing_oneof = _PPOUTPUT.oneofs_by_name['hasCleanFinish']
_PPOUTPUT.oneofs_by_name['hasMoveFinish'].fields.append(
  _PPOUTPUT.fields_by_name['moveFinish'])
_PPOUTPUT.fields_by_name['moveFinish'].containing_oneof = _PPOUTPUT.oneofs_by_name['hasMoveFinish']
_PPOUTPUT.oneofs_by_name['hasRectFinish'].fields.append(
  _PPOUTPUT.fields_by_name['rectFinish'])
_PPOUTPUT.fields_by_name['rectFinish'].containing_oneof = _PPOUTPUT.oneofs_by_name['hasRectFinish']
_PPOUTPUT.oneofs_by_name['hasPPMotionState'].fields.append(
  _PPOUTPUT.fields_by_name['ppMotionState'])
_PPOUTPUT.fields_by_name['ppMotionState'].containing_oneof = _PPOUTPUT.oneofs_by_name['hasPPMotionState']
DESCRIPTOR.message_types_by_name['PPInput'] = _PPINPUT
DESCRIPTOR.message_types_by_name['PPOutput'] = _PPOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PPInput = _reflection.GeneratedProtocolMessageType('PPInput', (_message.Message,), dict(
  DESCRIPTOR = _PPINPUT,
  __module__ = 'PbPathPlan_pb2'
  # @@protoc_insertion_point(class_scope:pb.PPInput)
  ))
_sym_db.RegisterMessage(PPInput)

PPOutput = _reflection.GeneratedProtocolMessageType('PPOutput', (_message.Message,), dict(
  DESCRIPTOR = _PPOUTPUT,
  __module__ = 'PbPathPlan_pb2'
  # @@protoc_insertion_point(class_scope:pb.PPOutput)
  ))
_sym_db.RegisterMessage(PPOutput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)