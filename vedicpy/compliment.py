from ctypes import CDLL

obj= CDLL('vedicpy/C program files/compliment.so')
    
def compliment_to_power_of10(num: int) -> int:
    return obj.compliment_to_power_of10(num)
