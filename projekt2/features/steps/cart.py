from behave import *


"""1. scenario"""


@given("User is on exact product page")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/index.php?route=product/product&product_id=43")


@given("Cart is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//span[contains(text(),'0 item(s) - $0.00')]")


@when("User adds item to cart")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[@id='button-cart']").click()


@then("Cart contains one more item")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[contains(text(),' 1 item(s) - $602.00')]")


"""2. scenario"""


@given("User is on cart page")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/index.php?route=checkout/cart")
    context.driver.find_element_by_xpath("//span[contains(text(),'0 item(s) - $0.00')]")


@when('User clicks "Continue"')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(),'Continue')]").click()


@then("Main page is loaded")
def step_impl(context):
    context.driver.get(context.base_url)
