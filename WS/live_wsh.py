import time
import json
import random
M_BYE = "TERMINATE"


def web_socket_do_extra_handshake(request):
    pass  # Always accept.


def web_socket_transfer_data(request):
    while True:
        line = request.ws_stream.receive_message()
        if line is None:
            return
        if isinstance(line, unicode):
            # request.ws_stream.send_message(line, binary=False)
            if line == M_BYE:
                return
            elif line == 'r' :
                try :
                    file = open("frame.txt","r")
                    matrix = file.read()
                    file.close()

                    request.ws_stream.send_message(str(matrix), binary=False)
                    # request.ws_stream.send_message(str(random.randint(1,21)), binary=False)
                except :
                    continue
        else:
            return
            request.ws_stream.send_message(line, binary=True)


