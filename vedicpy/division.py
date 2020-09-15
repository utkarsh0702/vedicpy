from ctypes import CDLL
import os

path= os.path.abspath(os.path.join( 'vedicpy', 'C program files', 'division.so'))
obj= CDLL(path)

def division_by9(num: int):
    obj.division_by9(num)
