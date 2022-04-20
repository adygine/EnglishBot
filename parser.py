from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import repository
import time
import pickle

def intialize() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={repository.user_agent}')
    #options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(
        executable_path='chrome_driver/chromedriver',
        options=options
    )
    return driver

def get_into(driver : webdriver.Chrome):
    try:
        driver.get(repository.url_edit)
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        time.sleep(5)
        driver.refresh()
        time.sleep(10)
    except Exception:
        authorize(driver)
        pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
        time.sleep(10)

def authorize(driver : webdriver.Chrome):
    driver.get(repository.url_login)
    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')
    username.clear()
    password.clear()
    username.send_keys(repository.auth()[0])
    password.send_keys(repository.auth()[1])
    password.send_keys(Keys.ENTER)

def add_card(driver : webdriver.Chrome):
    print('exec')
    driver.get(repository.url_edit)
    time.sleep(10)

def process():
    driver = intialize()
    try:
        get_into(driver)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()