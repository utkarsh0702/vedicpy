import unittest
from vedicpy import compliment, cube, multiply, square, squareroot, cuberoot

class TestModule(unittest.TestCase):
    #-------------------------compliment-----------------------------
    def test_compliment_to_power_of10(self):
        self.assertEqual(compliment.compliment_num(123), 877)
    
    #--------------------------cube and cube root----------------------
    def test_cube_a_number(self):
        self.assertEqual(cube.cube_using_near_powerof10(103), 1092727)
    
    def test_cube_2digit_number(self):
        self.assertEqual(cube.cube_2digit_number(12), 1728)
    
    def test_cuberoot_under_a_million(self):
        self.assertEqual(cuberoot.cuberoot_under_a_million(314432), 68)
    
    
    def test_cuberoot_under_thousand(self):
        self.assertEqual(cuberoot.cuberoot_under_thousand(275), 6.5463)

    #-----------------------------multiply--------------------------------
    def test_multiply_base_near_powerof10(self):
        self.assertEqual(multiply.multiply_base_near_powerof10(96, 104), 9984)
    
    def test_multiply_by11(self):
        self.assertEqual(multiply.multiply_by11(123), 1353)
    
    def test_multiply_by12(self):
        self.assertEqual(multiply.multiply_by12(123), 1476)
    
    def test_multiply_by13(self):
        self.assertEqual(multiply.multiply_by13(123), 1599)
    
    def test_multiply_by14(self):
        self.assertEqual(multiply.multiply_by14(123), 1722)
    
    def test_multiply_by15(self):
        self.assertEqual(multiply.multiply_by15(123), 1845)
    
    def test_multiply_by16(self):
        self.assertEqual(multiply.multiply_by16(123), 1968)
    
    def test_multiply_by17(self):
        self.assertEqual(multiply.multiply_by17(123), 2091)
    
    def test_multiply_by18(self):
        self.assertEqual(multiply.multiply_by18(123), 2214)
    
    def test_multiply_by19(self):
        self.assertEqual(multiply.multiply_by19(123), 2337)
    
    def test_multiply_by_9group(self):
        self.assertEqual(multiply.multiply_by_9group(123), 122877)
    
    def test_multiply_equdigit_number(self):
        self.assertEqual(multiply.multiply_equdigit_number(234,456), 106704)
    
    def test_multiply_lastdigit_sumto10(self):
        self.assertEqual(multiply.multiply_lastdigit_sumto10(24, 26), 624)
    
    #----------------square and square root------------------
    def test_square_ending5(self):
        self.assertEqual(square.square_ending5(75), 5625)
    
    def test_square_near_powerof10(self):
        self.assertEqual(square.square_near_powerof10(98), 9604)
    
    def test_square_under100(self):
        self.assertEqual(square.square_under100(78), 6084)
    
    def test_square_from100_to1000(self):
        self.assertEqual(square.square_from100_to1000(679), 461041)
    
    def test_perfect_sqrt_under_sqof100(self):
        self.assertEqual(squareroot.perfect_sqrt_under_sqof100(2116), 46)
    

if __name__ == '__main__':
    unittest.main()
