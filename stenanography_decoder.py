import json
import string
import numpy
import logging
import steganography_encoder as encoder
from PIL import Image


pixel_data = encoder.get_image_array("finished_picture.png")



def decode_picture_to_binary(pixel_data):
    answer = ""
    letter = ""
    hashtag_count = 0
    pixel_count1 = 0
    pixel_count2 = 0
    while hashtag_count < 4:
        holder = numpy.binary_repr(pixel_data[0][pixel_count2][pixel_count1])
        letter += str(holder[7])
        if pixel_count1 < 2:
            pixel_count1 += 1
        else:
            pixel_count1 = 0
            pixel_count2 += 1
        if len(letter) == 8:
            if encoder.binary_to_message(letter) == "#":
                hashtag_count += 1
            answer += encoder.binary_to_message(letter)
            letter = ""
    return answer.removesuffix("####")        



message = decode_picture_to_binary(pixel_data)

print(message)