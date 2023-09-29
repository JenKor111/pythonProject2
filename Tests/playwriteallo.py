from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.goto("https://www.google.com/search?q=Allo&sca_esv=569384727&source=hp&ei=x3YWZaL1O_C7hbIP9cebkAE&iflsig=AO6bgOgAAAAAZRaE2KMCeKScEqpmC09gMfOZB0yNJvRs&ved=0ahUKEwji9NOvoM-BAxXwXUEAHfXjBhIQ4dUDCAo&uact=5&oq=&gs_lp=Egdnd3Mtd2l6IgBIAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEDyAEA&sclient=gws-wiz")
    page.get_by_role("link", name="АЛЛО - національний маркетплейс із найширшим ... АЛЛО https://allo.ua › ...").click()
    page.locator(".ct-button > .vi").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)