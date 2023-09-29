from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/")
    page.get_by_role("heading", name="Elements").click()
    page.get_by_text("Text Box").click()
    page.locator("li").filter(has_text="Check Box").click()
    page.get_by_text("Radio Button").click()
    page.get_by_text("Web Tables").click()
    page.locator("li").filter(has_text="Buttons").click()
    page.get_by_text("Links", exact=True).click()
    page.get_by_text("Broken Links - Images").click()
    page.get_by_text("Upload and Download").click()
    page.locator("li").filter(has_text="Dynamic Properties").click()
    page.get_by_role("button", name="Visible After 5 Seconds").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)