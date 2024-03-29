from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://x-main.d33rile30xkzn5.amplifyapp.com')
input("Press ENTER...")

df = pd.read_excel('wallet_data.xlsx', usecols='A,B')
driver.get('https://x-main.d33rile30xkzn5.amplifyapp.com/customers/')
time.sleep(5)
for i in df.index:
    print(str(df['wallet_balance'][i]))
    try:
        button = driver.find_element(
            By.XPATH, '/html/body/div/div/div[1]/div/main/div/div/div/div[2]/div/div[2]/div[2]/form/span/input')
        button.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.LEFT_CONTROL).key_down(Keys.SHIFT).send_keys(
            Keys.HOME).key_up(Keys.CONTROL).key_up(Keys.SHIFT).send_keys(Keys.BACK_SPACE)
        actions.send_keys(str(df['phone'][i]))
        actions.perform()
        time.sleep(1)
        wallet_element = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/div/div/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[7]/div')
        s=wallet_element.text.replace(",","")
        if s.endswith("0"):
            s = s[:-1]
        print(s)
        if (s == str(df['wallet_balance'][i])):
            print('yes')
        else:
            print('no')
            f = open("failed.txt", "a", encoding="utf8")
            f.write(str(df['phone'][i]))
            f.write('\n')
    except Exception as e:
        print(e)
        f = open("failed.txt", "a", encoding="utf8")
        f.write(str(df['phone'][i]))
        f.write('\n')