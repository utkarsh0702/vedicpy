from ctypes import CDLL, RTLD_GLOBAL

obj= CDLL('./C program files/division.so', RTLD_GLOBAL)

def division_by9(num: int):
    obj.division_by9(num)
