import json



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

test_dictionary = {"A" : "test", "B" : "Fuck", "C" : ["hello", "ass"]}




