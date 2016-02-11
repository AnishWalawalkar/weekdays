import unittest
from datetime import datetime
from datetime import timedelta
from weekdays import weekdays


class TestWeekdays(unittest.TestCase):
    def setUp(self):
        self.weekday = datetime(2016, 2, 10)
        self.weekend = datetime(2016, 2, 6)
        self.date_range = (datetime(2016, 2, 10), datetime(2016, 2, 28))
        self.dates = [
            datetime(2016, 2, 10, 0, 0),
            datetime(2016, 2, 11, 0, 0),
            datetime(2016, 2, 12, 0, 0),
            datetime(2016, 2, 15, 0, 0),
            datetime(2016, 2, 16, 0, 0),
            datetime(2016, 2, 17, 0, 0),
            datetime(2016, 2, 18, 0, 0),
            datetime(2016, 2, 19, 0, 0),
            datetime(2016, 2, 22, 0, 0),
            datetime(2016, 2, 23, 0, 0),
            datetime(2016, 2, 24, 0, 0),
            datetime(2016, 2, 25, 0, 0),
            datetime(2016, 2, 26, 0, 0)
        ]

    def test_isweekday(self):
        self.assertTrue(weekdays.is_weekday(self.weekday))

    def test_isnotweekday(self):
        self.assertFalse(weekdays.is_weekday(self.weekend))

    def test_weekdaysuntil(self):
        self.assertEqual(
            weekdays.weekdays_until(self.date_range[0], self.date_range[1]),
            12
        )

    def test_weekdayspassed(self):
        self.assertEqual(
            weekdays.weekdays_until(self.date_range[0], self.date_range[1]),
            12
        )

    def test_nextweekday_withweekday(self):
        self.assertEqual(
            weekdays.next_weekday(self.weekday), self.weekday)

    def test_nextday_withweekend(self):
        self.assertEqual(
            weekdays.next_weekday(self.weekend), self.weekend+timedelta(days=2))

    def test_prevweekday_withweekday(self):
        self.assertEqual(
            weekdays.prev_weekday(self.weekday), self.weekday)

    def test_prevday_withweekend(self):
        self.assertEqual(
            weekdays.prev_weekday(self.weekend), self.weekend-timedelta(days=1))

    def test_rangeweekdays(self):
        dates_list = []
        for date in weekdays.range_weekdays(*self.date_range):
            dates_list.append(date)
        self.assertEqual(dates_list, self.dates)
