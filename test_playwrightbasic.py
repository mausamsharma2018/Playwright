import playwright
from playwright.sync_api import Page, expect


# def test_playwrightbasic(playwright):
#     browser= playwright.chromium.launch(headless=False)
#     context= browser.new_context()
#     page= context.new_page()
#     page.goto("https://rahulshettyacademy.com/")


def  test_playwrightshortcut(page:Page):
           # we are using the fixture(page) from Page class.
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
#test
#launching firefox browser in playwright (using plawright object from playwright class package )
# def test_firefoxbrowser(playwright: playwright):
#     firefoxbrowser= playwright.firefox.launch(headless=False)
#     page= firefoxbrowser.new_page()

    iphoneproducts=page.locator("app-card").filter(has_text="iphone x")
    iphoneproducts.get_by_role("button").click()

    Nokiaproducts= page.locator("app-card").filter(has_text="Nokia Edge")
    Nokiaproducts.get_by_role("button").click()

    page.get_by_text("Checkout").click()
    #validations check the product count in cart

    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.get_by_text("iphone x")).to_be_visible()
    expect(page.get_by_text("Nokia Edge")).to_be_visible()



def test_ChildWindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newpage_info:
        # page.locator(".blinkingText").click()
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_page= newpage_info.value
        text=child_page.locator(".red").text_content()
        print(text)
        # spliting the text got from locator.
        words= text.split("at")
        email=words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"














