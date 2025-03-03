import json
import time

import pytest
from playwright.async_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import playwright, page

from apiBase import Apiutils

# json file->util>access into test

with open('data/credential.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_apiTesting(playwright: Playwright, user_credentials):

    browser= playwright.chromium.launch(headless=True)
    context= browser.new_context()
    page= context.new_page()




# login without using the api request method.
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credentials["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
    page.locator("#login").click()



    # creating order using api utilities from apiBase class
    api_utils= Apiutils()
    orderId= api_utils.createOrder(playwright, user_credentials)

    print(orderId)


    #order history page->order is present
    row = page.locator("tr").filter(has_text=orderId)
    page.get_by_role("button", name="View").first.click()
    print(page.title())
    context.close()














