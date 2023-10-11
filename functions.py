
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Opens a url with firefox and saves tthe session in driver var


def createSession(url):
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(options=options)
    login_response = driver.get(url)
    return driver

# Closes the pop-up on the home page


def versionDialogCloser(session):
    WebDriverWait(session, 30).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#siteVersionContainer > div:nth-child(1)")))
    button = session.find_elements(By.CSS_SELECTOR, "span.close")
    button[0].click()

# Innovative wait in order to wait until the user logins


def wait(session, url, page):
    while True:
        if session.current_url == url:
            sleep(0.5)
        elif session.current_url == page:
            break
        else:
            continue

# Waits until the selected time and then executes the order


def executionWait(Time):
    now = datetime.now()
    tim = now.strftime("%H:%M:%S")

    while tim != Time:
        sleep(0.5)
        now = datetime.now()
        tim = now.strftime("%H:%M:%S")

# Searches for the selected stock


def searchStock(session, stock):
    search = session.find_elements(By.CSS_SELECTOR, "#txt_search")
    search = search[1]
    search.send_keys(stock)
    sleep(1.3)
    # wait for the first dropdown option to appear and open it
    WebDriverWait(session, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#stockAutocomplete-container-sendorder > symbol-search:nth-child(1) > div:nth-child(1) > angucomplete:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3)")))
    first_option = session.find_element(
        By.CSS_SELECTOR, "#stockAutocomplete-container-sendorder > symbol-search:nth-child(1) > div:nth-child(1) > angucomplete:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1)")

    first_option.click()

# Checks if the order is restricted or not


def checkOrderable(session):
    error = 0
    element = session.find_element(
        By.CSS_SELECTOR, "#stockAutocomplete-container-sendorder > symbol-search:nth-child(1) > div:nth-child(1) > angucomplete:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(4) > span:nth-child(1)")
    if 'ممنوع،متوقف' in element.text:
        error = 1
    return error

# Selects the buy button


def selectBuy(session):
    button = session.find_elements(
        By.CSS_SELECTOR, "#sendorder-container > div.header.tp-bo-1.tp-bo-b > div.orderside65.ordertabs")
    button[0].click()

# Selects the sell button


def selectSell(session):
    button = session.find_elements(
        By.CSS_SELECTOR, "#sendorder-container > div.header.tp-bo-1.tp-bo-b > div.orderside86.ordertabs")
    button[0].click()

# Enters the number of stock given


def stockCount(session, count):
    element = session.find_elements(
        By.CSS_SELECTOR, "#send_order_txtCount")
    element[0].send_keys(count)

# Enters the price of stock given


def stockPrice(session, price):
    element = session.find_elements(
        By.CSS_SELECTOR, "#send_order_txtPrice")
    element[0].send_keys(price)

# Sends the order to the system


def sendOrder(session):
    button = session.find_elements(
        By.CSS_SELECTOR, "#send_order_btnSendOrder")
    button[0].click()

# Confirms the order


def orderConfirmation(session):
    button = session.find_elements(
        By.CSS_SELECTOR, "#sendorder_ModalConfirm_btnSendOrder")
    button[0].click()

# Resets all the fields in the session


def resetSession(session):
    inputs = session.find_elements(By.TAG_NAME, "input")
    for input in inputs:
        try:
            input.clear()
        except:
            continue


def resetSearch(session):
    search = session.find_elements(
        By.CSS_SELECTOR, "#stockAutocomplete-container-sendorder > symbol-search:nth-child(1) > div:nth-child(1) > angucomplete:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
    search[0].click()
