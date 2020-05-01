from behave import *


@given("User is on registration page")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/index.php?route=account/register")
    context.driver.find_element_by_xpath("//*[contains(text(),'Register Account')]")


@when("user fills all of needed information")
def step_impl(context):
    context.driver.find_element_by_id("input-firstname").send_keys("tester")
    context.driver.find_element_by_id("input-lastname").send_keys("tester")
    context.driver.find_element_by_id("input-email").send_keys("tester@tester.com")
    context.driver.find_element_by_id("input-telephone").send_keys("0999999999")
    context.driver.find_element_by_id("input-address-1").send_keys("testtt")
    context.driver.find_element_by_id("input-city").send_keys("city")
    context.driver.find_element_by_id("input-postcode").send_keys("99999")
    context.driver.find_element_by_xpath("//fieldset[@id='address']/div[6]/div/select").click()
    context.driver.find_element_by_xpath("//div[7]/div/select/option[2]").click()
    context.driver.find_element_by_id("input-password").send_keys("test")
    context.driver.find_element_by_id("input-confirm").send_keys("test")


@when("accepts privacy policy")
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@name='agree']").click()


@when('clicks "Continue"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Continue']").click()


@then("registration is successful")
def step_impl(context):
    try:
        context.driver.find_element_by_class_name("account-success")
    except:
        pass


"""2. scenario"""


@when("user doesn't fill all of needed information")
def step_impl(context):
    context.driver.find_element_by_id("input-lastname").send_keys("tester")


@then("registration is not successful")
def step_impl(context):
    context.driver.find_element_by_class_name("account-register")


"""3. scenario"""


@when("doesn't accept privacy policy")
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//input[@name='agree']").click()
    except:
        pass


"""4. scenario"""


@given("User is on login page")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/index.php?route=account/login")


@given("enters his e-mail address")
def step_impl(context):
    context.driver.find_element_by_id("input-email").send_keys("tester@tester.com")


@given("enters correct password")
def step_impl(context):
    context.driver.find_element_by_id("input-password").send_keys("test")


@when('user clicks "Login"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Login']").click()


@then("user is logged in")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(),'My Account')]")


"""5. scenario"""


@when('user clicks "MyAccount"')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a/i").click()


@when('clicks "Order history"')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Order History')]").click()


@then("history of order is shown")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(),'Order History')]")

