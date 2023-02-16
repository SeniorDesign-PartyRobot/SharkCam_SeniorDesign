# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PbBase.proto

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
from . import PbMessages_pb2 as PbMessages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PbBase.proto',
  package='pb',
  syntax='proto3',
  serialized_pb=_b('\n\x0cPbBase.proto\x12\x02pb\x1a\x0ePbConsts.proto\x1a\x10PbMessages.proto\"\xbd\x04\n\x0bPbBaseInput\x12\x0f\n\x07\x62\x61ttery\x18\x01 \x01(\x05\x12\x12\n\x08\x62umpered\x18\x02 \x01(\x05H\x00\x12\x11\n\x07\x63liffed\x18\x03 \x01(\x05H\x01\x12\x17\n\rmagnetTrigger\x18\x04 \x01(\x05H\x02\x12\x14\n\nwaterLevel\x18\x05 \x01(\x05H\x03\x12\x12\n\x08\x64ockCode\x18\x06 \x01(\x05H\x04\x12\x16\n\x0c\x63hargeStatus\x18\x07 \x01(\x05H\x05\x12\x12\n\x08robotKey\x18\x08 \x01(\x05H\x06\x12\x13\n\tBDPSignal\x18\t \x01(\tH\x07\x12\"\n\twaterTank\x18\n \x01(\x0e\x32\r.pb.PbToggleTH\x08\x12\x10\n\x06\x63\x61rpet\x18\x0b \x01(\x05H\t\x12\x15\n\x0b\x64ustBinType\x18\x0c \x01(\x05H\n\x12\x14\n\nchargeType\x18\r \x01(\x05H\x0b\x12\x16\n\x0cmoppingSpeed\x18\x0e \x01(\x05H\x0c\x12\x13\n\tpumpSpeed\x18\x0f \x01(\x05H\rB\r\n\x0bhasBumperedB\x0c\n\nhasCliffedB\x10\n\x0ehasMagnetCliffB\x0f\n\rhasWaterLevelB\r\n\x0bhasDockCodeB\x11\n\x0fhasChargeStatusB\r\n\x0bhasRobotKeyB\x0e\n\x0chasBDPSignalB\x0e\n\x0chasWaterTankB\x0b\n\thasCarpetB\x10\n\x0ehasDustbinTypeB\x0f\n\rhasChargeTypeB\x11\n\x0fhasMoppingSpeedB\x0e\n\x0chasPumpSpeed\"\x90\x06\n\x0cPbBaseOutput\x12\x1c\n\x05twist\x18\x01 \x01(\x0b\x32\x0b.pb.PbTwistH\x00\x12\x11\n\x07\x62\x61seCmd\x18\x02 \x01(\x05H\x01\x12\x12\n\x08\x66\x61nSpeed\x18\x03 \x01(\x05H\x02\x12\x13\n\tpumpSpeed\x18\x04 \x01(\x05H\x03\x12\x18\n\x0erollBrushSpeed\x18\x05 \x01(\x05H\x04\x12\x18\n\x0esideBrushSpeed\x18\x06 \x01(\x05H\x05\x12\x14\n\ncleanSpeed\x18\x07 \x01(\x05H\x06\x12\x18\n\x0e\x66orceWifiLedOn\x18\t \x01(\x08H\x07\x12\x14\n\nwaterLevel\x18\n \x01(\x05H\x08\x12\"\n\twaterTank\x18\x0b \x01(\x0e\x32\r.pb.PbToggleTH\t\x12\x16\n\x0cmoppingSpeed\x18\x0c \x01(\x05H\n\x12\x1f\n\x06\x66\x61nJet\x18\r \x01(\x0e\x32\r.pb.PbToggleTH\x0b\x12\x11\n\x07l01UIID\x18\x0e \x01(\x05H\x0c\x12\x14\n\nobsVoiding\x18\x0f \x01(\x08H\r\x12\x15\n\x0b\x66\x61nJetSpeed\x18\x10 \x01(\x05H\x0e\x12\"\n\tfanJetLED\x18\x11 \x01(\x0e\x32\r.pb.PbToggleTH\x0f\x12 \n\x07padLift\x18\x12 \x01(\x0e\x32\r.pb.PbToggleTH\x10\x12 \n\x07\x61\x65\x64Info\x18\x13 \x01(\x0b\x32\r.pb.PbAedInfoH\x11\x42\n\n\x08hasTwistB\x0c\n\nhasBaseCmdB\r\n\x0bhasFanSpeedB\x0e\n\x0chasPumpSpeedB\x13\n\x11hasRollBrushSpeedB\x13\n\x11hasSideBrushSpeedB\x0f\n\rhasCleanSpeedB\x13\n\x11hasForceWifiLedOnB\x0f\n\rhasWaterLevelB\x0e\n\x0chasWaterTankB\x11\n\x0fhasMoppingSpeedB\x0b\n\thasFanJetB\x0c\n\nhasL01UIIDB\x0f\n\rhasObsVoidingB\x10\n\x0ehasFanJetSpeedB\x0e\n\x0chasFanJetLEDB\x0c\n\nhasPadLiftB\x0e\n\x0chasPbAedInfoB\x02H\x03\x62\x06proto3')
  ,
  dependencies=[PbConsts__pb2.DESCRIPTOR,PbMessages__pb2.DESCRIPTOR,])




_PBBASEINPUT = _descriptor.Descriptor(
  name='PbBaseInput',
  full_name='pb.PbBaseInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='battery', full_name='pb.PbBaseInput.battery', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bumpered', full_name='pb.PbBaseInput.bumpered', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cliffed', full_name='pb.PbBaseInput.cliffed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magnetTrigger', full_name='pb.PbBaseInput.magnetTrigger', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterLevel', full_name='pb.PbBaseInput.waterLevel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dockCode', full_name='pb.PbBaseInput.dockCode', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chargeStatus', full_name='pb.PbBaseInput.chargeStatus', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robotKey', full_name='pb.PbBaseInput.robotKey', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BDPSignal', full_name='pb.PbBaseInput.BDPSignal', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterTank', full_name='pb.PbBaseInput.waterTank', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='carpet', full_name='pb.PbBaseInput.carpet', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dustBinType', full_name='pb.PbBaseInput.dustBinType', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chargeType', full_name='pb.PbBaseInput.chargeType', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moppingSpeed', full_name='pb.PbBaseInput.moppingSpeed', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pumpSpeed', full_name='pb.PbBaseInput.pumpSpeed', index=14,
      number=15, type=5, cpp_type=1, label=1,
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
      name='hasBumpered', full_name='pb.PbBaseInput.hasBumpered',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasCliffed', full_name='pb.PbBaseInput.hasCliffed',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasMagnetCliff', full_name='pb.PbBaseInput.hasMagnetCliff',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWaterLevel', full_name='pb.PbBaseInput.hasWaterLevel',
      index=3, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasDockCode', full_name='pb.PbBaseInput.hasDockCode',
      index=4, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasChargeStatus', full_name='pb.PbBaseInput.hasChargeStatus',
      index=5, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasRobotKey', full_name='pb.PbBaseInput.hasRobotKey',
      index=6, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasBDPSignal', full_name='pb.PbBaseInput.hasBDPSignal',
      index=7, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWaterTank', full_name='pb.PbBaseInput.hasWaterTank',
      index=8, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasCarpet', full_name='pb.PbBaseInput.hasCarpet',
      index=9, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasDustbinType', full_name='pb.PbBaseInput.hasDustbinType',
      index=10, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasChargeType', full_name='pb.PbBaseInput.hasChargeType',
      index=11, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasMoppingSpeed', full_name='pb.PbBaseInput.hasMoppingSpeed',
      index=12, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasPumpSpeed', full_name='pb.PbBaseInput.hasPumpSpeed',
      index=13, containing_type=None, fields=[]),
  ],
  serialized_start=55,
  serialized_end=628,
)


_PBBASEOUTPUT = _descriptor.Descriptor(
  name='PbBaseOutput',
  full_name='pb.PbBaseOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='twist', full_name='pb.PbBaseOutput.twist', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baseCmd', full_name='pb.PbBaseOutput.baseCmd', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fanSpeed', full_name='pb.PbBaseOutput.fanSpeed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pumpSpeed', full_name='pb.PbBaseOutput.pumpSpeed', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rollBrushSpeed', full_name='pb.PbBaseOutput.rollBrushSpeed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sideBrushSpeed', full_name='pb.PbBaseOutput.sideBrushSpeed', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cleanSpeed', full_name='pb.PbBaseOutput.cleanSpeed', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forceWifiLedOn', full_name='pb.PbBaseOutput.forceWifiLedOn', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterLevel', full_name='pb.PbBaseOutput.waterLevel', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterTank', full_name='pb.PbBaseOutput.waterTank', index=9,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moppingSpeed', full_name='pb.PbBaseOutput.moppingSpeed', index=10,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fanJet', full_name='pb.PbBaseOutput.fanJet', index=11,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l01UIID', full_name='pb.PbBaseOutput.l01UIID', index=12,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obsVoiding', full_name='pb.PbBaseOutput.obsVoiding', index=13,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fanJetSpeed', full_name='pb.PbBaseOutput.fanJetSpeed', index=14,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fanJetLED', full_name='pb.PbBaseOutput.fanJetLED', index=15,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='padLift', full_name='pb.PbBaseOutput.padLift', index=16,
      number=18, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aedInfo', full_name='pb.PbBaseOutput.aedInfo', index=17,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='hasTwist', full_name='pb.PbBaseOutput.hasTwist',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasBaseCmd', full_name='pb.PbBaseOutput.hasBaseCmd',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasFanSpeed', full_name='pb.PbBaseOutput.hasFanSpeed',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasPumpSpeed', full_name='pb.PbBaseOutput.hasPumpSpeed',
      index=3, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasRollBrushSpeed', full_name='pb.PbBaseOutput.hasRollBrushSpeed',
      index=4, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasSideBrushSpeed', full_name='pb.PbBaseOutput.hasSideBrushSpeed',
      index=5, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasCleanSpeed', full_name='pb.PbBaseOutput.hasCleanSpeed',
      index=6, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasForceWifiLedOn', full_name='pb.PbBaseOutput.hasForceWifiLedOn',
      index=7, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWaterLevel', full_name='pb.PbBaseOutput.hasWaterLevel',
      index=8, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWaterTank', full_name='pb.PbBaseOutput.hasWaterTank',
      index=9, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasMoppingSpeed', full_name='pb.PbBaseOutput.hasMoppingSpeed',
      index=10, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasFanJet', full_name='pb.PbBaseOutput.hasFanJet',
      index=11, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasL01UIID', full_name='pb.PbBaseOutput.hasL01UIID',
      index=12, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasObsVoiding', full_name='pb.PbBaseOutput.hasObsVoiding',
      index=13, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasFanJetSpeed', full_name='pb.PbBaseOutput.hasFanJetSpeed',
      index=14, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasFanJetLED', full_name='pb.PbBaseOutput.hasFanJetLED',
      index=15, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasPadLift', full_name='pb.PbBaseOutput.hasPadLift',
      index=16, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasPbAedInfo', full_name='pb.PbBaseOutput.hasPbAedInfo',
      index=17, containing_type=None, fields=[]),
  ],
  serialized_start=631,
  serialized_end=1415,
)

_PBBASEINPUT.fields_by_name['waterTank'].enum_type = PbConsts__pb2._PBTOGGLET
_PBBASEINPUT.oneofs_by_name['hasBumpered'].fields.append(
  _PBBASEINPUT.fields_by_name['bumpered'])
_PBBASEINPUT.fields_by_name['bumpered'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasBumpered']
_PBBASEINPUT.oneofs_by_name['hasCliffed'].fields.append(
  _PBBASEINPUT.fields_by_name['cliffed'])
_PBBASEINPUT.fields_by_name['cliffed'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasCliffed']
_PBBASEINPUT.oneofs_by_name['hasMagnetCliff'].fields.append(
  _PBBASEINPUT.fields_by_name['magnetTrigger'])
_PBBASEINPUT.fields_by_name['magnetTrigger'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasMagnetCliff']
_PBBASEINPUT.oneofs_by_name['hasWaterLevel'].fields.append(
  _PBBASEINPUT.fields_by_name['waterLevel'])
_PBBASEINPUT.fields_by_name['waterLevel'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasWaterLevel']
_PBBASEINPUT.oneofs_by_name['hasDockCode'].fields.append(
  _PBBASEINPUT.fields_by_name['dockCode'])
_PBBASEINPUT.fields_by_name['dockCode'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasDockCode']
_PBBASEINPUT.oneofs_by_name['hasChargeStatus'].fields.append(
  _PBBASEINPUT.fields_by_name['chargeStatus'])
_PBBASEINPUT.fields_by_name['chargeStatus'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasChargeStatus']
_PBBASEINPUT.oneofs_by_name['hasRobotKey'].fields.append(
  _PBBASEINPUT.fields_by_name['robotKey'])
_PBBASEINPUT.fields_by_name['robotKey'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasRobotKey']
_PBBASEINPUT.oneofs_by_name['hasBDPSignal'].fields.append(
  _PBBASEINPUT.fields_by_name['BDPSignal'])
_PBBASEINPUT.fields_by_name['BDPSignal'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasBDPSignal']
_PBBASEINPUT.oneofs_by_name['hasWaterTank'].fields.append(
  _PBBASEINPUT.fields_by_name['waterTank'])
_PBBASEINPUT.fields_by_name['waterTank'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasWaterTank']
_PBBASEINPUT.oneofs_by_name['hasCarpet'].fields.append(
  _PBBASEINPUT.fields_by_name['carpet'])
_PBBASEINPUT.fields_by_name['carpet'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasCarpet']
_PBBASEINPUT.oneofs_by_name['hasDustbinType'].fields.append(
  _PBBASEINPUT.fields_by_name['dustBinType'])
_PBBASEINPUT.fields_by_name['dustBinType'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasDustbinType']
_PBBASEINPUT.oneofs_by_name['hasChargeType'].fields.append(
  _PBBASEINPUT.fields_by_name['chargeType'])
_PBBASEINPUT.fields_by_name['chargeType'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasChargeType']
_PBBASEINPUT.oneofs_by_name['hasMoppingSpeed'].fields.append(
  _PBBASEINPUT.fields_by_name['moppingSpeed'])
_PBBASEINPUT.fields_by_name['moppingSpeed'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasMoppingSpeed']
_PBBASEINPUT.oneofs_by_name['hasPumpSpeed'].fields.append(
  _PBBASEINPUT.fields_by_name['pumpSpeed'])
_PBBASEINPUT.fields_by_name['pumpSpeed'].containing_oneof = _PBBASEINPUT.oneofs_by_name['hasPumpSpeed']
_PBBASEOUTPUT.fields_by_name['twist'].message_type = PbMessages__pb2._PBTWIST
_PBBASEOUTPUT.fields_by_name['waterTank'].enum_type = PbConsts__pb2._PBTOGGLET
_PBBASEOUTPUT.fields_by_name['fanJet'].enum_type = PbConsts__pb2._PBTOGGLET
_PBBASEOUTPUT.fields_by_name['fanJetLED'].enum_type = PbConsts__pb2._PBTOGGLET
_PBBASEOUTPUT.fields_by_name['padLift'].enum_type = PbConsts__pb2._PBTOGGLET
_PBBASEOUTPUT.fields_by_name['aedInfo'].message_type = PbMessages__pb2._PBAEDINFO
_PBBASEOUTPUT.oneofs_by_name['hasTwist'].fields.append(
  _PBBASEOUTPUT.fields_by_name['twist'])
_PBBASEOUTPUT.fields_by_name['twist'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasTwist']
_PBBASEOUTPUT.oneofs_by_name['hasBaseCmd'].fields.append(
  _PBBASEOUTPUT.fields_by_name['baseCmd'])
_PBBASEOUTPUT.fields_by_name['baseCmd'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasBaseCmd']
_PBBASEOUTPUT.oneofs_by_name['hasFanSpeed'].fields.append(
  _PBBASEOUTPUT.fields_by_name['fanSpeed'])
_PBBASEOUTPUT.fields_by_name['fanSpeed'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasFanSpeed']
_PBBASEOUTPUT.oneofs_by_name['hasPumpSpeed'].fields.append(
  _PBBASEOUTPUT.fields_by_name['pumpSpeed'])
_PBBASEOUTPUT.fields_by_name['pumpSpeed'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasPumpSpeed']
_PBBASEOUTPUT.oneofs_by_name['hasRollBrushSpeed'].fields.append(
  _PBBASEOUTPUT.fields_by_name['rollBrushSpeed'])
_PBBASEOUTPUT.fields_by_name['rollBrushSpeed'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasRollBrushSpeed']
_PBBASEOUTPUT.oneofs_by_name['hasSideBrushSpeed'].fields.append(
  _PBBASEOUTPUT.fields_by_name['sideBrushSpeed'])
_PBBASEOUTPUT.fields_by_name['sideBrushSpeed'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasSideBrushSpeed']
_PBBASEOUTPUT.oneofs_by_name['hasCleanSpeed'].fields.append(
  _PBBASEOUTPUT.fields_by_name['cleanSpeed'])
_PBBASEOUTPUT.fields_by_name['cleanSpeed'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasCleanSpeed']
_PBBASEOUTPUT.oneofs_by_name['hasForceWifiLedOn'].fields.append(
  _PBBASEOUTPUT.fields_by_name['forceWifiLedOn'])
_PBBASEOUTPUT.fields_by_name['forceWifiLedOn'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasForceWifiLedOn']
_PBBASEOUTPUT.oneofs_by_name['hasWaterLevel'].fields.append(
  _PBBASEOUTPUT.fields_by_name['waterLevel'])
_PBBASEOUTPUT.fields_by_name['waterLevel'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasWaterLevel']
_PBBASEOUTPUT.oneofs_by_name['hasWaterTank'].fields.append(
  _PBBASEOUTPUT.fields_by_name['waterTank'])
_PBBASEOUTPUT.fields_by_name['waterTank'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasWaterTank']
_PBBASEOUTPUT.oneofs_by_name['hasMoppingSpeed'].fields.append(
  _PBBASEOUTPUT.fields_by_name['moppingSpeed'])
_PBBASEOUTPUT.fields_by_name['moppingSpeed'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasMoppingSpeed']
_PBBASEOUTPUT.oneofs_by_name['hasFanJet'].fields.append(
  _PBBASEOUTPUT.fields_by_name['fanJet'])
_PBBASEOUTPUT.fields_by_name['fanJet'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasFanJet']
_PBBASEOUTPUT.oneofs_by_name['hasL01UIID'].fields.append(
  _PBBASEOUTPUT.fields_by_name['l01UIID'])
_PBBASEOUTPUT.fields_by_name['l01UIID'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasL01UIID']
_PBBASEOUTPUT.oneofs_by_name['hasObsVoiding'].fields.append(
  _PBBASEOUTPUT.fields_by_name['obsVoiding'])
_PBBASEOUTPUT.fields_by_name['obsVoiding'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasObsVoiding']
_PBBASEOUTPUT.oneofs_by_name['hasFanJetSpeed'].fields.append(
  _PBBASEOUTPUT.fields_by_name['fanJetSpeed'])
_PBBASEOUTPUT.fields_by_name['fanJetSpeed'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasFanJetSpeed']
_PBBASEOUTPUT.oneofs_by_name['hasFanJetLED'].fields.append(
  _PBBASEOUTPUT.fields_by_name['fanJetLED'])
_PBBASEOUTPUT.fields_by_name['fanJetLED'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasFanJetLED']
_PBBASEOUTPUT.oneofs_by_name['hasPadLift'].fields.append(
  _PBBASEOUTPUT.fields_by_name['padLift'])
_PBBASEOUTPUT.fields_by_name['padLift'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasPadLift']
_PBBASEOUTPUT.oneofs_by_name['hasPbAedInfo'].fields.append(
  _PBBASEOUTPUT.fields_by_name['aedInfo'])
_PBBASEOUTPUT.fields_by_name['aedInfo'].containing_oneof = _PBBASEOUTPUT.oneofs_by_name['hasPbAedInfo']
DESCRIPTOR.message_types_by_name['PbBaseInput'] = _PBBASEINPUT
DESCRIPTOR.message_types_by_name['PbBaseOutput'] = _PBBASEOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbBaseInput = _reflection.GeneratedProtocolMessageType('PbBaseInput', (_message.Message,), dict(
  DESCRIPTOR = _PBBASEINPUT,
  __module__ = 'PbBase_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbBaseInput)
  ))
_sym_db.RegisterMessage(PbBaseInput)

PbBaseOutput = _reflection.GeneratedProtocolMessageType('PbBaseOutput', (_message.Message,), dict(
  DESCRIPTOR = _PBBASEOUTPUT,
  __module__ = 'PbBase_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbBaseOutput)
  ))
_sym_db.RegisterMessage(PbBaseOutput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)