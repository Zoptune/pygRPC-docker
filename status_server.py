
from concurrent import futures
import logging

import grpc
import subprocess
import status_pb2
import status_pb2_grpc
#import status_resources

DOCKER_BRIDGE = '172.17.0.1'
# DOCKER_BRIDGE = '127.0.0.1'
RPC_PORT = '5001'

class StatusServicer(status_pb2_grpc.StatusServicer):
    def GetStatus(self, request, context):
        if(request.module == "list"):
            path = ""
            if(request.optional_data == ""):
                path = "/"
            else:
                path = request.optional_data

            list_files = subprocess.run(["ls", "-l", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return status_pb2.StatusResp(stdout=list_files.stdout, stderr=list_files.stderr, status_code=list_files.returncode)
        elif(request.module == "reboot"):
            list_files = subprocess.run(["reboot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return status_pb2.StatusResp(stdout="reboot request received", stderr="", status_code=0)
        else:
            return status_pb2.StatusResp(stdout="", stderr="unknown module " % request.module, status_code=-1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    status_pb2_grpc.add_StatusServicer_to_server(
        StatusServicer(), server)
    server.add_insecure_port(DOCKER_BRIDGE + ':' + RPC_PORT)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()