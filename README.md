# playwright-learning


## Playwright vs Selenium vs Puppeteer.

Compared to other popular browser automation toolkits like Selenium or Puppeteer, Playwright has a few advantages:

- Playwright supports many programming languages whereas Puppeteer is only available in Javasrcipt.
- Playwright uses Chrome Devtools Protocol (CDP) and a more modern API, whereas Selenium is using webdriver protocol and a less modern API.
- Playwright supports both asynchronous and synchronous clients, whereas Selenium only supports a synchronous client and Puppeteer an asynchronous one. In Playwright, we can write small scrapers using synchronous clients and scale up simply by switching to a more complex asynchronous architecture.

In other words, Playwright is a horizontal improvement over Selenium and Puppeteer.

### Notes
- The difference between the Locator and ElementHandle is that the ElementHandle points to a particular element, while Locator captures the logic of how to retrieve an element.
    https://www.checklyhq.com/blog/understanding-element-handles-and-page-locators/
- 
