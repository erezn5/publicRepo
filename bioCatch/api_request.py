# -*- coding: utf-8 -*-
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class API(unittest.TestCase):

    def hello(self):

        import requests
        params = {'customerID': 'fixer', 'action': 'getScore', 'uuid': 'QA_Test_36YQ4WR','customerSessionID': 'AB88KTM0IQUTYZH'}
        headers = {"Accept-Encoding": "gzip, deflate", "User-Agent": "gzip"}
        response = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score?', params=params,headers=headers)
        print(response.content)
        code=response.status_code
        print(code)
        if(response.status_code!=200):
            print("Response code is not valid! please try again!")
        json_response = response.content
        j = json.loads(json_response)
        score=j['score']

        if(score<800):
            print('Score is too low...request is not valid')
        print(score)

if __name__ == "__main__":
    unittest.main()
