from ctypes import CDLL

obj= CDLL("vedicpy/C program files/divisibility.so")


def divisibility_under10(num1: int, num2: int):
    obj.divisibility_under10(num1, num2)
