class Led:
    def __init__(self,dim=0,color=0):
        self.dim = dim
        self.color = color

    def __repr__(self):
        return str([self.dim, self.color])
    
    def __str__(self):
        return 'dim: {}, color: {}'.format(self.dim, self.color)

    def build_byte_array(self):
        return [self.dim,self.color]

    @property
    def dim(self):
        return self._dim

    @dim.setter
    def dim(self,val):
        if val < 0 or val > 16: 
            raise Exception("Dim needs to be in rage 0-16")
        self._dim = val

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,val):
        if val < 0 or val > 255: 
            raise Exception("Color needs to be in range 0-255")
        self._color = val
