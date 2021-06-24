import time
import zmq
from user.user import User
import json

class Application:

    def __init__(self):
        self.context = zmq.Context()
        self.users = self.createDummyUsers()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")

    def createDummyUsers(self) -> dict:
        hans = User("Hans", "user", "awsd")
        peter = User("Peter", "superuser", "1234")
        users = {"Hans": hans, "Peter": peter}
        return users

    def authenticateUser(self) -> bool:
        message = self.socket.recv_json()
        if message["Task"] == "Authentication":
            if message["Password"] == self.users[message["Name"]].password:
                authentication_msg = {"Authentication": True}
                self.socket.send_json(authentication_msg)
                return True
            else:
                authentication_msg = {"Authentication": True}
                self.socket.send_json(authentication_msg)
                return

        return False

context = zmq.Context()

def createDummyUsers() -> dict:
    hans = User("Hans", "user", "awsd")
    peter = User("Peter", "superuser", "1234")
    users = {"Hans": hans, "Peter": peter}
    return users

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    backend_app = Application()

    while not backend_app.authenticateUser():
        message = socket.recv_json()
        print(type(message))
        if message["Task"] == "Authentication":
            if message["Password"] == users[message["Name"]].password:
                authentication = True
                print(message["Name"] + " was authenticated")
                authentication_msg = {"Authentication": True}
                socket.send_json(authentication_msg)

    json_dict = {"Header": "Hello World", "Message": "There once was a ship"}
    while True:
        message = socket.recv_json()
        #print(message)
        #print(message["Request number"])
        time.sleep(1)
        socket.send_json(json_dict)