# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from symbol_manager.API.Protos import api_pb2 as symbol__manager_dot_API_dot_Protos_dot_api__pb2

GRPC_GENERATED_VERSION = '1.72.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in symbol_manager/API/Protos/api_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PostSymbol = channel.unary_unary(
                '/api.Api/PostSymbol',
                request_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.PostSymbolRequest.SerializeToString,
                response_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.PostSymbolResponse.FromString,
                _registered_method=True)
        self.GetSymbols = channel.unary_unary(
                '/api.Api/GetSymbols',
                request_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetSymbolsRequest.SerializeToString,
                response_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetSymbolsResponse.FromString,
                _registered_method=True)
        self.GetActiveSymbols = channel.unary_unary(
                '/api.Api/GetActiveSymbols',
                request_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetActiveSymbolsRequest.SerializeToString,
                response_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetActiveSymbolsResponse.FromString,
                _registered_method=True)
        self.ToggleSymbolActivation = channel.unary_unary(
                '/api.Api/ToggleSymbolActivation',
                request_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.ToggleSymbolActivationRequest.SerializeToString,
                response_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.ToggleSymbolActivationResponse.FromString,
                _registered_method=True)


class ApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PostSymbol(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSymbols(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActiveSymbols(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ToggleSymbolActivation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PostSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.PostSymbol,
                    request_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.PostSymbolRequest.FromString,
                    response_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.PostSymbolResponse.SerializeToString,
            ),
            'GetSymbols': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSymbols,
                    request_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetSymbolsRequest.FromString,
                    response_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetSymbolsResponse.SerializeToString,
            ),
            'GetActiveSymbols': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActiveSymbols,
                    request_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetActiveSymbolsRequest.FromString,
                    response_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetActiveSymbolsResponse.SerializeToString,
            ),
            'ToggleSymbolActivation': grpc.unary_unary_rpc_method_handler(
                    servicer.ToggleSymbolActivation,
                    request_deserializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.ToggleSymbolActivationRequest.FromString,
                    response_serializer=symbol__manager_dot_API_dot_Protos_dot_api__pb2.ToggleSymbolActivationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.Api', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('api.Api', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Api(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PostSymbol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.Api/PostSymbol',
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.PostSymbolRequest.SerializeToString,
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.PostSymbolResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.Api/GetSymbols',
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetSymbolsRequest.SerializeToString,
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetSymbolsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetActiveSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.Api/GetActiveSymbols',
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetActiveSymbolsRequest.SerializeToString,
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.GetActiveSymbolsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ToggleSymbolActivation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.Api/ToggleSymbolActivation',
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.ToggleSymbolActivationRequest.SerializeToString,
            symbol__manager_dot_API_dot_Protos_dot_api__pb2.ToggleSymbolActivationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
