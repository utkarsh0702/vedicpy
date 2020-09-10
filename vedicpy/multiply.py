from ctypes import CDLL

obj= CDLL("vedicpy/C program files/multiply.so")


def multiply_by11(num: int) -> int:
    return obj.multiply_by11(num)

def multiply_by12(num: int) -> int:
    return obj.multiply_by12(num)

def multiply_by13(num: int) -> int:
    return obj.multiply_by13(num)

def multiply_by14(num: int) -> int:
    return obj.multiply_by14(num)

def multiply_by15(num: int) -> int:
    return obj.multiply_by15(num)

def multiply_by16(num: int) -> int:
    return obj.multiply_by16(num)

def multiply_by17(num: int) -> int:
    return obj.multiply_by17(num)

def multiply_by18(num: int) -> int:
    return obj.multiply_by18(num)

def multiply_by19(num: int) -> int:
    return obj.multiply_by19(num)

def multiply_by_9group(num: int) -> int:
    return obj.multiply_by_9group(num)

def multiply_sumto10(num1: int, num2: int) -> int:
    return obj.multiply_sumto10(num1, num2)

def multiply_base_near_powerof10(num1: int, num2: int) -> int:
    return obj.multiply_base_near_powerof10(num1, num2)

def multiply_equdigit_number(num1: int, num2: int) -> int:
    return obj.multiply_equdigit_number(num1, num2)
