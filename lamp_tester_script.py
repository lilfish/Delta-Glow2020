import socket
import sys
import time 

array = []
counter = 0
# prepare bite array
for i in range(410):
    if counter == 0:
        # red dim 16
        array.append(0)
    elif counter == 1:
        #  red 255
        array.append(0)
    elif counter == 2:
        # green dim 16
        array.append(0)
    elif counter == 3:
        # green 0 255
        array.append(0)
    elif counter == 4:
        # blue dim 16
        array.append(0)
    elif counter == 5:
        # blue 0 255
        array.append(0)
    elif counter == 6:
        # warm white dim 16
        array.append(0)
    elif counter == 7:
        # warm white 0 255
        array.append(0)
    elif counter == 8:
        # cold white dim 16
        array.append(0)
    elif counter == 9:
        # cold white 0 255
        array.append(0)
        counter = -1
    counter = counter + 1

HOST = '192.168.4.204'  # Standard loopback interface address (localhost)
PORT = 4210 # Port of the philips lamp

print("UDP target IP: %s" % HOST)
print("UDP target port: %s" % PORT)

try:
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(bytearray(array), (HOST, PORT))
except:
    print("Unexpected error:", sys.exc_info()[0])

print("Done")