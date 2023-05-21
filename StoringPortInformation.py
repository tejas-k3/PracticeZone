# Question : For n users trying to connect to same server, write
# makeConnection and endConnection where make accepts a userId
# and reutrns user available port while end accepts portNmebr
# and frees the port from connection marking it available.

# Assumptions :-
# 1 All ports can be used
# 2 Space complexity is not an issue

MIN_PORT = 0
MAX_PORT = 65535

class User:
    __all_users = dict()
    def __init__(self, name, id, port=None):
        name = name
        id = id
        port = port
        User.all_users[id]=self
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_id(self):
        return self.__id
    def set_id(self, id):
        User.__all_users.pop(self.__id)
        self.__id = id
        User.__all_users[id] = self
    def get_port(self):
        return self.__port
    def set_port(self, port):
        self.__port = port

    def getById(self, id):
        try :
            return User.__all_users[id]
        except KeyError:
            return None
    
    @staticmethod
    def get_all_users():
        return User.__all_users

class PortInformation:
    __ports = {
        'available': set([i for i in range(MIN_PORT, MAX_PORT+1)]),
        'unavailable': set()
    }
    def portAllocation(self, userId):
        if self.__ports['available'] > 0:
            portValue = self.__ports['available'].pop()
            User.getById(userId).port = portValue
            self.__ports['unavailable'].add(portValue)
        else:
            print("Cant allocate port, unavailable!")
        return
    def portDeallocation(self, userId):
        user = User.getById(userId)
        if user:
            portValue = user.get_port() 
            user.set_port(None)
            self.__ports['unavailable'].discard(portValue)
            self.__ports['available'].add(portValue)
        else:
            print("Cant deallocate port, unavailable user!")
        return
