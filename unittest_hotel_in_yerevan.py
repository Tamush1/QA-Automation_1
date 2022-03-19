
import unittest

import booking_hotels


class Test_Hotel_Payments(unittest.TestCase):

    selenium_vs = booking_hotels.strName
    manual_version = "All card information is fully encrypted, secure and protected."


    def setUp(self):
        print('Test case started')

    def test_payment_page(self):

        manual_vs = self.manual_version
        selenium_vs = self.selenium_vs
        assert manual_vs == selenium_vs


    def tearDown(self):
        print("End of the test case")

if __name__ == '__main__':
    unittest.main()

