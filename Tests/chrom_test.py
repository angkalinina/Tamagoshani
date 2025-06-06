from selenium import webdriver
from selenium.webdriver.chrome import options

capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

options.capabilities,update(selenium_capabilities)
driver = webdriver.Remote(
    command_executor=f"https://{selenium_login}:{selenium_pass}@{selenium_url}/wd/hub",
    options=options)

browser.config.driver = driver