import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
import unittest

class Test_Hotel_Payments(unittest.TestCase):

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://www.phptravels.net/signup")
    first_name = driver.find_element_by_xpath('//input[@name = "first_name"]')
    first_name.click()
    first_name.send_keys("Tam")
    last_name = driver.find_element_by_xpath('//input[@name = "last_name"]')
    last_name.click()
    last_name.send_keys("Gh")
    phone = driver.find_element_by_xpath('//input[@name = "phone"]')
    phone.click()
    phone.send_keys("+37494000")
    email = driver.find_element_by_xpath('//input[@name = "email"]')
    email.click()
    email.send_keys("tam.gh@mail.ru")
    sleep(2)
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    password = driver.find_element_by_xpath('//input[@name = "password"]')
    password.click()
    password.send_keys("t1234567")
    singup = driver.find_element_by_xpath('//span[@class="ladda-label"][text()="Signup"]')
    singup.click()
    driver.get('https://www.phptravels.net/login')
    email_login = driver.find_element_by_xpath('//input[@name = "email"]')
    email_login.click()
    email_login.send_keys("tam.gh@mail.ru")
    password_login = driver.find_element_by_xpath('//input[@name = "password"]')
    password_login.click()
    password_login.send_keys("t1234567")
    password_login.send_keys(Keys.ENTER)
    hotels = driver.find_element_by_xpath('//a[@href="https://www.phptravels.net/hotels"]')
    hotels.click()
    searchbox = driver.find_element_by_xpath('//*[@id="select2-hotels_city-container"]')
    searchbox.click()
    city = driver.find_element_by_class_name('select2-search__field')
    city.send_keys("Yerevan")
    sleep(2)
    city.send_keys(Keys.ENTER * 1)
    search = driver.find_element_by_xpath('//button[@type= "submit"]')
    search.click()
    details = driver.find_element_by_xpath('//*[@id="yerevan deluxe hotel"]/div/div[2]/div/div[2]/div/a/span[1]')
    details.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    sleep(5)
    search_2 = driver.find_element_by_xpath('//*[@id="SearchBoxContainer"]/div/div/button/span')
    search_2.click()
    sleep(5)
    driver.execute_script("window.scrollTo(0, 1700)")
    sleep(5)
    select_rooms = driver.find_element_by_xpath('//h3[@class="PropertyCard__HotelName"][text()="Hotel National"]')
    select_rooms.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[2])
    sleep(5)
    view = driver.find_element_by_xpath('//*[@id="hotelNavBar"]/div/div/div/div/button')
    view.click()
    sleep(10)
    booking = driver.find_element_by_xpath('//button[@type="button"][text()="Book now"]')
    booking.click()
    sleep(10)
    full_name = driver.find_element_by_xpath('//*[@id="firstName_lastName"]')
    full_name.click()
    full_name.send_keys("Tam Gh")
    sleep(3)
    email_reserve = driver.find_element_by_xpath('//input[@name = "email"]')
    email_reserve.click()
    email_reserve.send_keys("tam.gh@mail.ru")
    sleep(3)
    retype_email = driver.find_element_by_xpath('//input[@name = "retypeEmail"]')
    retype_email.click()
    retype_email.send_keys("tam.gh@mail.ru")
    sleep(3)
    phone = driver.find_element_by_xpath('//input[@name = "phoneNumber"]')
    phone.click()
    phone.send_keys("+374940000")
    final_step = driver.find_element_by_xpath('//span[@class="Spanstyled__SpanStyled-sc-16tp9kb-0 lfpNCX kite-js-Span "][text()="NEXT: FINAL STEP"]')
    final_step.click()
    payment_page_title = driver.find_element_by_css_selector("[data-component=mob-flight-payment-subHeader]")
    strName = payment_page_title.text
    manual_version = "All card information is fully encrypted, secure and protected."


    def setUp(self):
        print('Test case started')

    def test_payment_page(self):

        manual_vs = self.manual_version
        selenium_vs = self.strName
        assert manual_vs == selenium_vs


    def tearDown(self):
        print("End of the test case")

if __name__ == '__main__':
    unittest.main()

