# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bridge.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x62ridge.proto\"\r\n\x0bNullMessage\"[\n\x0cScalarMetric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x1c\n\x01x\x18\x03 \x01(\x0b\x32\x11.ScalarMetric.Arg\x1a\x14\n\x03\x41rg\x12\r\n\x05value\x18\x01 \x01(\x01\"\xb0\x03\n\x04Item\x12!\n\titem_type\x18\x01 \x01(\x0e\x32\x0e.Item.ItemType\x12\x10\n\x08\x64ict_key\x18\x02 \x01(\t\x12\x12\n\nbool_value\x18\x03 \x01(\x08\x12\x11\n\tint_value\x18\x04 \x01(\x12\x12\x13\n\x0b\x66loat_value\x18\x05 \x01(\x01\x12\x11\n\tstr_value\x18\x06 \x01(\t\x12+\n\x11numpy_array_value\x18\x08 \x01(\x0b\x32\x10.Item.NumpyArray\x1a\x46\n\nNumpyArray\x12\x0c\n\x04last\x18\x01 \x01(\x08\x12\r\n\x05\x64type\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x03(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"\xae\x01\n\x08ItemType\x12\r\n\tLIST_OPEN\x10\x00\x12\x0e\n\nLIST_CLOSE\x10\x01\x12\r\n\tDICT_OPEN\x10\x02\x12\x0e\n\nDICT_CLOSE\x10\x03\x12\x08\n\x04NONE\x10\x04\x12\x08\n\x04\x42OOL\x10\x05\x12\x07\n\x03INT\x10\x06\x12\t\n\x05\x46LOAT\x10\x07\x12\x07\n\x03STR\x10\x08\x12\x10\n\x0cNUMPY_INT_32\x10\t\x12\x10\n\x0cNUMPY_INT_64\x10\n\x12\x0f\n\x0bNUMPY_ARRAY\x10\x0b\x32}\n\x06\x42ridge\x12$\n\x04Init\x12\x0c.NullMessage\x1a\x0c.NullMessage\"\x00\x12\x19\n\x03Run\x12\x05.Item\x1a\x05.Item\"\x00(\x01\x30\x01\x12\x32\n\x11StoreScalarMetric\x12\r.ScalarMetric\x1a\x0c.NullMessage\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ITEM_ITEMTYPE = _descriptor.EnumDescriptor(
  name='ItemType',
  full_name='Item.ItemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIST_OPEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_CLOSE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DICT_OPEN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DICT_CLOSE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STR', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMPY_INT_32', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMPY_INT_64', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMPY_ARRAY', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=383,
  serialized_end=557,
)
_sym_db.RegisterEnumDescriptor(_ITEM_ITEMTYPE)


_NULLMESSAGE = _descriptor.Descriptor(
  name='NullMessage',
  full_name='NullMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=16,
  serialized_end=29,
)


_SCALARMETRIC_ARG = _descriptor.Descriptor(
  name='Arg',
  full_name='ScalarMetric.Arg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ScalarMetric.Arg.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=102,
  serialized_end=122,
)

_SCALARMETRIC = _descriptor.Descriptor(
  name='ScalarMetric',
  full_name='ScalarMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ScalarMetric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='ScalarMetric.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='ScalarMetric.x', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SCALARMETRIC_ARG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=122,
)


_ITEM_NUMPYARRAY = _descriptor.Descriptor(
  name='NumpyArray',
  full_name='Item.NumpyArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last', full_name='Item.NumpyArray.last', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='Item.NumpyArray.dtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='Item.NumpyArray.shape', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Item.NumpyArray.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=310,
  serialized_end=380,
)

_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_type', full_name='Item.item_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dict_key', full_name='Item.dict_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='Item.bool_value', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='Item.int_value', index=3,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='Item.float_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_value', full_name='Item.str_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numpy_array_value', full_name='Item.numpy_array_value', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ITEM_NUMPYARRAY, ],
  enum_types=[
    _ITEM_ITEMTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=557,
)

_SCALARMETRIC_ARG.containing_type = _SCALARMETRIC
_SCALARMETRIC.fields_by_name['x'].message_type = _SCALARMETRIC_ARG
_ITEM_NUMPYARRAY.containing_type = _ITEM
_ITEM.fields_by_name['item_type'].enum_type = _ITEM_ITEMTYPE
_ITEM.fields_by_name['numpy_array_value'].message_type = _ITEM_NUMPYARRAY
_ITEM_ITEMTYPE.containing_type = _ITEM
DESCRIPTOR.message_types_by_name['NullMessage'] = _NULLMESSAGE
DESCRIPTOR.message_types_by_name['ScalarMetric'] = _SCALARMETRIC
DESCRIPTOR.message_types_by_name['Item'] = _ITEM

NullMessage = _reflection.GeneratedProtocolMessageType('NullMessage', (_message.Message,), dict(
  DESCRIPTOR = _NULLMESSAGE,
  __module__ = 'bridge_pb2'
  # @@protoc_insertion_point(class_scope:NullMessage)
  ))
_sym_db.RegisterMessage(NullMessage)

ScalarMetric = _reflection.GeneratedProtocolMessageType('ScalarMetric', (_message.Message,), dict(

  Arg = _reflection.GeneratedProtocolMessageType('Arg', (_message.Message,), dict(
    DESCRIPTOR = _SCALARMETRIC_ARG,
    __module__ = 'bridge_pb2'
    # @@protoc_insertion_point(class_scope:ScalarMetric.Arg)
    ))
  ,
  DESCRIPTOR = _SCALARMETRIC,
  __module__ = 'bridge_pb2'
  # @@protoc_insertion_point(class_scope:ScalarMetric)
  ))
_sym_db.RegisterMessage(ScalarMetric)
_sym_db.RegisterMessage(ScalarMetric.Arg)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(

  NumpyArray = _reflection.GeneratedProtocolMessageType('NumpyArray', (_message.Message,), dict(
    DESCRIPTOR = _ITEM_NUMPYARRAY,
    __module__ = 'bridge_pb2'
    # @@protoc_insertion_point(class_scope:Item.NumpyArray)
    ))
  ,
  DESCRIPTOR = _ITEM,
  __module__ = 'bridge_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  ))
_sym_db.RegisterMessage(Item)
_sym_db.RegisterMessage(Item.NumpyArray)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class BridgeStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Init = channel.unary_unary(
          '/Bridge/Init',
          request_serializer=NullMessage.SerializeToString,
          response_deserializer=NullMessage.FromString,
          )
      self.Run = channel.stream_stream(
          '/Bridge/Run',
          request_serializer=Item.SerializeToString,
          response_deserializer=Item.FromString,
          )
      self.StoreScalarMetric = channel.unary_unary(
          '/Bridge/StoreScalarMetric',
          request_serializer=ScalarMetric.SerializeToString,
          response_deserializer=NullMessage.FromString,
          )


  class BridgeServicer(object):

    def Init(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Run(self, request_iterator, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def StoreScalarMetric(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_BridgeServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Init': grpc.unary_unary_rpc_method_handler(
            servicer.Init,
            request_deserializer=NullMessage.FromString,
            response_serializer=NullMessage.SerializeToString,
        ),
        'Run': grpc.stream_stream_rpc_method_handler(
            servicer.Run,
            request_deserializer=Item.FromString,
            response_serializer=Item.SerializeToString,
        ),
        'StoreScalarMetric': grpc.unary_unary_rpc_method_handler(
            servicer.StoreScalarMetric,
            request_deserializer=ScalarMetric.FromString,
            response_serializer=NullMessage.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Bridge', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaBridgeServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Init(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Run(self, request_iterator, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def StoreScalarMetric(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaBridgeStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Init(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Init.future = None
    def Run(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    def StoreScalarMetric(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    StoreScalarMetric.future = None


  def beta_create_Bridge_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Bridge', 'Init'): NullMessage.FromString,
      ('Bridge', 'Run'): Item.FromString,
      ('Bridge', 'StoreScalarMetric'): ScalarMetric.FromString,
    }
    response_serializers = {
      ('Bridge', 'Init'): NullMessage.SerializeToString,
      ('Bridge', 'Run'): Item.SerializeToString,
      ('Bridge', 'StoreScalarMetric'): NullMessage.SerializeToString,
    }
    method_implementations = {
      ('Bridge', 'Init'): face_utilities.unary_unary_inline(servicer.Init),
      ('Bridge', 'Run'): face_utilities.stream_stream_inline(servicer.Run),
      ('Bridge', 'StoreScalarMetric'): face_utilities.unary_unary_inline(servicer.StoreScalarMetric),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Bridge_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Bridge', 'Init'): NullMessage.SerializeToString,
      ('Bridge', 'Run'): Item.SerializeToString,
      ('Bridge', 'StoreScalarMetric'): ScalarMetric.SerializeToString,
    }
    response_deserializers = {
      ('Bridge', 'Init'): NullMessage.FromString,
      ('Bridge', 'Run'): Item.FromString,
      ('Bridge', 'StoreScalarMetric'): NullMessage.FromString,
    }
    cardinalities = {
      'Init': cardinality.Cardinality.UNARY_UNARY,
      'Run': cardinality.Cardinality.STREAM_STREAM,
      'StoreScalarMetric': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Bridge', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
