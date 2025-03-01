import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_text("rahulshettyacademy").click()
    page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material Incorrect username/").press("ControlOrMeta+c")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_text("learning").click()
    page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material Incorrect username/").press("ControlOrMeta+c")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("learning")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_text("rahulshettyacademy").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("button", name="Sign In").click()
    page.locator("app-card").filter(has_text="iphone X $24.99 Lorem ipsum").get_by_role("button").click()
    page.locator("app-card").filter(has_text="Samsung Note 8 $24.99 Lorem").get_by_role("button").click()
    page.get_by_text("Checkout ( 2 ) (current)").click()
    page.get_by_role("row", name="iphone X by Sim cart Status:").get_by_role("button").click()
    page.get_by_role("button", name="Remove").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)