
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from selenium import webdriver
import datetime
import time

with open('credentials.json') as data_file:
    data = json.load(data_file)

email = data['spotify']['email']
password = data['spotify']['password']


def main():

    song_url = data['spotify']['song']['url']

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")

    loginBox = driver.find_element(By.XPATH, '//*[@id="login-username"]')
    passwordBox = driver.find_element(By.XPATH, '//*[@id="login-password"]')

    loginBox.send_keys(email)
    passwordBox.send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    time.sleep(5)

    driver.get(song_url)

    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div['
                                  '2]/main/section/div[3]/div[4]/div/div/div/div/div/button').click()

    length = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div['
                                           '2]/main/section/div[1]/div[5]/div/span[2]').text

    x = time.strptime(length.split(',')[0], '%M:%S')
    restartTime = ((datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds())/2) + 5

    restart = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div[1]/div[2]/div/div[1]/div['
                                            '1]/button[2]')

    if restartTime > 240:
        restartTime = 242
        while True:
            time.sleep(restartTime)
            restart.click()
    else:
        while True:
            time.sleep(restartTime)
            restart.click()


if __name__ == "__main__":
    main()
