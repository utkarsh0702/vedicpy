from ctypes import CDLL, RTLD_GLOBAL
import os

obj= CDLL(os.path.join(os.getcwd(),'C program files/cube_cuberoot.so'), RTLD_GLOBAL)

def cube_a_number(num: int) -> int:
    return obj.cube_a_number(num)

def cube_2digit_number(num: int) -> int:
    return obj.cube_2digit_number(num)

def cuberoot_under_1000000(num: int) -> int:
    return obj.cuberoot_under_1000000(num)

