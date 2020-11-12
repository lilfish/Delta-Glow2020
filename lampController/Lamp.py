from .Light import Light
import re


"""This class represents a lampController which controls 36 lights"""


class Lamp:
    def __init__(self, id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port

        # This represents all the small lights in the big lampController, there are
        self.lights = [Light(id) for id in range(38)]

    # This is called when you try to iterate over the lampController
    def __iter__(self):
        return self.lights

    # Return all data in a readable format
    def __str__(self):
        result = ""
        for light in self.lights:
            result = result + str(light)
        return result

    # Find a single light
    def get_light(self, id):
        light = self.lights[id]
        if not light: raise Exception("Light not found")
        return light

    # Save a light
    def update_light(self, new_light):
        if type(new_light) is Light:
            self.lights[new_light.id] = new_light
        else:
            raise Exception("Argument must be of type Light")

    # Clear a single light
    def clear_light(self, id):
        self.lights[id] = Light(id)

    # Clear all lights
    def clear_lights(self):
        self.lights = [Light(id) for id in range(38)]

    # This is called when you try to get a string
    def build_byte_array(self):
        byte_array = []
        for light in self.lights:
            byte_array = byte_array + light.build_byte_array()
        return bytearray(byte_array)

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, val):
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", val):
            raise Exception("Ip is invalid")
        self._ip = val

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, val):
        if val < 0 or val > 65535:
            raise Exception("Port is invalid")
        self._port = val
