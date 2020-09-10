from ctypes import CDLL

obj= CDLL('compliment/compliment.so')

def compliment_to_power_of10(num: int) -> int:
    return obj.compliment_to_power_of10(num)
