.. _square:

============
Square
============

1) square_ending5
---------------------------------

.. image:: screenshot/ending_5.png
   :alt: square of ending with 5


**Implementation:**

.. code-block:: python

    import vedicpy as vedic

    a= vedic.square.square_ending5(35)
    print(a)

>>> 1225

2) square_near_powerof10
---------------------------------

.. image:: screenshot/near_power_of10.png
   :alt: square near power of 10


**Implementation:**

.. code-block:: python

    import vedicpy as vedic

    a= vedic.square.square_near_powerof10(98)
    print(a)

>>> 9604


3) square_under100
---------------------------------

.. image:: screenshot/2digit_1.png
   :alt: square of 2 digit number

.. image:: screenshot/2digit_2.png
   :alt: square of 2 digit number


**Implementation:**

.. code-block:: python

    import vedicpy as vedic

    a= vedic.square.square_under100(69)
    print(a)

>>> 4761


4) square_from100_to1000
---------------------------------

.. image:: screenshot/3digit.png
   :alt: square of 3 digit number


**Implementation:**

.. code-block:: python

    import vedicpy as vedic

    a= vedic.square.square_from100_to1000(983)
    print(a)

>>> 966289
