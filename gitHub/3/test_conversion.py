from selenium.webdriver.common.by import By
import time

url = "https://www.metric-conversions.org/"


def test_celsius_to_fahrenheit(driver):
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@class="typeConv temperature bluebg"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@href="/temperature/celsius-to-fahrenheit.htm"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="argumentConv"]').send_keys("0")
    answer = driver.find_element(By.XPATH, '//p[@id="answer"]').text
    assert answer == '0°C= 32.00000°F'


def test_meters_to_feet(driver):
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@class="typeConv length bluebg"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@href="/length/meters-to-feet.htm"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="argumentConv"]').send_keys("1")
    answer = driver.find_element(By.XPATH, '//p[@id="answer"]').text
    assert answer == '1m= 3ft 3.370079in'


def test_ounces_to_grams(driver):
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@class="typeConv weight bluebg"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@href="/weight/ounces-to-grams.htm"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="argumentConv"]').send_keys("1")
    answer = driver.find_element(By.XPATH, '//p[@id="answer"]').text
    assert answer == '1oz= 28.34952g'
