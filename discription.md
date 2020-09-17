**vedicpy**
===========

For humans, through regular mathematical steps, solving problems sometimes are complex and time-consuming. But using Vedic Mathematic’s General Techniques (applicable to all sets of given data) and Specific Techniques (applicable to specific sets of given data), numerical calculations can be done very fast.

This package is a python implementation of Vedic mathematical sutras. It uses the Vedic mathematics for performing basic mathematical operations like multiplication, division, square roots, cube roots etc.

This can be used to perform large multiplications and divisions. Though python does not have any restrictions on the size of integers, floats.

Since Vedic maths sutras work on individual digits in a number as opposed to the whole number, the implementation works slower on small digit numbers but works faster on larger digit numbers and some other operations like finding the square root or the cube root of a number.

-   **Documentation:** <https://vedic.readthedocs.io/en/latest/?badge=latest>
-   **Source Code:** <https://github.com/utkarsh0702/vedicpy>

**Implementation**
------------------

**1. Installation**
``` python
pip install vedicpy
```

**2. Usage**
``` python
import vedicpy as vedic
a= vedic.cube_cuberoot.cube_2digit_number(43)
print(a)
```

**Available Functionalities**
-----------------------------

- Vedic Multiplication
- Vedic Division
- Square and Square Root
- Cube and Cube Root
- Divisibility
- Recurring fractions
- Compliment
