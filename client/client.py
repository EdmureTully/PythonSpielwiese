
import zmq
from user.user import User

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response

if __name__ == '__main__':

    test = User("Peter", "user", "1234")

    for request in range(1):
        json_dict = {"Task": "Authentication", "Name": "Peter", "Password": "1234"}
        print("Sending request %s …" % request)
        socket.send_json(json_dict)

    #  Get the reply.
        message = socket.recv_json()

        if message["Authentication"]:
            print("Congratulation " + test.name + " was authenticated")
        else:
            print("User was not authenticated. Either wrong password or username.")
        print("Received reply %s [ %s ]" % (request, message))