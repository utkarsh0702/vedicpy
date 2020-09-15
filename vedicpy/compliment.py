from ctypes import CDLL, RTLD_GLOBAL
import os

obj= CDLL(os.path.join(os.getcwd(),'C program files/compliment.so'), RTLD_GLOBAL)
    
def compliment_to_power_of10(num: int) -> int:
    return obj.compliment_to_power_of10(num)
