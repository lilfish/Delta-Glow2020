from .Light import Light
from .Errors import OutOfBoundsError
import math
import re
import copy

"""This class represents a lampController which controls 38 lights"""
lamp_grid = [[-1, -1, -1, 15, 0, 1, -1, -1, -1],
             [-1, -1, 14, 27, 16, 17, 2, -1, -1],
             [-1, 13, 26, 35, 28, 29, 18, 3, -1],
             [12, 25, 34, 37, -1, 38, 30, 19, 4],
             [-1, 11, 24, 33, 32, 31, 20, 5, -1],
             [-1, -1, 10, 23, 22, 21, 6, -1, -1],
             [-1, -1, -1, 9, 8, 7, -1, -1, -1]]


class Lamp:
    def __init__(self, lamp_id: int, x: int, y: int, radius: int, ip: str, port: str):
        self.id = lamp_id
        self.x = x
        self.y = y
        self.radius = radius
        self.ip = ip
        self.port = port
        # This represents all the small lights in the big lampController, there are
        self.lights = [Light(light_id) for light_id in range(0, 38)]
        self.grid = lamp_grid

    # This is called when you try to iterate over the lampController
    def __iter__(self):
        return iter(self.lights)

    # Return all data in a readable format
    def __str__(self):
        result = ""
        for light in self.lights:
            result = result + str(light)
        return result

    # Find a single light
    def get_light(self, light_id: int):
        light = self.lights[light_id]
        if not light:
            raise Exception("Light not found")

        return light

    def set_all(self, new_light: Light):
        for i, light in enumerate(self.lights):
            new_light.id = i
            self.lights[i] = copy.copy(new_light)

    # Clear a single light
    def clear_light(self, light_id: int):
        self.lights[light_id] = Light(light_id)

    # Clear all lights
    def clear_all_lights(self):
        self.lights = [Light(light_id) for light_id in range(39)]

    # This is called when you try to get a string
    def build_byte_array(self):
        byte_array = []
        for light in self.lights:
            byte_array = byte_array + light.build_byte_array()
        return bytearray(byte_array)

    # Save a light
    def update_light(self, x: int, y: int, new_light: Light):
        if type(new_light) is Light:
            # Get the id of the light that should be updated
            light_id = self.__convert_coordinates_to_light_id(x, y)
            for i, light in enumerate(self.lights):
                if light.id == light_id:
                    new_light.id = light_id
                    self.lights[light_id] = copy.copy(new_light)
                    break
            result = []
            for light in self.lights:
                result.append(light.id)
        else:
            raise Exception("Argument must be of type Light")

    # Checks if the given coordinate is inside this lamps area.
    def is_inside(self, x: int, y: int) -> bool:
        if math.pow(self.x - x, 2) + math.pow(self.y - y, 2) <= math.pow(self.radius, 2):
            return True
        else:
            return False

    # Converts the x, y of the grid to a light id
    def __convert_coordinates_to_light_id(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            raise OutOfBoundsError
        x_in_circle = round(x - self.x)
        y_in_circle = round(y - self.y)
        light_id = lamp_grid[self.radius-y_in_circle][self.radius+1+x_in_circle]

        if light_id != -1:
            return light_id
        else:
            # Get light closest to the coordinate
            # C is the point we want, we can calculate with this formula
            # A is the base of the circle
            # B is the coordinate in the grid
            # r is the radius of the circle
            # Cx = Ax + r((Bx - Ax) / √((Bx−Ax)^2+(By−Ay)^2))
            # Cy = Ay + r((By - Ay) / √((Bx−Ax)^2+(By−Ay)^2))
            closest_point_x = self.x + self.radius * ((x - self.x) / math.sqrt((x-self.x)**2 + (y - self.y)**2))
            closest_point_y = self.y + self.radius * ((y - self.y) / math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2))
            return self.__convert_coordinates_to_light_id(math.floor(closest_point_x), math.floor(closest_point_y))

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
