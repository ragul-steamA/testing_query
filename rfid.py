from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://x-main.d33rile30xkzn5.amplifyapp.com')
input("Press ENTER...")
input_email= driver.find_element(
            By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[2]/form/div[1]/div/div/div/div/input')
input_email.send_keys('arvind@steam-a.com')
input_pass= driver.find_element(
            By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[2]/form/div[2]/div/div/div/div/span/input')
input_pass.send_keys('Admin@123')
enter_button=driver.find_element(
            By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[2]/form/button[2]')
enter_button.click()
time.sleep(3)

df = pd.read_excel('rfid.xlsx', usecols='A,B')

for i in df.index:
    try:
        driver.get('https://x-main.d33rile30xkzn5.amplifyapp.com/customers/show/'+'"'+str(df['phone'][i])+'"')
        time.sleep(3)
        rfid_element=driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/main/div/div[4]/div[2]/div/div/div")
        text=rfid_element.text
        if not text:
            child_elements = rfid_element.find_elements_by_xpath(".//*")
            text = ' '.join(e.text for e in child_elements)
        print(text)
        if str(df['rfid'][i]) not in rfid_element.text:
            print('no')
            f = open("failed_rfid.txt", "a", encoding="utf8")
            f.write(str(df['phone'][i]))
            f.write('\n')
        else:
            print('yes')
    except Exception as e:
        print(e)
        f = open("failed_rfid.txt", "a", encoding="utf8")
        f.write(str(df['phone'][i]))
        f.write('\n')