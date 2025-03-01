import playwright.sync_api
from playwright.sync_api import Playwright


fakePayloadOrderResponse= {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(
        json= fakePayloadOrderResponse
    )



def test_apiResponseMocking(playwright:Playwright):

    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page= context.new_page()

    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/user/get-orders-for-customer/*",intercept_response)
    page.locator("#userEmail").fill("mausamsharma2018@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Qwerty@2210")
    page.locator("#login").click()
    page.get_by_role("button",name= "ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)