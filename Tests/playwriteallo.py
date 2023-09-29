from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_label("Найти").click()
    page.get_by_label("Найти").fill("allo")
    page.get_by_label("Поиск в Google").first.click()
    page.get_by_role("link", name="АЛЛО - національний маркетплейс із найширшим ... АЛЛО https://allo.ua › ...").click()
    page.get_by_placeholder("Пошук товарів").click()
    page.get_by_placeholder("Пошук товарів").fill("Телефон")
    page.get_by_role("button", name="Надіслати").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)