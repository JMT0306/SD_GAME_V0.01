from stub.client_stub import ClientMathServer
from client import Client
from socket_impl.sockets import Socket
from stub import SERVER_ADDRESS
from stub import PORT

def main():
    #socket = Socket(SERVER_ADDRESS,PORT)
    #socket = Socket.create_client_connection(SERVER_ADDRESS,PORT)
    stub = ClientMathServer(SERVER_ADDRESS, PORT)
    _client = Client(stub)
    _client.run()


if __name__=="__main__":
    main()