from behave import *
from selenium import webdriver

use_step_matcher("re")


@given("launch chrome browser")
def launchBrowser(context):
   #context.driver=webdriver.Chrome(executable_path="C:/Users/usuario/PycharmProjects/pythonProject2/venv/Scripts/chromedriver.exe")
    context.driver=webdriver.Chrome()
    """
    :type context: behave.runner.Context
    """
   # raise NotImplementedError(u'STEP: Given launch chrome browser')


@when("open orange hrm homepage")
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    """
    :type context: behave.runner.Context
    """
   # raise NotImplementedError(u'STEP: When open orange hrm homepage')


@then("verify that the logo present on page")
def verifyLogo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert  status is True
    """
    :type context: behave.runner.Context
    """
    #raise NotImplementedError(u'STEP: Then verify that the logo present on page')


@step("close browser")
def closeBrowser(context):
    """
    :type context: behave.runner.Context
    """
   #raise NotImplementedError(u'STEP: And close browser')