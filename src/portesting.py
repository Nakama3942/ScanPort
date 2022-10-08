import socket


def is_port_open(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))  # Connection attempt
        # s.settimeout(0.05)  # Timeout for a little more speed
    except:
        return False  # Port is closed
    else:
        return True  # Port is opened
