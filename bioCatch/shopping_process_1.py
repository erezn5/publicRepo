# -*- coding: utf-8 -*-
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from re import sub
from decimal import Decimal
import unittest, time, re


def check_total(value):
    pass


class Shop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')
        self.driver.implicitly_wait(30)
        #self.base_url = "https://www.aliexpress.com/"
        self.base_url="https://www.amazon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_shop(self):
        driver = self.driver
        driver.get(self.base_url + "/")
       # driver.find_element_by_id("twotabsearchtextbox").click()
        driver.find_element_by_id("twotabsearchtextbox").clear()
        driver.find_element_by_id("twotabsearchtextbox").send_keys(
            "Apple iPhone 5S 16 GB Unlocked, Silver (Certified Refurbished)")
        driver.find_element_by_css_selector("input.nav-input").click()
        driver.find_element_by_xpath("//li[@id='result_0']/div/div/div/div[2]/div/div/a/h2").click()
        Select(driver.find_element_by_id("quantity")).select_by_visible_text("2")
        time.sleep(3)
        driver.find_element_by_id("add-to-cart-button").click()
        time.sleep(3)
        driver.find_element_by_id("siNoCoverage-announce").click()


        element=driver.find_element_by_xpath('//*[@id="hlb-subcart"]/div[1]/span/span[2]').text
        print(element)
        value = Decimal(sub(r'[^\d.]', '', element))
        
        check_total(value)
        

       #  driver.find_element_by_id("twotabsearchtextbox").clear()
       #  driver.find_element_by_id("twotabsearchtextbox").send_keys(
       #      "Merax High-back Gaming Chair Ergonomic Design Office Chair Racing Style Computer Chair (blue and black)")
       #  driver.find_element_by_css_selector("input.nav-input").click()
       #  driver.find_element_by_xpath("//li[@id='result_0']/div/div/div/div[2]/div/div/a/h2").click()
       #  driver.find_element_by_id("add-to-cart-button").click()

        #driver.find_element_by_id("siNoCoverage-announce").click()
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
