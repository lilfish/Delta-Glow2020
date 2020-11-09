from .Light import Light

# This represents the big lamp
class Lamp:
    def __init__(self,id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port

        # This represents all the small lights in the big lamp, there are 
        self.lights = [Light(id) for id in range(38)]

    # This is called when you try to iterate over the lamp
    def __iter__(self):
        return self.lights
    
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
            raise ArgumentException("Argument must be of type Light")
    
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
        return byte_array