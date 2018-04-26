# python ../pywebsocket-master/mod_pywebsocket/standalone.py -p 10333 -w .


def web_socket_do_extra_handshake(request):
    pass  # Always accept.


def web_socket_transfer_data(request):
	return