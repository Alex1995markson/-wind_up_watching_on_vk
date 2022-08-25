import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


load_dotenv()

PATH_TO_DRIVER = os.getenv('PATH_TO_DRIVER')
URL = os.getenv('DEFAULT_URL')


def open_video() -> None:
    driver = webdriver.Chrome(PATH_TO_DRIVER)
    driver.get(URL)
    driver.implicitly_wait(15)
    play_video_btn = driver.find_element(By.CLASS_NAME, '_play')
    play_video_btn.click()
    driver.implicitly_wait(20)
    driver.close()
