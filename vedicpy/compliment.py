from ctypes import CDLL
import os

path= os.path.abspath(os.path.join( 'vedicpy', 'C program files', 'compliment.so'))
# print(path)
obj= CDLL(path)
    
def compliment_to_power_of10(num: int) -> int:
    return obj.compliment_to_power_of10(num)
