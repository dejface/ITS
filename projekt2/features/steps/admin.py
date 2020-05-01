from behave import *

"""1. scenario"""


@given("User is on admin page")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/admin/")


@given("is not logged in")
def step_impl(context):
    context.driver.find_elements_by_xpath("//*[contains(text(), 'Please enter your login details.')]")


@when("user enters correct login")
def step_impl(context):
    context.driver.find_element_by_id("input-username").send_keys("admin")

    context.driver.find_element_by_id("input-password").send_keys("admin")


@when("logs in")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()


@then("user is logged as admin in admin section")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Dashboard')]")
    context.driver.find_element_by_xpath("//*[contains(text(), 'Logout')]")


"""2. scenario"""


@given("User is logged as admin")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/admin/")

    context.driver.find_element_by_id("input-username").send_keys("admin")

    context.driver.find_element_by_id("input-password").send_keys("admin")

    context.driver.find_element_by_xpath("//button[@type='submit']").click()

    context.driver.find_element_by_xpath("//*[contains(text(), 'Dashboard')]")
    context.driver.find_element_by_xpath("//*[contains(text(), 'Logout')]")


@when('user clicks "Catalog"')
def step_impl(context):
    context.driver.find_element_by_xpath("//li[@id='catalog']/a").click()


@when('user clicks "Products"')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()


@then("all products will show up")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Product List')]")
    context.driver.find_element_by_xpath("//*[contains(text(), 'Filter')]")


"""3. scenario"""


@when('user clicks "Categories"')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Categories')]").click()


@then("all categories will show up")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[contains(text(), 'Categories')]")
    context.driver.find_element_by_xpath("//*[contains(text(), 'Category List')]")


"""4. scenario"""


@when('user clicks "Logout"')
def step_impl(context):
    context.driver.find_element_by_xpath("//header[@id='header']/ul/li[4]/a").click()


@then("user is logged out")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8084/admin/")
    context.driver.find_elements_by_xpath("//*[contains(text(), 'Please enter your login details.')]")
