import unittest

from isHoliday import isHoliday_day

class testClassCalendar(unittest.TestCase):

    def test_monday_holiday(self):
        isHoliday = isHoliday_day("Monday")
        self.assertFalse(isHoliday)

       

