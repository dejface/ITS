from selenium import webdriver


def before_scenario(context, feature):
    dp = {'browserName': 'chrome', 'marionette': 'true', 'javascriptEnabled': 'true'}
    # Connect to hub
    context.driver = webdriver.Remote(command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub", desired_capabilities=dp)
    # Dom timeout
    context.driver.implicitly_wait(15)
    context.base_url = "http://pat.fit.vutbr.cz:8084"


def after_scenario(context, feature):
    context.driver.quit()
