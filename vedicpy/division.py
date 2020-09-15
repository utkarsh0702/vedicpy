from ctypes import CDLL

obj= CDLL('/home/utkarsh/Desktop/vedicpy/vedicpy/C program files/division.so')

def division_by9(num: int):
    obj.division_by9(num)
