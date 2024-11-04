from playwright.sync_api import sync_playwright
from lxml.html import tostring, html5parser, fromstring
import time


def generate_html_element(response: str):
    """"""
    element = fromstring(response)
    return element


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
    # print(f'DEBUG FIRST EL: {first_element}')

    parsed = []
    # Locators
    stream_boxes_play = page.locator('//div[contains(@class,"tw-tower")]/div[@data-target]')
    # Handles
    # print(f'DEBUG ELEMENTS LOCATOR: {stream_boxes_play.element_handles()}')

    # Parsing HTML with lxml...
    stream_boxes_lxml = first_element.xpath('//div[contains(@class,"tw-tower")]/div[@data-target]')
    # print(f'DEBUG ELEMENTS LXML: {stream_boxes_lxml}')

    for item in stream_boxes_lxml:
        title = item.xpath('.//h3/text()')[0].strip()
        url = item.xpath('.//a[@data-a-id]/@href')[0]

        user_card_id = item.xpath('.//a[@data-a-id]/@data-a-id')[0]
        user_name = user_card_id.split('-')[-1]
        tags = [tag.text_content() for tag in item.xpath('.//button[contains(@aria-label, "Tag")]')]
        viewers = item.xpath('.//div[contains(@class, "tw-media-card-stat")]/text()')[0].strip()

        parsed.append({
            'title': title,
            'url': url,
            'user_name': user_name,
            'tags': tags,
            'viewers': viewers,
        })

    print(parsed)
