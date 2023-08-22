from __future__ import print_function
import requests
import logging

import grpc
import users_pb2
import users_pb2_grpc


def run():
    # response = []
    response = requests.get('http://localhost:5000/get_users')
    users_list = response.json()
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    for user in users_list:
        print("User ID:", user['id'])
        print("Name:", user['name'])
        print("Email:", user['email'])
        print("Password:", user['password'])
        print("-" * 20)


    # print("Will try to greet world ...")
    # with grpc.insecure_channel("localhost:50051") as channel:
    #     stub = users_pb2_grpc.UsersStub(channel)
    #     response = stub.GetUsers(users_pb2.GetUserRequest())
    # print(response.users)


if __name__ == "__main__":
    # logging.basicConfig()
    run()