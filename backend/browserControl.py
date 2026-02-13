from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = None
def start_browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

def openYoutube():
    global driver
    driver = start_browser()
    driver.get("https://www.youtube.com")
    return f"Opening Youtbe"
def searchYoutube(video_name):
    global driver
    if driver is None:
        openYoutube()
    time.sleep(2)
    search = driver.find_element(By.NAME, "search_query")
    search.clear()
    search.send_keys(video_name)
    search.send_keys(Keys.RETURN)
    return f"Searching on youtube {video_name}"
def open_youtube_video(video_name):
    global driver
    if driver is None:
        openYoutube()
    wait = WebDriverWait(driver, 10)
    search = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    search.click()
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(Keys.DELETE)
    search.send_keys(video_name)
    search.send_keys(Keys.RETURN)
    video = wait.until(
        EC.element_to_be_clickable((By.ID, "video-title"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", video)
    video.click()
    return f"Playing {video_name}"

def openGoogle():
    global driver
    driver = start_browser()
    driver.get("https://www.google.com")
    return "Opening Google"
def searchGoogle(query):
    global driver
    if driver is None:
        openGoogle()
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.click()
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(Keys.DELETE)
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    return f"Searching Google for {query}"
def open_first_website(query):
    global driver
    if driver is None:
        openGoogle()
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    first_result = wait.until(
        EC.element_to_be_clickable((By.XPATH, '(//h3)[1]'))
    )
    first_result.click()
    return f"Opening {query}"

def scroll_down():
    driver = start_browser()
    driver.execute_script("window.scrollBy(0, 500);")
    return "Scrolling down"

def scroll_up():
    driver = start_browser()
    driver.execute_script("window.scrollBy(0, -500);")
    return "Scrolling up"

def start_whatsapp():
    global driver
    driver=start_browser()
    driver.get("https://web.whatsapp.com")
    print("Scan QR Code if required...")
    return "opening whatsapp"
def send_whatsapp_message(contact_name, message):
    global driver
    try:
        if driver is None:
            start_whatsapp()
        wait = WebDriverWait(driver, 30)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"]')
            )
        )
        search_box = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            )
        )
        search_box.click()
        search_box.clear()
        search_box.send_keys(contact_name)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        message_box = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            )
        )
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        return f"Message sent to {contact_name}"

    except Exception as e:
        return f"WhatsApp error: {e}"