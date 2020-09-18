Tutorial
========

This section covers the fundamentals of developing with **vedicpy**, including
a package overview, basic and advanced usage.

Overview
~~~~~~~~

The *vedicpy* package is structured as collection of submodules:

  - vedicpy

    - :ref:`vedicpy.compliment <compliment>`
        Functions for calculating the compliment of a number.

    - :ref:`vedicpy.cube <cube>`
        Functions for calculating cube of a number.

    - :ref:`vedicpy.cuberoot <cuberoot>`
        Functions for checking and calculating cube root of a number.

    - :ref:`vedicpy.divisibility <divisibility>`
        Function for finding whether a number is divisible by the given number or not.

    - :ref:`vedicpy.division <division>`
        Function for calculating quotient and reminder.

    - :ref:`vedicpy.multiply <multiply>`
        Functions for calculating the multiplication of two number using vedic mathematical sutras.

    - :ref:`vedicpy.recurring <recurring>`
        Function for converting fractional number to its corresponding recurring decimal.

    - :ref:`vedicpy.square <square>`
        Functions for calculating square of a number.

    - :ref:`vedicpy.squareroot <squareroot>`
        Functions for checking and calculating square root of a number.


Quickstart
~~~~~~~~~~
Before diving into the details, we'll walk through a brief example program

.. code-block:: python

    # Example of calculating the cube of a number
    import vedicpy as vedic

    # calling cube_2digit_number from vedic.cube
    result = vedic.cube.cube_2digit_number(67)

    print(result)

In the program we first call the package by using ``import`` and by giving a compact syntax to it by using ``vedic`` as the name.

Then we simply call the ``cube_2digit_number`` function from ``cube`` module present in vedicpy.

As the name suggest ``cube_2digit_number`` function only cubes 2 digit integer numbers and returns an interger value that is stored in variable ``result`` and then we simply print that value of the variable.
