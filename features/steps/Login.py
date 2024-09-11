import time
from Logs import LogFile
import config
from behave import *
from features.steps.locator import *
use_step_matcher('re')

log = LogFile.loggen()

@given(u'Navigate to Tango site')
def NavigatetoTango(context):
    log.info("********Click SignIn*************")
    context.base_instance.do_click(context, LoginLocators.signin)


@when(u'User Enters the Username "(.*)"')
def EnterUN(context, uname):
    log.info("**********Enter Username****************")
    context.base_instance.do_sendkeys(context, LoginLocators.userName, uname)
    print(uname)


@when(u'User Enters the Password')
def EnterPwd(context):
    log.info("***************Enter Password****************")
    pwd = config.pwd
    context.base_instance.do_sendkeys(context, LoginLocators.password, pwd)

@when(u'User clicks on Login button')
def ClickLogin(context):
    context.base_instance.do_click(context, LoginLocators.loginButton)
    time.sleep(10)

@then(u'click on Push button')
def ClickPush(context):
    pass