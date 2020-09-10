from ctypes import CDLL

obj= CDLL('vedicpy/C program files/compliment.so')
    
def compliment_to_power_of10(self, num: int) -> int:
    return self.obj.compliment_to_power_of10(num)
