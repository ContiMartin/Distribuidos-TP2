# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import file_system_pb2 as file__system__pb2


class FSStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFiles = channel.unary_unary(
                '/FS/ListFiles',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.PathFiles.FromString,
                )
        self.OpenFile = channel.unary_unary(
                '/FS/OpenFile',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.Boolean.FromString,
                )
        self.ReadFile = channel.unary_unary(
                '/FS/ReadFile',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.File.FromString,
                )
        self.CloseFile = channel.unary_unary(
                '/FS/CloseFile',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.Boolean.FromString,
                )


class FSServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FSServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.PathFiles.SerializeToString,
            ),
            'OpenFile': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenFile,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.Boolean.SerializeToString,
            ),
            'ReadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFile,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.File.SerializeToString,
            ),
            'CloseFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseFile,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.Boolean.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FS', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FS(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/ListFiles',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.PathFiles.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/OpenFile',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.Boolean.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/ReadFile',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.File.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/CloseFile',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.Boolean.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
