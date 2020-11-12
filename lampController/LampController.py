import socket
from .Lamp import Lamp


# This class is responsible for 'clustering' the lamps and sending the data to the lamps
class LampController:
    def __init__(self):
        self.lamps = []
        self.grid = [[]]
        self.lamp_grid_size = [6, 6]

    def __str__(self):
        result = ""
        for row in self.grid:
            result += '['
            for cell in row:
                result += str(cell) + ','
            result += ']\n'
        return result

    def create_lamp(self, ip, port):
        self.lamps.append(Lamp(len(self.lamps), ip, port))

    # Creates the grid to determine which lampController is where
    # [0,1]
    # [2,3]
    def create_grid(self):
        if len(self.lamps) % 2 != 0:
            raise Exception("Amount of lamps is uneven which currently is not supported")

        # Create 2d array based on grid
        cells = 2
        rows = len(self.lamps) // cells  # For now create rows that are 2 wide
        self.grid = [[0] * cells * self.lamp_grid_size[0] for i in range(rows*self.lamp_grid_size[1])]

    def set_cell(self, coordinates, value):
        self.grid[coordinates] = value
