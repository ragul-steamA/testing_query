from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://steam-ev-stage.d4twos69vhff8.amplifyapp.com')
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
df = pd.read_excel('charge_point.xlsx', usecols='Z,AB')
driver.get('https://steam-ev-stage.d4twos69vhff8.amplifyapp.com/chargepoint/')
time.sleep(5)
for i in df.index:
    print(str(df['ocpp_charge_point_id'][i]))
    print(str(df['charger_type'][i]))
    try:
        button = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/div/div/div[2]/div/div[2]/div[2]/form/span/input')
        button.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).key_down("A").send_keys(Keys.DELETE).key_up(Keys.CONTROL).key_up(Keys.SHIFT)
        actions.perform()
        time.sleep(0.5)
        button.send_keys(str(df['ocpp_charge_point_id'][i]))
        time.sleep(2)
        charger_type_element = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/div/div/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[4]/span')
        print(charger_type_element.text)
        if(charger_type_element.text==str(df['charger_type'][i])):
            print('yes')
        else:
            print('no')
            f = open("failed_cpid.txt", "a", encoding="utf8")
            f.write(str(df['ocpp_charge_point_id'][i]))
            f.write('\n')
    except Exception as e:
        print(e)
        f = open("failed_cpid.txt", "a", encoding="utf8")
        f.write(str(df['ocpp_charge_point_id'][i]))
        f.write('\n')