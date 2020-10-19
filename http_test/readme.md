# Delta-lamp demo tool

Here you see the two files that make up the delta-lamp demo tool.  The tool is made out of a `.html` file which has `vue.js` included, and a python file which serves as a bridge between the html file and the lamp by being a small http server.

The `.html` file is a new version of the demo-tool made for the unity3d lamp made in the previous semester.

# HTML - Front-end

As stated above, the front-end is made using vue.js. The reason for this is that vue is easy to use and lightweight which makes it handy to quickly make a tool like this.

There are a few things that happen in the `.html` file that are notable:

**Data**  
The data for the lamp itself is written as an array containing multiple "lamp" json objects. This looks a bit like this:

```json
lamp: [
        {
            id: 0,
            value: [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            color: [
                [0,0,0,1],
                [0,0,0,1],
                [0,0,0,1],
                [0,0,0,1],
                [0,0,0,1],
                [0,0,0,1],
            ]
        }, {
            id: 1,
            value: [
                0,
                0...
```

The id is used to iterate over the lamps in the front-end. The `value` attribute's are the real color values that the lamp can read. The `color` attributes are color values written in rgba format which are used to present the color in the front-end.

**Calculating rgba value**  
Down here you see how the rgba value for the front-end is calculated:

```javascript
rgbas: function() {
    var rgbas = [
        [this.r,    0,  0,  1-0.8/16*this.r_dim],
        [0, this.g, 0,  1-0.8/16*this.g_dim],
        [0, 0,  this.b, 1-0.8/16*this.b_dim],
        [this.ww,   this.ww/100*80, 0+(this.ww/3),   1-0.8/16*this.ww_dim],
        [0+(this.kw/3), 0+(this.kw/2),   this.kw,   1-0.8/16*this.kw_dim]
        ]
    return rgbas
},
```

As you can see, the ww (warm white) and kw (cold white) values are calculated in a different matter than the RGB values. This is done so that it looks like warm and cold white as it looks like in real life.

**Creating lamp-data array**  
Creating the lamp-data array is not that special, but still notable:

```javascript
jsonObject: function(){
    var all_vals = [];
    var fake_led = [0,0,0,0,0,0,0,0,0,0];
    // fill all values in a single array
    this.lamp.forEach(led => {
        all_vals = all_vals.concat(led.value);
    });
    // add 3 more fake leds
    for (let y = 0; y < 3; y++) {
        all_vals = all_vals.concat(fake_led);
    }
    return all_vals;
}
```

As you can see, we create a new empty array called `all_vals`. We fill this array with the `lamp.value` of each lamp (described in ``data`` above). After filling the array, we also fill the array with 30 empty values. The reason we do this is that we need 410 total values to be able to talk to the lamp. 

**Sending data**  

Sending the data is done using XHR. The Python webserver is hosted on port 8080 and has CORS enabled.
```js
 sendUpdate: async function () {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            if (xhr.status == 200) {
                this.updateInfo("Response was 200, updated");
            } else {
                this.updateInfo("Response was not 200, error?");
            }
        }
    }.bind(this);
    xhr.open("POST", 'http://127.0.0.1:8080', true);
    xhr.setRequestHeader('Access-Control-Allow-Headers', '*');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.send(JSON.stringify(this.jsonObject));
    this.updateInfo("Sending update...");
}
```

# Python - HTTP bridge

The python program is quite simple and is written using ``CherryPy`` and ``Socket``. 

**The server itself**  
The server itself listens to `OPTION` and `POST` requests. When a `OPTION` request is send, the server responses with the available methods on the route, which is `POST`. After this demo-tool is allowed to send a `POST` request with the lamp data. 

When the server receives valid JSON data, it will convert each value in the array to a int which can be converted to a bytearray in the ``sendData(arr)`` function.
```python
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
```

**Send data**  
The send function is nothing more then a small function thats send the given array as a bytearray to the lamp using UDP.
```python
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
```

**The rest**  
The last function in the python script is the `main` function. The `main` function starts the http server which listens to port 8080 and has CORS enabled so localhost is allowed to communicate with the server.

```python
def main():
    cherrypy_cors.install()
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        'cors.expose.on': True,
    })
    cherrypy.quickstart(Server())


__name__ == '__main__' and main()  # pylint: disable=expression-not-assigned
```

**Imports**  
Last but not least, these are the imports used to start and run the python server:

```python
import cherrypy
import cherrypy_cors
import socket
import sys
```