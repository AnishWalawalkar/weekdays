=======
weekdays
=======

A python module that provides methods to work with ‘weekdays’

Examples
========

.. code-block:: python

    from datetime import datetime
    from weekdays import weekdays

    date = datetime(2016, 2, 10)

    weekdays.is_weekday(date) # True
    weekdays.next_weekday(date, num_days=2) # datetime.datetime(2016, 2, 12, 0, 0)
