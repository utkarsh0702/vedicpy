.. _compliment:

============
Compliment
============

1) compliment_to_power_of10
---------------------------------

The Complement of a number is the difference between that number and the next higher power of 10. 3 is the complement of 7 (as next higher power of 7 is 10). 34 is the complement of 66 (as next higher power of 66 is 100).

Vedic Sutra:

  **Nikhilam Navatah Charamam Dasatah** 

which means, All from 9 and last from 10.

**Details:** We have to get the complement (Nikhilam) for the entire number by using 10 for the digit in the units place and by using 9 for the remaining digits.

**Implementation:**

.. code-block:: python

    import vedicpy as vedic

    a= vedic.compliment.compliment_to_power_of10(123)
    print(a)

>>> 877


