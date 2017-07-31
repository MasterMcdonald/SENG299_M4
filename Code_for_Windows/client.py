#client code
"""
client clode
Author: Haotian Shen
Editor: Zelan Xiang
"""
import socket
import sys
import select


def send(actions, msgs):
    """
    The send method is to merge the action and message, and send it to server.
    """
    message = actions + msgs
    S.send(message)
    return


#HOST = '134.87.190.80'
#HOST = '192.168.56.1'
#HOST = '10.255.255.174'
HOST = socket.gethostname()
PORT = 10000
ADDRESS = (HOST, PORT)
MSG = ''
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.connect(ADDRESS)
print "Client starts now"
print "================="

while True:
    #receive()
    READ_LIST = [sys.stdin, S]
    #sys.stdout.write('\n[You]: ')
    #READ, WRITE, ERROR = select.select(READ_LIST, [], [])
    for sock in READ_LIST:
        if sock == S:
            try: 
                data = sock.recv(1024)
                if data:
                    sys.stdout.write(data)
                #sys.stdout.write('\n[You]: ')
                    sys.stdout.flush()
                else:
                    print "disconnected"
                    sys.exit()
            except:
                sys.exit()
        else:
            userinput = sys.stdin.readline()
            input_split = userinput.split(" ")
            if len(input_split) > 1:
                MSG = str(input_split[1:])
            #aprint ("ok" + userinput)

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
                MSG = input_split[0:]
                MSG = reduce((lambda x, y: x+' '+y), MSG)
            try:
                send(action, MSG)
            except:
                print "disconnected"
                sys.exit()
            #sys.stdout.write(userinput)
            sys.stdout.flush()
            #print "finish"
