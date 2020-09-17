![logo](https://github.com/utkarsh0702/vedicpy/blob/master/logo.png)

[![pypi](https://img.shields.io/pypi/v/vedicpy.svg)](https://pypi.python.org/pypi/vedicpy) [![Documentation Status](https://readthedocs.org/projects/vedic/badge/?version=latest)](https://vedic.readthedocs.io/en/latest/?badge=latest) [![Python Versions](https://img.shields.io/pypi/pyversions/vedicpy.svg)](https://pypi.python.org/pypi/vedicpy) [![License](https://img.shields.io/badge/License-BSD%203--Clause-brightgreen.svg)](https://github.com/utkarsh0702/vedicpy/blob/master/LICENSE)

**A Python Package for Vedic Mathematics**

For humans, through regular mathematical steps, solving problems sometimes are complex and time-consuming. But using Vedic Mathematic’s General Techniques (applicable to all sets of given data) and Specific Techniques (applicable to specific sets of given data), numerical calculations can be done very fast.

This package is a python implementation of Vedic mathematical sutras. It uses the Vedic mathematics for performing basic mathematical operations like multiplication, division, square roots, cube roots etc.

Since Vedic maths sutras work on individual digits in a number as opposed to the whole number, the implementation works slower on small digit numbers but works faster on larger digit numbers and some other operations like finding the square root or the cube root of a number.

-   **Documentation:** <https://vedic.readthedocs.io/en/latest/?badge=latest>
-   **Package:** <https://pypi.python.org/pypi/vedicpy>

**How to use it**
-----------------

**1. Installation**

```python
pip install vedicpy
```

**2. Usage**

```python
import vedicpy as vedic
result = vedic.cube_cuberoot.cube_2digit_number(43)
print(result)
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

**Directory Structure**
-------------------------

```
│─── tests
|     │── __init__.py
|     └── test_module.py
│─── vedicpy
|     │── __init__.py
|     │── compliment.py
|     │── cube_cuberoot.py
|     │── divisibility.py
|     │── division.py
|     │── multiply.py
|     │── recurring.py
|     └── sq_sqrt.py
│─── .gitignore
│─── AUTHORS.rst 
│─── CONTRIBUTING.rst 
│─── HISTORY.rst 
│─── LICENSE
│─── MANIFEST.in
│─── README.rst
│─── setup.cfg
└─── setup.py
```

**Contributions**
-----------------

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.
For contributions please read the file [CONTRIBUTING.RST](https://github.com/utkarsh0702/vedicpy/blob/master/CONTRIBUTING.rst)

**Authors**
-----------

- Utkarsh Mishra 
    - Email: <utkarsh.um07@gmail.com>
- Ashish Kumar 
    - Email: <asheesh22@gmail.com>