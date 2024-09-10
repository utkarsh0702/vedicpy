.. _divisibility:

=================
Divisibility
=================

1) divisibility_under10
---------------------------------

.. image:: screenshot/divisibility.png
   :alt: divisibility test


**Implementation:**

.. code-block:: python

    import vedicpy as vedic

    # divisibility_under10() function takes two arguments,
    # first one is dividend and the other one is divisor
    vedic.divisibility.divisibility_under10(108, 9)
    
    >>> True

*The function returns a boolean value.*

**The divisibility test is only applicable for divisor less than 10.**
