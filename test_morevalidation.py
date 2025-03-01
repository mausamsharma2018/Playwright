import time

from playwright.sync_api import Page, expect


def test_moreValidation(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    #locatiing element by using placeholder
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #alertboxes

    page.get_by_role("button",name="Alert").click()
    page.on("dialog",lambda dialog:dialog.accept())
    time.sleep(4)
    page.get_by_role("button",name="Confirm").click()
    page.on("dialog",lambda dialog:dialog.reject())

    #framehandling
    pageframe=page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link",name="All Access plan").click()

    #expect(page.locator("#body")).to_contain_text("Practice Page")

    #mousehover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top")

def test_moreValidations(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #extracting value from dynamic table (find thr price of rice is equal to 37)
    #extracting the price column
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
              pricecolvalue= index;
              print(f"price column value is {pricecolvalue}")
              break

    #extracting the rice row number
    ricerow=page.locator("tr").filter(has_text="Rice")
    # check in the ricerow if pricecolumnvalue has text 37 or value 37.
    expect(ricerow.locator("td").nth(pricecolvalue)).to_have_text("37")












