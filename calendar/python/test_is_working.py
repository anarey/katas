import unittest

from is_working import is_working_day, is_working_date, is_working_range

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
        is_working = is_working_day("")
        self.assertEqual(is_working, "")

    def test_incorrect_day(self):
        is_working = is_working_day("wrong_day")
        self.assertEqual(is_working, "")

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
        is_working = is_working_date("")
        self.assertEqual(is_working, "")

    def test_working_incorrect_date(self):
        is_working = is_working_date("sedrfse")
        self.assertEqual(is_working, "")

    def test_working_false_date(self):
        is_working = is_working_date("34/07/2012")
        self.assertEqual(is_working, "")

class TestClassRangeDay(unittest.TestCase):

    def test_working_day_1(self):
        range_days = is_working_range("01/07/2012", "04/07/2012")
        self.assertEqual(range_days, {'01/07/2012' : False,
                                    '02/07/2012' : True,
                                    '03/07/2012' : True,
                                    '04/07/2012' : True})

    def test_working_day_2(self):
        range_days = is_working_range("02/07/2012", "05/07/2012")
        self.assertNotEqual(range_days, {'01/07/2012' : False,
                                    '02/07/2012' : True,
                                    '03/07/2012' : True,
                                    '04/07/2012' : True})

    def test_working_day_3(self):
        range_days = is_working_range("04/07/2012", "08/07/2012")
        self.assertEqual(range_days, {'04/07/2012' : True,
                                    '05/07/2012' : True,
                                    '06/07/2012' : True,
                                    '07/07/2012' : False,
                                    '08/07/2012' : False})

    def test_working_day_0(self):
        range_days = is_working_range("04/07/2012", "04/07/2012")
        self.assertEqual(range_days,{})

    def test_working_bad_range(self):
        is_working = is_working_range("05/07/2012", "03/07/2012")
        self.assertEqual(is_working, {})
        
    def test_working_bad_range2(self):
        is_working = is_working_range("06/07/2012", "04/07/2012")
        self.assertEqual(is_working, {})

    def test_working_bad_range3(self):
        is_working = is_working_range("", "04/07/2012")
        self.assertEqual(is_working, {})

    def test_working_bad_range4(self):
        is_working = is_working_range("06/07/2012","")
        self.assertEqual(is_working, {})

    def test_working_bad_range5(self):
        is_working = is_working_range("", "")
        self.assertEqual(is_working, {})

    def test_working_bad_range_date(self):
        is_working = is_working_range("232231", "05/05/2012")
        self.assertEqual(is_working, {})

    def test_working_Invalid_date(self):
        is_working = is_working_range("12/03/1633", "04/07/2012")
        self.assertEqual(is_working, {})

    def test_working_Invalid_date(self):
        is_working = is_working_range("34/03/1633", "04/07/2012")
        self.assertEqual(is_working, {})
