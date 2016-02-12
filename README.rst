=======
weekdays
=======

.. image:: https://travis-ci.org/AnishWalawalkar/weekdays.svg?branch=master
    :target: https://travis-ci.org/AnishWalawalkar/weekdays

A python module that provides methods to work with weekdays

Installation
============

.. code-block:: bash

    $ pip install pyweekdays

Examples
========

.. code-block:: python

    from datetime import datetime
    from weekdays import weekdays

    date = datetime(2016, 2, 10)

    weekdays.is_weekday(date) # True

    weekdays.next_weekday(date, num_days=2) # datetime.datetime(2016, 2, 12, 0, 0)
    weekdays.prev_weekday(date, num_days=2) # datetime.datetime(2016, 2, 8, 0, 0)

    weekdays.weekdays_until(datetime(2016,2,10), datetime(2016,2,28)) # 12.0
    weekdays.weekdays_passed(datetime(2016,2,28), datetime(2016,2,10)) # 12.0

    date_range = (datetime(2016, 2, 1), datetime(2016, 2, 15))

    for date in weekdays.date_range(*date_range):
        print(date)
    # 2016-02-01 00:00:00
    # 2016-02-02 00:00:00
    # 2016-02-03 00:00:00
    # 2016-02-04 00:00:00
    # 2016-02-05 00:00:00
    # 2016-02-08 00:00:00
    # 2016-02-09 00:00:00
    # 2016-02-10 00:00:00
    # 2016-02-11 00:00:00
    # 2016-02-12 00:00:00
