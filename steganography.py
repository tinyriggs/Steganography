import json
import numpy
from PIL import Image


def message_to_binary(message):
    if type(message) == str:
        return "".join(format(ord(i), "08b") for i in message)
    elif type(message) == dict:
        return "".join(format(ord(i), "08b") for i in json.dumps(message))
    else:
        raise TypeError("Input type not supported")

def binary_to_message(binary):
    n = int(binary, 2)
    string = n.to_bytes((n.bit_length() + 7) // 8, "big").decode()
    if string[0] == "{":
        return json.loads(string)
    else:
        return string


def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values


image = get_image("picture.png")

for i in image:
    print(i)
# print(image.shape)




