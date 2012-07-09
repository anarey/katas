import unittest

from isWorking import is_working_day

from isWorking import NotDayFound, IncorrectDay

class testClassCalendar(unittest.TestCase):

    def test_monday_working(self):
        is_working = is_working_day("Monday")
        self.assertTrue(is_working)
    
    def test_sunday_working(self):
        is_working = is_working_day("Sunday")
        self.assertFalse(is_working)

    def test_wednesday_working(self):
        is_working = is_working_day("Wednesday")
        self.assertTrue(is_working)
    
    def test_saturday_working(self):
        is_working = is_working_day("Saturday")
        self.assertFalse(is_working)

    def test_no_day_working(self):
        self.assertRaises(NotDayFound, is_working_day, "")

    def test_incorrect_day(self):
        self.assertRaises(IncorrectDay, is_working_day, "wrong_day")
