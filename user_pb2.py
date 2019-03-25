# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nuser.proto\x12\x04user\"*\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1c\n\x08Response\x12\x10\n\x08response\x18\x01 \x01(\x08\x32\x61\n\tuserLogin\x12*\n\nuserCreate\x12\n.user.User\x1a\x0e.user.Response\"\x00\x12(\n\x08userAuth\x12\n.user.User\x1a\x0e.user.Response\"\x00\x62\x06proto3')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='user.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='user.User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='user.User.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=62,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='user.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='user.Response.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  ))
_sym_db.RegisterMessage(User)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.Response)
  ))
_sym_db.RegisterMessage(Response)



_USERLOGIN = _descriptor.ServiceDescriptor(
  name='userLogin',
  full_name='user.userLogin',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=94,
  serialized_end=191,
  methods=[
  _descriptor.MethodDescriptor(
    name='userCreate',
    full_name='user.userLogin.userCreate',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='userAuth',
    full_name='user.userLogin.userAuth',
    index=1,
    containing_service=None,
    input_type=_USER,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERLOGIN)

DESCRIPTOR.services_by_name['userLogin'] = _USERLOGIN

# @@protoc_insertion_point(module_scope)
