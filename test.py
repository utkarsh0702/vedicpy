import vedicpy as vedic

# Compliment
print('\n---------------Compliment-------------------//')
print(vedic.compliment.compliment_to_power_of10(123))   #877

#Cube abd Cube root
print('\n---------------Cube and Cube Root----------------------//')
print(vedic.cube_cuberoot.cube_2digit_number(45))   #91125
print(vedic.cube_cuberoot.cube_a_number(123))   #1860867
print(vedic.cube_cuberoot.cuberoot_under_1000000(314432))  #68

# Divisibility
print('\n---------------Divisibility-------------------//')
vedic.divisibility.divisibility_under10(228,6)  # The number is divisible

# Division
print('\n---------------Division-------------------//')
vedic.division.division_by9(1234)  # q= 136,  r=1

# Multiply
print('\n---------------Multiply-------------------//')
print(vedic.multiply.multiply_base_near_powerof10(96, 104))  #9984
print(vedic.multiply.multiply_by11(123))  #1353
print(vedic.multiply.multiply_by12(123))  #1476
print(vedic.multiply.multiply_by13(123))  #1599
print(vedic.multiply.multiply_by14(123))  #1722
print(vedic.multiply.multiply_by15(123))  #1845
print(vedic.multiply.multiply_by16(123))  #1968
print(vedic.multiply.multiply_by17(123))  #2091
print(vedic.multiply.multiply_by18(123))  #2214
print(vedic.multiply.multiply_by19(123))  #2337
print(vedic.multiply.multiply_by_9group(123))  #122877
print(vedic.multiply.multiply_equdigit_number(234,456))  #106704
print(vedic.multiply.multiply_sumto10(24, 26))  #624

# Recurring
print('\n---------------Recurring-------------------//')
vedic.recurring.recuring_fractionto_decimal(11, 19)  # 0.578947

# Square and Square root
print('\n---------------Square and Square Root-------------------//')
print(vedic.sq_sqrt.square_ending5(75))  # 5625
print(vedic.sq_sqrt.square_near_powerof10(98))  # 9604
print(vedic.sq_sqrt.square_under100(78))  #6084
print(vedic.sq_sqrt.square_from100_to1000(679))  # 461041
print(vedic.sq_sqrt.perfect_sqrt_under_sqof100(2116))  # 46