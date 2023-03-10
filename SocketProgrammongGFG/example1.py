# ví dụ về script (mã) kết nối với google

import socket
import sys

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket successfully created!")
except socket.error as err:
    print("Socket creation failed with error: ", err)

port = 80
try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    # ngắt kết nối wifi (kết nối mạng để nhảy vào trường hợp này)
    print("There was an error resolving the host")
    sys.exit()

s.connect((host_ip,port))

print("The socket has successfully connected to the google!")