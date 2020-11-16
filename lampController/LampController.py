import socket
from .Lamp import Lamp
from .Errors import OutOfBoundsError
from .Light import Light

# This class is responsible for 'clustering' the lamps and sending the data to the lamps
class LampController:
    def __init__(self):
        self.lamps = []
        # Initialize socket connection
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __str__(self):
        result = ""
        for lamp in self.lamps:
            result += lamp
        return result

    def create_lamp(self, x: int, y: int, radius: int, ip: str, port: str) -> Lamp:
        new_lamp = Lamp(len(self.lamps) + 1, x, y, radius, ip, port)
        self.lamps.append(new_lamp)
        return new_lamp

    def get_lamp(self, lamp_id: int) -> Lamp:
        for lamp in self.lamps:
            if lamp.id == lamp_id:
                return lamp

    # TODO Currently we ignore points that are not in the circle, \
    #  the functionality is there to calculate the closest point. \
    #  we need to decide if we want to ignore the points or use the \
    #  points that are close with the risk that the point is in 2 circles \
    #  which forces us to loop over all the lamps
    def update_by_coordinate(self, x: int, y: int, light: Light):
        for lamp in self.lamps:
            if lamp.is_inside(x, y):
                lamp.update_light(x, y, light)
                return
        raise OutOfBoundsError

    # Clear all lamps
    def clear_lamps(self):
        for lamp in self.lamps:
            lamp.clear_all_lights()

    # Send the corresponding byteArray to every lamp
    def update_lamps(self):
        for lamp in self.lamps:
            self.socket.sendto(lamp.build_byte_array(), (lamp.ip, lamp.port))
