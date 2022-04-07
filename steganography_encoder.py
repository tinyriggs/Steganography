import json
import string
import numpy
import logging
from PIL import Image
# from matplotlib import image, pyplot

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

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


def get_image_array(image_path : string):
    picture = Image.open(image_path)
    return numpy.array(picture)

# numpy.binary_repr(int) returns the int as binary
# int("binary", 2) returns binary as int


pixel_data = get_image_array("picture.png")


test_string = "IS this string going to work now"

test_binary = message_to_binary(test_string + "####")

def encode_binary_to_picture(binary, pixel_data):
    pixel_count1 = 0
    pixel_count2 = 0
    binary = list(binary)
    while len(binary) > 0:
        holder = numpy.binary_repr(pixel_data[0][pixel_count2][pixel_count1])
        holder = holder[:7] + binary.pop(0)
        pixel_data[0][pixel_count2][pixel_count1] = int(holder, 2)
        if pixel_count1 < 2:
            pixel_count1 += 1
        else:
            pixel_count1 = 0
            pixel_count2 += 1
    return pixel_data




# binary.pop(0)

# encode_binary_to_picture(test_binary, pixel_data)

# string[:7] + "Q" puts q in the 8th spot of the string

encoded_data = encode_binary_to_picture(test_binary, pixel_data)

Image.fromarray(encoded_data).save("finished_picture.png")
