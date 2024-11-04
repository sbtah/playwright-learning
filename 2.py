from playwright.sync_api import sync_playwright
from lxml.html import tostring, html5parser


def generate_html_element(response: str):
    """"""
    return html5parser.fromstring(response)


with sync_playwright() as pw:

    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()

    page.goto('https://twitch.tv/directory/game/Art')

    # Wait for desired element to load.
    page.wait_for_selector('//div[@data-target="directory-container"]')

    # Response to element
    # Lxml Htmlelement for faster data extraction.
    first_element = generate_html_element(page.content())

    parsed = []
    stream_boxes_play = page.locator('//div[contains(@class,"tw-tower")]/div[@data-target]')
    print(f'DEBUG ELEMENTS LOCATOR: {stream_boxes_play}')

    stream_boxes_lxml = first_element.xpath('//div[contains(@class,"tw-tower")]/div[@data-target]')
    print(f'DEBUG ELEMENTS LXML: {stream_boxes_lxml}')
