from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import playwright

ordersPayload= {"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}

class Apiutils:

    def getToken(self,playwright:Playwright,user_credentials):
        user_email= user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        api_request_context= playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response= api_request_context.post("/api/ecom/auth/login", data={"userEmail":user_email,"userPassword":user_password},)
        assert response.ok
        response_body= response.json()
        return response_body["token"]

    def createOrder(self,playwright:Playwright,user_credentials):
        Token= self.getToken(playwright,user_credentials)
        api_request_context= playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response= api_request_context.post("/api/ecom/order/create-order",data= ordersPayload,
                                 headers={"Authorization":Token,
                                          "content_type": "application/json"})
        print(response.json())
        response.body= response.json()
        orderId= response.body["orders"][0]
        return orderId







