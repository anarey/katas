import unittest

from isWorking import is_working_day, is_working_date

from isWorking import NotDayFound, IncorrectDay, NotDateFound

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


class TestClassCalendarDay(unittest.TestCase):
    
    def test_working_day_09072012(self):
        is_working = is_working_date("09/07/2012")
        self.assertTrue(is_working)

    def test_working_day_08072012(self):
        is_working = is_working_date("08/07/2012")
        self.assertFalse(is_working)

    def test_working_day_05072012(self):
        is_working = is_working_date("05/07/2012")
        self.assertTrue(is_working)

    def test_working_day_30062012(self):
        is_working = is_working_date("30/06/2012")
        self.assertFalse(is_working)

    def test_working_day_noday(self):
        self.assertRaises(NotDateFound, is_working_date, "")

