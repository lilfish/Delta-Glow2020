import lampController


def main():
    field = lampController.LampController()
    field.create_lamp('192.168.4.203', 4210)
    field.create_lamp('192.168.4.204', 4210)
    field.create_grid()
    print(field)

    # lampController = library.Lamp(0, '192.168.4.204', 4210)
    #
    # # Print the entire data structure (usefull for debugging)
    # # print(lampController)
    #
    # # Get a single light
    # single_light = lampController.get_light(5)
    # print(f'Single light:\n{single_light}')
    #
    # # Update the light
    # single_light.red.dim = 16
    # single_light.red.color = 55
    #
    # lampController.update_light(single_light)
    # print(f'Updated light:\n{single_light}')
    # lampController.clear_light(5)
    # print(f'Cleared light:\n{lampController.get_light(5)}')
    #
    # # Get a single light
    # single_light = lampController.get_light(5)
    # # Update the light
    # single_light.set_with_array([5,20,16,55,5,25,0,0,0,0])
    # print(single_light)
    #
    # lampController.update_light(single_light)
    #
    # byte_array = lampController.build_byte_array()
    #
    # print(f'Byte array:\n{byte_array}')
    #
    # # You can uncomment these lines to test the exceptions
    # # lampController.get_light(69).red.dim = 2
    # # lampController.get_light(2).red.dim = 17
    # # lampController.get_light(2).red.color = 256


if __name__ == "__main__":
    main()
