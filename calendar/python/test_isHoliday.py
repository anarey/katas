import unittest

class testClassCalendar(unittest.TestCase):
    def test_monday_holiday(self):
        isHoliday = isHoliday_day("Monday")
        self.assertFalse(isHoliday)

       

