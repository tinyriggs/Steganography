import json
import string
import numpy
import logging
import steganography_encoder as encoder
from PIL import Image


pixel_data = encoder.get_image_array("finished_picture.png")

def decode_picture_to_binary(pixel_data):
    answer = ""
    pixel_count1 = 0
    pixel_count2 = 0
    while len(answer) < 72:
        holder = numpy.binary_repr(pixel_data[0][pixel_count2][pixel_count1])
        answer += str(holder[7])
        if pixel_count1 < 2:
            pixel_count1 += 1
        else:
            pixel_count1 = 0
            pixel_count2 += 1
    return answer        

message_binary = decode_picture_to_binary(pixel_data)

message = encoder.binary_to_message(message_binary)

print(message)