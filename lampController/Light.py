from .Led import Led


class Light:
    def __init__(self, light_id=0, red=(0, 0), green=(0, 0), blue=(0, 0), warm_white=(0, 0), cold_white=(0, 0)):
        """
        :param light_id: Id of the light
        :param red: (dim, color)
        :param green: (dim, color)
        :param blue: (dim, color)
        :param warm_white: (dim, color)
        :param cold_white: (dim, color)
        """
        self.id = light_id
        self.red = Led(red)
        self.green = Led(green)
        self.blue = Led(blue)
        self.warm_white = Led(warm_white)
        self.cold_white = Led(cold_white)

    def __str__(self):
        result = str(
            f'id: {self.id} \n' +
            f'red: {str(self.red)} \n' +
            f'green: {str(self.green)} \n' +
            f'blue: {str(self.blue)} \n' +
            f'warm_white: {str(self.warm_white)} \n' +
            f'cold_white: {str(self.cold_white)} \n' +
            '================== \n'
        )
        return result

    # Set all the lamps with 1 array
    def set_with_array(self, array):
        if not len(array) == 10:
            raise Exception("set_with_array takes an array of 10 numbers")
        self.red.dim = array[0]
        self.red.color = array[1]
        self.green.dim = array[2]
        self.green.color = array[3]
        self.blue.dim = array[4]
        self.blue.color = array[5]
        self.warm_white.dim = array[6]
        self.warm_white.color = array[7]
        self.cold_white.dim = array[8]
        self.cold_white.color = array[9]

    def build_byte_array(self):
        return (
                self.red.build_byte_array() +
                self.green.build_byte_array() +
                self.blue.build_byte_array() +
                self.warm_white.build_byte_array() +
                self.cold_white.build_byte_array()
        )
