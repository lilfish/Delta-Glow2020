from .Light import Light
import re


"""This class represents a lampController which controls 36 lights"""

lamp_grid = [[0, 0, 0, 1, 2, 3, 0, 0, 0],
             [0, 0, 4, 5, 6, 7, 8, 0, 0],
             [0, 9, 10, 11, 12, 13, 14, 15, 0],
             [16, 17, 18, 19, 0, 20, 21, 22, 23],
             [0, 24, 25, 26, 27, 28, 29, 30, 0],
             [0, 0, 31, 32, 33, 34, 35, 0, 0],
             [0, 0, 0, 36, 37, 38, 0, 0, 0]]


class Lamp:
    def __init__(self, lamp_id, ip, port):
        self.id = lamp_id
        self.ip = ip
        self.port = port
        # This represents all the small lights in the big lampController, there are
        self.lights = [Light(light_id) for light_id in range(38)]
        self.grid = lamp_grid

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
    def get_light(self, light_id):
        light = self.lights[light_id]
        if not light:
            raise Exception("Light not found")

        return light

    # Save a light
    def update_light(self, new_light):
        if type(new_light) is Light:
            self.lights[new_light.id] = new_light
        else:
            raise Exception("Argument must be of type Light")

    # Clear a single light
    def clear_light(self, light_id):
        self.lights[light_id] = Light(light_id)

    # Clear all lights
    def clear_all_lights(self):
        self.lights = [Light(light_id) for light_id in range(38)]

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
