import time
import datetime


class User:
    __userInformation = {
        "name": "",
        "role": "",
        "password": "",
        "time": datetime.datetime.now()
    }

    def __init__(self, name: str, role: str, password: str):
        self.__userInformation["name"] = name
        self.__userInformation["role"] = role
        self.__userInformation["password"] = password
        self.__userInformation["time"] = datetime.datetime.now()

    def getUserInformation(self) -> dict:
        return self.__userInformation

    def getPassword(self) -> str:
        return self.__userInformation["password"]

    def getName(self) -> str:
        return self.__userInformation["name"]

    password = property(getPassword)
    name = property(getName)