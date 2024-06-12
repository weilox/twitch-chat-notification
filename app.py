from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, sys
from playsound import playsound

while True:
    x = input("Enter your channel name\n> ")
    break

try:
    chrome_options = Options()

    service = Service('chromedriver.exe')
    service.start()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(f"https://www.twitch.tv/{x}")

    total_messages = driver.find_elements(By.CLASS_NAME, "chat-line__message")

    while True:
        if (driver.find_elements(By.CLASS_NAME, "chat-line__message") != total_messages):
            playsound("notif.wav")
            total_messages = driver.find_elements(By.CLASS_NAME, "chat-line__message")
except:
    sys.exit()