from ctypes import CDLL, RTLD_GLOBAL

obj= CDLL('./C program files/recurring.so', RTLD_GLOBAL)


def recuring_fractionto_decimal(numerator: int, denominator: int):
    obj.recuring_fractionto_decimal(numerator, denominator)
