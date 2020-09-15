from ctypes import CDLL
import os

obj= CDLL(os.path.abspath(os.path.join( 'vedicpy', 'C program files', 'division.so')))

def division_by9(num: int):
    obj.division_by9(num)
