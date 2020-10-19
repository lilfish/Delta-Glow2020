import cherrypy
import cherrypy_cors
import socket
import sys

class Server(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        result = {"operation": "request", "result": "success"}
        if cherrypy.request.method == 'OPTIONS':
            cherrypy_cors.preflight(allowed_methods=['POST'])
        if cherrypy.request.method == 'POST':
            arr = cherrypy.request.json
            arr = [ int(x) for x in arr ]
            sendData(arr)
        return result

def sendData(array):
    HOST = '192.168.4.204'  # Standard loopback interface address (localhost)
    PORT = 4210 # Port of the philips lamp

    print("Sending data to")
    print("UDP target IP: %s" % HOST)
    print("UDP target port: %s" % PORT)
    print("data:")
    print(bytearray(array))
    try:
        sock = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
        sock.sendto(bytearray(array), (HOST, PORT))
    except:
        print("Unexpected error:", sys.exc_info()[0])
    print("Done")

def main():
    cherrypy_cors.install()
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        'cors.expose.on': True,
    })
    cherrypy.quickstart(Server())


__name__ == '__main__' and main()  # pylint: disable=expression-not-assigned