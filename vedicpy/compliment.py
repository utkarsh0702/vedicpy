from ctypes import CDLL
import os

obj= CDLL(os.path.abspath(os.path.join( 'vedicpy', 'C program files', 'compliment.so')))
    
def compliment_to_power_of10(num: int) -> int:
    return obj.compliment_to_power_of10(num)
