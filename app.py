# coding=UTF-8
from flask import Flask, jsonify, request, send_from_directory, abort
from flask_cors import CORS
import logging
from wrapt import synchronized
import grpc

import status_pb2
import status_pb2_grpc

# configuration
DEBUG = True

DOCKER_BRIDGE = "172.17.0.1"
# DOCKER_BRIDGE = "127.0.0.1"
RPC_PORT = "5001"

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@synchronized
@app.route('/get/status', methods=['GET'])
def get_status():
    stdout=""
    stderr="rpc error"
    status_code=-1

    with grpc.insecure_channel(DOCKER_BRIDGE + ":" + RPC_PORT) as channel:
        stub = status_pb2_grpc.StatusStub(channel)
        response = stub.GetStatus(status_pb2.StatusReq(module="list", optional_data=""))
        stdout=response.stdout
        stderr=response.stderr
        status_code=response.status_code

    return jsonify(stdout=stdout,
                    stderr=stderr,
                    status_code=status_code)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] : %(message)s')
    app.run(host='0.0.0.0', use_reloader=True)
