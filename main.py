from lampController import LampController, Light, Errors
import requests
import random
import time

def main():
    field = LampController()
    field.create_lamp(0, 0, 3, '127.0.0.1', 4400)
    field.create_lamp(6, 0, 3, '192.168.4.204', 4210)
    # for i in range(0, 50):
    #     field.clear_lamps()
    #     light = Light.Light(0)
    #     light.set_with_array([0, random.randint(0, 255),
    #                           0, random.randint(0, 255),
    #                           0, random.randint(0, 255),
    #                           0, random.randint(0, 255),
    #                           0, random.randint(0, 255)])
    #     try:
    #         field.update_by_coordinate(random.randint(-3, 3), random.randint(-3, 3), light)
    #     except Errors.OutOfBoundsError:
    #         print("OUT OF BOUNDS")
    #         pass
    #     unity_update(field.get_lamp(1))
    #     time.sleep(.1)

    light = Light.Light(0)
    light.set_with_array([0, 255, 0, 0, 0, 0, 0, 0, 0, 0])
    field.update_by_coordinate(0, 3, light)
    field.update_by_coordinate(0, 2, light)
    field.update_by_coordinate(0, 1, light)
    field.update_by_coordinate(0, -1, light)
    field.update_by_coordinate(0, -2, light)
    field.update_by_coordinate(0, -3, light)

    field.update_by_coordinate(1, 0, light)
    field.update_by_coordinate(2, 0, light)
    field.update_by_coordinate(3, 0, light)
    field.update_by_coordinate(-1, 0, light)
    field.update_by_coordinate(-2, 0, light)
    field.update_by_coordinate(-3, 0, light)
    unity_update(field.get_lamp(1))


def unity_update(lamp):
    url = 'http://localhost:4444'
    json = {'lights': []}
    for light in lamp:
        json['lights'].append({'id': str(light.id), 'value': f'{light.red.color},{light.green.color},{light.blue.color},1)'})

    print(json)

    x = requests.post(url, json=json)

    print(x.text)


if __name__ == "__main__":
    main()
