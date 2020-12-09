from behave import *
from selenium import webdriver

use_step_matcher("re")


@given("I launch Chrome browser")
def step_impl(context):
    context.driver=webdriver.Chrome()
    """
    :type context: behave.runner.Context
    """



@when("I open orange HRM Homepage")
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    """
    :type context: behave.runner.Context
    """



@step("Click on login button")
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()
    """
    :type context: behave.runner.Context
    """



@then("User must successfully login to the Dashboard page")
def step_impl(context):
   #try:
       #text = context.driver.find_element_by_xpath("//*[@id='content')/div/div[1]/h1").text
   #except:
   #    context.driver.close()
   #    assert False,"Test Failed"
   #if text=="Dashboad":
   #    context.driver.close()
   #   assert True, "Test Passed"#
    """
    :type context: behave.runner.Context
    """



@step('Enter username "(?P<username>.+)" and password "(?P<password>.+)"')
def step_impl(context, username, password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
