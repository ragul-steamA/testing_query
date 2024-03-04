from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://steam-ev-stage.d4twos69vhff8.amplifyapp.com')
input("Make sure your in Full screen maximized Press ENTER...")
input_email = driver.find_element(
    By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[2]/form/div[1]/div/div/div/div/input')
input_email.send_keys('arvind@steam-a.com')
input_pass = driver.find_element(
    By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[2]/form/div[2]/div/div/div/div/span/input')
input_pass.send_keys('Admin@123')
enter_button = driver.find_element(
    By.XPATH, '/html/body/div/div/div[1]/div/div/div/div/div[2]/form/button[2]')
enter_button.click()
time.sleep(3)
df = pd.read_excel('sessions.xlsx', usecols='A,B,C')
driver.get('https://steam-ev-stage.d4twos69vhff8.amplifyapp.com/sessions/')
time.sleep(4)
button = driver.find_element(
    By.XPATH, '/html/body/div/div/div[1]/div/main/div/div/div/div[2]/div/div[1]/div/div/div/form/div/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/span')
button.click()
time.sleep(1)
button2 = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/div/div/div[2]/div/div[3]/div/div/div/div/div/table/thead/tr/th[2]/div/span[1]')
button2.click()
for i in df.index:
    try:
        button1 = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/div/div/div[2]/div/div[2]/div[2]/form/span/input')
        button1.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys(
            "A").send_keys(Keys.DELETE).key_up(Keys.CONTROL)
        actions.perform()
        time.sleep(0.5)
        button1.send_keys(str(df['ocpp_transaction_id'][i].astype(int)))
        time.sleep(2)
        total_cost_element = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/div/div/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[11]/div/div[1]')
        print('total_cost_element.text '+total_cost_element.text)
        cost=total_cost_element.text
        cost=total_cost_element.text.replace(",","")
        if cost!="0":
            
            if cost.endswith("0"):
                cost = cost[:-1]
        clickable=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/main/div/div/div/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[1]/a')
        clickable.click()
        time.sleep(1.5)
        invoice_id_element=driver.find_element(
            By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div[1]/div[2]/div[2]/p')
        invoice=invoice_id_element.text
        print('invoice_id_element.text '+invoice_id_element.text)
        button=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[3]/button')
        button.click()
        if str(df['inv_no'][i])==invoice and str(df['total_cost'][i])==cost:
            print('yes')
        else:
            print('no')
            f = open("failed_sessions.txt", "a", encoding="utf8")
            f.write(str(df['ocpp_transaction_id'][i]))
            f.write('\n')
    except Exception as e:
        print(e)
        f = open("failed_sessions.txt", "a", encoding="utf8")
        f.write(str(df['ocpp_transaction_id'][i]))
        f.write('\n')
