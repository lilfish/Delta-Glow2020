class Led:

    def __init__(self, values=(0, 0)):
        """
        :param values: (dim, color)
        """
        self.dim = values[0]
        self.color = values[1]

    def __repr__(self):
        return str([self.dim, self.color])
    
    def __str__(self):
        return 'dim: {}, color: {}'.format(self.dim, self.color)

    def build_byte_array(self):
        return [self.dim, self.color]

    @property
    def dim(self):
        return self._dim

    @dim.setter
    def dim(self, val):
        if val < 0 or val > 16: 
            raise Exception("Dim needs to be in rage 0-16")
        self._dim = val

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        if val < 0 or val > 255: 
            raise Exception("Color needs to be in range 0-255")
        self._color = val
