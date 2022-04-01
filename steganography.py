

def string_to_binary(message):
    answer = "".join(format(ord(i), "08b") for i in message)
    return answer

def binary_to_string(message):
    n = int(message, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode()

