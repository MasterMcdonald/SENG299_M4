#client code
"""
client clode
Druft Author: Haotian Shen
Editor: Zelan Xiang
"""
import socket
import sys
import os

import threading


def send():
    """
    The send method is to merge the action
    and message, and send it to server.
    """
    userinputs = sys.stdin.readline()
    input_split = userinputs.split(" ")
    if len(input_split) > 1:
        msg = str(input_split[1:])
    if input_split[0] == "/quit":
        S.close()
        quit()
    elif input_split[0] == "/create":
        action = '01'
    elif input_split[0] == "/delete":
        action = '02'
    elif input_split[0] == "/join":
        action = '03'
    elif input_split[0] == "/block":
        action = '04'
    elif input_split[0] == "/unblock":
        action = '05'
    elif input_split[0] == "/set_alias":
        action = '06'
    else:
        action = '00'
        msg = input_split[0:]
        msg = reduce((lambda x, y: x+' '+y), msg)
    try:
        message = action + msg
        S.send(message)
    except socket.error:
        TORF[0] = False

def receive():
    """
    The recieve method is to recieve message from server.
    """
    try:
        data = S.recv(1024)
        if data:
            sys.stdout.write(data)
            sys.stdout.flush()
        else:
            TORF[0] = False
    except socket.error:
        TORF[0] = False

HOST = socket.gethostname()
PORT = 10000
ADDRESS = (HOST, PORT)
MSG = ''
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.connect(ADDRESS)
print "Client starts now"
print "================="
TORF = [True]
while TORF[0]:
    RECEIVE = threading.Thread(name="recieve message", target=receive)
    try:
        RECEIVE.start()
    except Exception:
        pass
    SEND = threading.Thread(name="send message", target=send)
    try:
        SEND.start()
    except Exception:
        pass
    sys.stdout.flush()
print "disconnected"
os._exit(0)
