class BaseClass:

    def navigateurl(self, context, locator):
        context.page.goto(locator)

    def do_click(self, context, locator):
        context.page.click(locator)

    def do_sendkeys(self,context, locator, text):
        context.page.fill(locator, text)

