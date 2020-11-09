from lamp import Lamp as library

def main():
    lamp = library.Lamp(0, '192.168.4.204', 4210)

    # Print the entire data structure (usefull for debugging)
    # print(lamp)

    # Get a single light
    single_light = lamp.get_light(5)
    print(f'Single light:\n{single_light}')

    # Update the light
    single_light.red.dim = 16
    single_light.red.color = 55

    lamp.update_light(single_light)
    print(f'Updated light:\n{single_light}')
    lamp.clear_light(5)
    print(f'Cleared light:\n{lamp.get_light(5)}')

    # Get a single light
    single_light = lamp.get_light(5)
    # Update the light
    single_light.set_with_array([5,20,16,55,5,25,0,0,0,0])
    print(single_light)
    
    lamp.update_light(single_light)

    byte_array = lamp.build_byte_array()

    print(f'Byte array:\n{byte_array}')

    # You can uncomment these lines to test the exceptions
    # lamp.get_light(69).red.dim = 2
    # lamp.get_light(2).red.dim = 17
    # lamp.get_light(2).red.color = 256


if __name__ == "__main__":
    main()
