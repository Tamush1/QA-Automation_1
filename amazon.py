<<<<<<< HEAD

=======
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time impor

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")
sleep(2)
search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.click()
sleep(2)
search.send_keys("iPhone 12")
search.send_keys(Keys.ENTER)
sleep(2)
iPhone_12 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a')
iPhone_12.click()
sleep(2)
AddCart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
AddCart.click()
sleep(2)
Cart = driver.find_element_by_xpath('//*[@id="nav-cart-count"]')
Cart.click()
sleep(2)
iPhone_12_in_Cart = driver.find_element_by_xpath('//*[@id="sc-item-C7b672afe-7670-49f5-bdcd-a36c4bd7c6fe"]/div[4]/div/div[1]/div/div/div[1]/a/img')
# iPhone_12_in_Cart = driver.find_element_by_xpath('//*[@id="sc-item-Ced8e71bd-515b-4eab-b4e9-d7c52974951b"]/div[4]/div/div[1]/div/div/div[2]/ul/li[1]/span/a/span[1]/span/span[2]')
iPhone_12_in_Cart.click()
sleep(2)
driver.close()
>>>>>>> 090a34e (Add file)
