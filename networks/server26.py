import time
import random
import socket


""" This is the server portion of the socket. The protocol specifies
    that it receives te first message as a 'hand-shake', to which it
    reacts with the type of services it provides: It looks for a 4
    letter request asfollows:

    NAME - sends its name,
    TIME - sends the currect time as hh:mm:ss,
    RAND - sends a random integer between 1 and 10.
    EXIT - it quits (closes the connection)
"""
IP = '0.0.0.0'
PORT = 1729
TIME_PRE = '0'
START_HOUR = -13
END_SEC = -5
MESSAGE_SIZE = 4
RAND_LOW = 1
RAND_HIGH = 10


def format_response(response):
    """ The first 4 bytes of the response is its length. so the client
        knows how  many bytes are left for the request.
        Called from:  'serve_requests'
        The returned string
                           NAME:  0020My name is: HAL 9000  length is 20
                           RAND:  00018 len is 1 and rand number is 8
                           TIME:  000821:31:43  length is 8

    """

    m_length = str(len(response))

    m_length = m_length.zfill(MESSAGE_SIZE)

    message_back = m_length + response

    return message_back



def inital_listen():
    """ Run the server and start listening to messages from a client """

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(1)
    return server


def check_client(server):
    client, (ip, port) = server.accept()

    data = client.recv(MESSAGE_SIZE)
    first_response = 'Your options are: TIME, RAND(1-10), NAME or EXIT'
    client.send(first_response)
    '''
    The client is responsible for sending only 4 bytes. We could let it
    send more and indicate back invalid data (see Bad data... message)
    '''
    data = client.recv(MESSAGE_SIZE)
    return client, data


def serve_requests(data, client, server):
    """ Serve requests by the client, as long as they come """

    while True:
        if data == 'TIME':
            response = time.ctime()[START_HOUR:END_SEC]
        elif data == 'RAND':
            response = str(random.randint(RAND_LOW, RAND_HIGH))
        elif data == 'NAME':
            response = 'My name is: HAL 9000'
        elif data == 'EXIT':
            break
        else:
            response = 'Bad data, only: TIME, RAND, NAME or EXIT are allowed'
        message_back = format_response(response)
        client.send(message_back)
        data = client.recv(MESSAGE_SIZE)
    client.close()


def main():
    """
    Gets the first message as a hand-shake, and then loops
    until EXIT is requested, for each request prepares and
    sends the correct response, including a note on invalid
    input.
    """
    server = inital_listen()

    while True:
        client, data = check_client(server)
        try:
            serve_requests(data, client, server)
        except:
            client.close()
    server.close()

if __name__ == '__main__':
    main()
