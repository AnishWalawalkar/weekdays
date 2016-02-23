========
weekdays
========

|pypi|_
|build status|_
|pypi downloads|_
|MIT License|_


A python module that provides methods to work with weekdays

Installation
============

.. code-block:: bash

    $ pip install pyweekdays

Manual Installation
===================

.. code-block:: bash

    $ git clone https://github.com/AnishWalawalkar/weekdays.git
    $ cd weekdays/
    $ python setup.py install

Examples
========

.. code-block:: python

    import time
    from datetime import datetime
    from weekdays import weekdays

    date = datetime(2016, 2, 10)

    # convert time object to datetime object to work with weekdays module
    weekdays.time_to_datetime(time_struct=time.gmtime()) # datetime.datetime(2016, 2, 22, 16, 42, 9)
    weekdays.time_to_datetime(time_struct=time.localtime()) # datetime.datetime(2016, 2, 22, 11, 42, 39)
    weekdays.time_to_datetime(time_in_seconds=time.time()) # datetime.datetime(2016, 2, 22, 11, 43, 14, 760845)

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


.. |build status| image:: https://travis-ci.org/AnishWalawalkar/weekdays.svg?branch=master
.. _build status: https://travis-ci.org/AnishWalawalkar/weekdays
.. |pypi| image:: https://img.shields.io/pypi/v/pyweekdays.svg
.. _pypi: https://pypi.python.org/pypi/pyweekdays
.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg
.. _MIT License: https://en.wikipedia.org/wiki/MIT_License
.. |pypi downloads| image:: https://img.shields.io/pypi/dm/pyweekdays.svg
.. _pypi downloads: https://pypi.python.org/pypi/pyweekdays
