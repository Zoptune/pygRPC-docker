import logging

import grpc

import status_pb2
import status_pb2_grpc

DOCKER_BRIDGE = "172.17.0.1"
RPC_PORT = "5001"

def run():
    with grpc.insecure_channel(DOCKER_BRIDGE + ":" + RPC_PORT) as channel:
        stub = status_pb2_grpc.StatusStub(channel)
        response = stub.GetStatus(status_pb2.StatusReq(module="list", optional_data=""))
    print("stdout: \n" + response.stdout)
    print("stderr: \n" + response.stderr)
    print("status code = " + str(response.status_code))


if __name__ == '__main__':
    logging.basicConfig()
    run()
