from playwright.sync_api import sync_playwright
import time


with sync_playwright() as pw:
    # Create a browser instance.
    browser = pw.chromium.launch(
        headless=False,
    )

    # Create a context.abs
    # Using context I can define page properties, like viewport dimensions, etc...
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
    )

    # Create a page aka `browser tab`.
    page = context.new_page()

    # Go to the url.
    page.goto('https://twitch.tv/directory/game/Art')
    
    # Wait for element to appear.
    el_1 = page.wait_for_selector('//div[@data-target="directory-container"]')
    print(el_1.as_element())
    print(dir(el_1))
    print(type(el_1))

    el_2 = page.locator('//div[@data-target="directory-container"]')
    # print(el_2)
    # print(dir(el_2))
    # print(type(el_2))
    # Print HTML - same as driver.page_source?
