
from concurrent import futures
import logging
from flask import Flask, jsonify
import grpc
import users_pb2
import users_pb2_grpc
app = Flask(__name__)

class Users(users_pb2_grpc.UsersServicer):
 def GetUsers(self, request, context):
    return users_pb2.GetUserResponse( users=[
        users_pb2.User(id='1', 
                       name="John Doe",
                         email="abc",
                         password="abc123",)
    ])


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
@app.route('/get_users', methods=['GET'])
def get_users():
    # You can make a gRPC call here to the Users service
    # and return the response as JSON
    users_response = Users().GetUsers(None, None)
    users_list = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
        for user in users_response.users
    ]
    return jsonify(users_list)

if __name__ == "__main__":
    logging.basicConfig()
    # serve()
    # Start the gRPC server in a separate thread
import threading
grpc_thread = threading.Thread(target=serve)
grpc_thread.start()
    
    # Start the Flask app
app.run(host='0.0.0.0', port=5000)