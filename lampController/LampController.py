import socket
from .Lamp import Lamp
from .Errors import OutOfBoundsError


# This class is responsible for 'clustering' the lamps and sending the data to the lamps
class LampController:
    def __init__(self):
        self.lamps = []
        # Initialize socket connection
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __str__(self):
        result = ""
        for row in self.lamps:
            result += '['
            for cell in row:
                result += str(cell) + ','
            result += ']\n'
        return result

    def create_lamp(self, x, y, radius, ip, port):
        self.lamps.append(Lamp(len(self.lamps) + 1, x, y, radius, ip, port))

    def get_lamp(self, lamp_id):
        for lamp in self.lamps:
            if lamp.id == lamp_id:
                return lamp

    def update_by_coordinate(self, x, y, light):
        for lamp in self.lamps:
            if lamp.is_inside(x, y):
                lamp.update_light(x, y, light)
                return
        raise OutOfBoundsError

    def clear_lamps(self):
        for lamp in self.lamps:
            lamp.clear_all_lights()

    def set_cell(self, coordinates, value):
        self.grid[coordinates] = value

    def update_lamps(self):
        for lamp in self.lamps:
            self.socket.sendto(lamp.build_byte_array(), (lamp.ip, lamp.port))
