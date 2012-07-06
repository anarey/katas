import unittest

from isHoliday import is_holiday_day

class testClassCalendar(unittest.TestCase):

    def test_monday_holiday(self):
        is_holiday = is_holiday_day("Monday")
        self.assertFalse(is_holiday)
 

