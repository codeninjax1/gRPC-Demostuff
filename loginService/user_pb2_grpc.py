# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import user_pb2 as user__pb2


class userLoginStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.userCreate = channel.unary_unary(
        '/user.userLogin/userCreate',
        request_serializer=user__pb2.User.SerializeToString,
        response_deserializer=user__pb2.Response.FromString,
        )
    self.userAuth = channel.unary_unary(
        '/user.userLogin/userAuth',
        request_serializer=user__pb2.User.SerializeToString,
        response_deserializer=user__pb2.Response.FromString,
        )


class userLoginServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def userCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def userAuth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_userLoginServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'userCreate': grpc.unary_unary_rpc_method_handler(
          servicer.userCreate,
          request_deserializer=user__pb2.User.FromString,
          response_serializer=user__pb2.Response.SerializeToString,
      ),
      'userAuth': grpc.unary_unary_rpc_method_handler(
          servicer.userAuth,
          request_deserializer=user__pb2.User.FromString,
          response_serializer=user__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'user.userLogin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
