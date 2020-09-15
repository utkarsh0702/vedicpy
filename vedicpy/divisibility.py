from ctypes import CDLL, RTLD_GLOBAL

obj= CDLL('./C program files/divisibility.so', RTLD_GLOBAL)


def divisibility_under10(num: int, divisor: int):
    obj.divisibility_under10(num, divisor)
