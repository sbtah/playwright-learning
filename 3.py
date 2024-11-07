from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1020})
    page = context.new_page()

    page.goto('https://www.twitch.tv/directory/game/Art')

    # Locate the search box and type query.
    search_box = page.locator('//input[@autocomplete="twitch-nav-search"]')
    search_box.type('Painting', delay=100)

    # LOL!
    search_box.press('Enter')

    # We can also locate send/confirm button...
    search_button = page.locator('//button[@aria-label="Search Button"]')
    search_button.click()

    # ....
