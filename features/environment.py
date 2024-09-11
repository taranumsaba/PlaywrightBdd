from playwright.sync_api import sync_playwright
from features.steps.basepage import BaseClass

def before_all(context):
    browser = sync_playwright().start().chromium.launch(headless=False, slow_mo=1000, channel='chrome')
    # Creating Page instance that can be used in all the scripts

    context.page = browser.new_page()
    context.page.set_viewport_size({"width": 1560, "height": 1200})
    # Creating Baseclass object this can be used in all the pages
    context.base_instance = BaseClass()
    context.page.goto("")
    context.page.set_viewport_size({"width": 1520, "height": 500})
    #context.page.keyboard.



