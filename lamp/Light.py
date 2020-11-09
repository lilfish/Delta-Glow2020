from .Led import Led

class Light:
    def __init__(self, id):
        self.id = id
        self.red = Led()
        self.green = Led()
        self.blue = Led()
        self.warm_white = Led()
        self.cold_white = Led()

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

    def build_byte_array(self):
        return (
            self.red.build_byte_array() + 
            self.green.build_byte_array() + 
            self.blue.build_byte_array() + 
            self.warm_white.build_byte_array() + 
            self.cold_white.build_byte_array()
        )