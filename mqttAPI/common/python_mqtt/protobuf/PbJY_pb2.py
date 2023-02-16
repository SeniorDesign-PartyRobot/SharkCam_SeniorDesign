# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PbJY.proto

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
  name='PbJY.proto',
  package='pb',
  syntax='proto3',
  serialized_pb=_b('\n\nPbJY.proto\x12\x02pb\x1a\x0ePbConsts.proto\"\x83\x02\n\x0bPbDockInput\x12$\n\x08workMode\x18\x01 \x01(\x0e\x32\x10.pb.DockWorkModeH\x00\x12&\n\tworkState\x18\x02 \x01(\x0e\x32\x11.pb.DockWorkStateH\x01\x12\x15\n\x0bmountModule\x18\x03 \x01(\x05H\x02\x12\x1c\n\x12\x63\x61pacityModuleBits\x18\x04 \x01(\x05H\x03\x12\x19\n\x0fstateModuleBits\x18\x05 \x01(\x05H\x04\x42\r\n\x0bhasWorkModeB\x0e\n\x0chasWorkStateB\x10\n\x0ehasMountModuleB\x13\n\x11hasCapacityModuleB\x10\n\x0ehasStateModule\"\xd7\x01\n\x0cPbDockOutput\x12$\n\x08workMode\x18\x01 \x01(\x0e\x32\x10.pb.DockWorkModeH\x00\x12!\n\x03\x43md\x18\x02 \x01(\x0e\x32\x12.pb.DockControlCMDH\x01\x12&\n\tsleepMode\x18\x03 \x01(\x0e\x32\x11.pb.DockSleepModeH\x02\x12\x16\n\x0c\x62\x61\x63kWashArea\x18\x04 \x01(\x05H\x03\x42\r\n\x0bhasWorkModeB\x0c\n\nhasDockCmdB\x0e\n\x0chasSleepModeB\x11\n\x0fhasBackWashArea\"l\n\tPbJYInput\x12$\n\tdockInput\x18\x01 \x01(\x0b\x32\x0f.pb.PbDockInputH\x00\x12\x16\n\x0c\x62\x61\x63kWashArea\x18\x02 \x01(\x05H\x01\x42\x0e\n\x0chasDockInputB\x11\n\x0fhasBackWashArea\"\xb5\x01\n\nPbJYOutput\x12&\n\ndockOutput\x18\x01 \x01(\x0b\x32\x10.pb.PbDockOutputH\x00\x12$\n\x0bisOnStation\x18\x02 \x01(\x0e\x32\r.pb.PbToggleTH\x01\x12$\n\x0b\x62\x61\x63kWashMop\x18\x04 \x01(\x0e\x32\r.pb.PbToggleTH\x02\x42\x0f\n\rhasDockOutputB\x10\n\x0ehasIsOnStationB\x10\n\x0ehasBackWashMopB\x02H\x03\x62\x06proto3')
  ,
  dependencies=[PbConsts__pb2.DESCRIPTOR,])




_PBDOCKINPUT = _descriptor.Descriptor(
  name='PbDockInput',
  full_name='pb.PbDockInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workMode', full_name='pb.PbDockInput.workMode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workState', full_name='pb.PbDockInput.workState', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mountModule', full_name='pb.PbDockInput.mountModule', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacityModuleBits', full_name='pb.PbDockInput.capacityModuleBits', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stateModuleBits', full_name='pb.PbDockInput.stateModuleBits', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
      name='hasWorkMode', full_name='pb.PbDockInput.hasWorkMode',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWorkState', full_name='pb.PbDockInput.hasWorkState',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasMountModule', full_name='pb.PbDockInput.hasMountModule',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasCapacityModule', full_name='pb.PbDockInput.hasCapacityModule',
      index=3, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasStateModule', full_name='pb.PbDockInput.hasStateModule',
      index=4, containing_type=None, fields=[]),
  ],
  serialized_start=35,
  serialized_end=294,
)


_PBDOCKOUTPUT = _descriptor.Descriptor(
  name='PbDockOutput',
  full_name='pb.PbDockOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workMode', full_name='pb.PbDockOutput.workMode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Cmd', full_name='pb.PbDockOutput.Cmd', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sleepMode', full_name='pb.PbDockOutput.sleepMode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backWashArea', full_name='pb.PbDockOutput.backWashArea', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
      name='hasWorkMode', full_name='pb.PbDockOutput.hasWorkMode',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasDockCmd', full_name='pb.PbDockOutput.hasDockCmd',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasSleepMode', full_name='pb.PbDockOutput.hasSleepMode',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasBackWashArea', full_name='pb.PbDockOutput.hasBackWashArea',
      index=3, containing_type=None, fields=[]),
  ],
  serialized_start=297,
  serialized_end=512,
)


_PBJYINPUT = _descriptor.Descriptor(
  name='PbJYInput',
  full_name='pb.PbJYInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dockInput', full_name='pb.PbJYInput.dockInput', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backWashArea', full_name='pb.PbJYInput.backWashArea', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
      name='hasDockInput', full_name='pb.PbJYInput.hasDockInput',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasBackWashArea', full_name='pb.PbJYInput.hasBackWashArea',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=514,
  serialized_end=622,
)


_PBJYOUTPUT = _descriptor.Descriptor(
  name='PbJYOutput',
  full_name='pb.PbJYOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dockOutput', full_name='pb.PbJYOutput.dockOutput', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isOnStation', full_name='pb.PbJYOutput.isOnStation', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backWashMop', full_name='pb.PbJYOutput.backWashMop', index=2,
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
      name='hasDockOutput', full_name='pb.PbJYOutput.hasDockOutput',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasIsOnStation', full_name='pb.PbJYOutput.hasIsOnStation',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasBackWashMop', full_name='pb.PbJYOutput.hasBackWashMop',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=625,
  serialized_end=806,
)

_PBDOCKINPUT.fields_by_name['workMode'].enum_type = PbConsts__pb2._DOCKWORKMODE
_PBDOCKINPUT.fields_by_name['workState'].enum_type = PbConsts__pb2._DOCKWORKSTATE
_PBDOCKINPUT.oneofs_by_name['hasWorkMode'].fields.append(
  _PBDOCKINPUT.fields_by_name['workMode'])
_PBDOCKINPUT.fields_by_name['workMode'].containing_oneof = _PBDOCKINPUT.oneofs_by_name['hasWorkMode']
_PBDOCKINPUT.oneofs_by_name['hasWorkState'].fields.append(
  _PBDOCKINPUT.fields_by_name['workState'])
_PBDOCKINPUT.fields_by_name['workState'].containing_oneof = _PBDOCKINPUT.oneofs_by_name['hasWorkState']
_PBDOCKINPUT.oneofs_by_name['hasMountModule'].fields.append(
  _PBDOCKINPUT.fields_by_name['mountModule'])
_PBDOCKINPUT.fields_by_name['mountModule'].containing_oneof = _PBDOCKINPUT.oneofs_by_name['hasMountModule']
_PBDOCKINPUT.oneofs_by_name['hasCapacityModule'].fields.append(
  _PBDOCKINPUT.fields_by_name['capacityModuleBits'])
_PBDOCKINPUT.fields_by_name['capacityModuleBits'].containing_oneof = _PBDOCKINPUT.oneofs_by_name['hasCapacityModule']
_PBDOCKINPUT.oneofs_by_name['hasStateModule'].fields.append(
  _PBDOCKINPUT.fields_by_name['stateModuleBits'])
_PBDOCKINPUT.fields_by_name['stateModuleBits'].containing_oneof = _PBDOCKINPUT.oneofs_by_name['hasStateModule']
_PBDOCKOUTPUT.fields_by_name['workMode'].enum_type = PbConsts__pb2._DOCKWORKMODE
_PBDOCKOUTPUT.fields_by_name['Cmd'].enum_type = PbConsts__pb2._DOCKCONTROLCMD
_PBDOCKOUTPUT.fields_by_name['sleepMode'].enum_type = PbConsts__pb2._DOCKSLEEPMODE
_PBDOCKOUTPUT.oneofs_by_name['hasWorkMode'].fields.append(
  _PBDOCKOUTPUT.fields_by_name['workMode'])
_PBDOCKOUTPUT.fields_by_name['workMode'].containing_oneof = _PBDOCKOUTPUT.oneofs_by_name['hasWorkMode']
_PBDOCKOUTPUT.oneofs_by_name['hasDockCmd'].fields.append(
  _PBDOCKOUTPUT.fields_by_name['Cmd'])
_PBDOCKOUTPUT.fields_by_name['Cmd'].containing_oneof = _PBDOCKOUTPUT.oneofs_by_name['hasDockCmd']
_PBDOCKOUTPUT.oneofs_by_name['hasSleepMode'].fields.append(
  _PBDOCKOUTPUT.fields_by_name['sleepMode'])
_PBDOCKOUTPUT.fields_by_name['sleepMode'].containing_oneof = _PBDOCKOUTPUT.oneofs_by_name['hasSleepMode']
_PBDOCKOUTPUT.oneofs_by_name['hasBackWashArea'].fields.append(
  _PBDOCKOUTPUT.fields_by_name['backWashArea'])
_PBDOCKOUTPUT.fields_by_name['backWashArea'].containing_oneof = _PBDOCKOUTPUT.oneofs_by_name['hasBackWashArea']
_PBJYINPUT.fields_by_name['dockInput'].message_type = _PBDOCKINPUT
_PBJYINPUT.oneofs_by_name['hasDockInput'].fields.append(
  _PBJYINPUT.fields_by_name['dockInput'])
_PBJYINPUT.fields_by_name['dockInput'].containing_oneof = _PBJYINPUT.oneofs_by_name['hasDockInput']
_PBJYINPUT.oneofs_by_name['hasBackWashArea'].fields.append(
  _PBJYINPUT.fields_by_name['backWashArea'])
_PBJYINPUT.fields_by_name['backWashArea'].containing_oneof = _PBJYINPUT.oneofs_by_name['hasBackWashArea']
_PBJYOUTPUT.fields_by_name['dockOutput'].message_type = _PBDOCKOUTPUT
_PBJYOUTPUT.fields_by_name['isOnStation'].enum_type = PbConsts__pb2._PBTOGGLET
_PBJYOUTPUT.fields_by_name['backWashMop'].enum_type = PbConsts__pb2._PBTOGGLET
_PBJYOUTPUT.oneofs_by_name['hasDockOutput'].fields.append(
  _PBJYOUTPUT.fields_by_name['dockOutput'])
_PBJYOUTPUT.fields_by_name['dockOutput'].containing_oneof = _PBJYOUTPUT.oneofs_by_name['hasDockOutput']
_PBJYOUTPUT.oneofs_by_name['hasIsOnStation'].fields.append(
  _PBJYOUTPUT.fields_by_name['isOnStation'])
_PBJYOUTPUT.fields_by_name['isOnStation'].containing_oneof = _PBJYOUTPUT.oneofs_by_name['hasIsOnStation']
_PBJYOUTPUT.oneofs_by_name['hasBackWashMop'].fields.append(
  _PBJYOUTPUT.fields_by_name['backWashMop'])
_PBJYOUTPUT.fields_by_name['backWashMop'].containing_oneof = _PBJYOUTPUT.oneofs_by_name['hasBackWashMop']
DESCRIPTOR.message_types_by_name['PbDockInput'] = _PBDOCKINPUT
DESCRIPTOR.message_types_by_name['PbDockOutput'] = _PBDOCKOUTPUT
DESCRIPTOR.message_types_by_name['PbJYInput'] = _PBJYINPUT
DESCRIPTOR.message_types_by_name['PbJYOutput'] = _PBJYOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbDockInput = _reflection.GeneratedProtocolMessageType('PbDockInput', (_message.Message,), dict(
  DESCRIPTOR = _PBDOCKINPUT,
  __module__ = 'PbJY_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbDockInput)
  ))
_sym_db.RegisterMessage(PbDockInput)

PbDockOutput = _reflection.GeneratedProtocolMessageType('PbDockOutput', (_message.Message,), dict(
  DESCRIPTOR = _PBDOCKOUTPUT,
  __module__ = 'PbJY_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbDockOutput)
  ))
_sym_db.RegisterMessage(PbDockOutput)

PbJYInput = _reflection.GeneratedProtocolMessageType('PbJYInput', (_message.Message,), dict(
  DESCRIPTOR = _PBJYINPUT,
  __module__ = 'PbJY_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbJYInput)
  ))
_sym_db.RegisterMessage(PbJYInput)

PbJYOutput = _reflection.GeneratedProtocolMessageType('PbJYOutput', (_message.Message,), dict(
  DESCRIPTOR = _PBJYOUTPUT,
  __module__ = 'PbJY_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbJYOutput)
  ))
_sym_db.RegisterMessage(PbJYOutput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)