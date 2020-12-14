# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import status_pb2 as status__pb2


class StatusStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStatus = channel.unary_unary(
                '/status.Status/GetStatus',
                request_serializer=status__pb2.StatusReq.SerializeToString,
                response_deserializer=status__pb2.StatusResp.FromString,
                )


class StatusServicer(object):
    """The greeting service definition.
    """

    def GetStatus(self, request, context):
        """Sends status request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatusServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=status__pb2.StatusReq.FromString,
                    response_serializer=status__pb2.StatusResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'status.Status', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Status(object):
    """The greeting service definition.
    """

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/status.Status/GetStatus',
            status__pb2.StatusReq.SerializeToString,
            status__pb2.StatusResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)