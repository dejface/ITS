from behave import *


"""1. scenario"""


@given("User is on any eshop page")
def step_impl(context):
    context.driver.get(context.base_url)


@given('User clicks on "Currency" option')
def step_impl(context):
    context.driver.find_element_by_xpath("//form[@id='form-currency']/div/button/i").click()


@when("new currency is selected")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[@name='EUR']").click()


@then("currency on page was changed")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(),'€')]").click()


"""2. scenario"""


@given("User has opened internet browser")
def step_impl(context):
    pass


@step("user has internet connection")
def step_impl(context):
    context.driver.get("http://www.ismyinternetworking.com")
    context.driver.find_element_by_xpath("//*[contains(text(),'YES!')]")


@when("user searches for eshop page")
def step_impl(context):
    context.driver.get(context.base_url)


@then("page correctly loads")
def step_impl(context):
    context.driver.find_element_by_class_name("common-home")


"""3. scenario"""


@given("user is logged in")
def step_impl(context):
    context.driver.get(context.base_url)
    context.driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a").click()
    context.driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()

    context.driver.find_element_by_id("input-email").send_keys("test@test.com")
    context.driver.find_element_by_id("input-password").send_keys("test")

    context.driver.find_element_by_xpath("//*[contains(text(),'My Account')]")


@when('user clicks on "Newsletter"')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Newsletter')]").click()


@then("user has newsletter subscription")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(),'My Account')]")


"""4. scenario"""


@when('clicks on "Wish list"')
def step_impl(context):
    context.driver.find_element_by_xpath("//li[3]/a/i").click()


@then("user wish list is shown")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/index.php?route=account/wishlist")

