from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
#####################################################################################################################
#-----------Selector
url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
Customer_Login_selector = 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button'
User_selection_selector = "userSelect"
User_selection_value1= "1"
User_selection_value2= "2"
Login_click_selector= 'body > div > div > div.ng-scope > div > form > button'
Deposit_Menu_Button_selector = 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)'
Amount_Box_selector = 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input'
Amount_Box_text = 'AAAA'
Deposit_click_selector = 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button'
Manager_Login_selector = 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button'
Add_Customer_selector = 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)'
First_Name_selector = 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input'
Last_Name_selector = 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input'
Last_Name_text = 'israel'
Post_Code_selector = 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input'
Post_Code_value = '1234'
Add_Customer_Button_selector = 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button'
Customer_Menu_selector = 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)'
Row_count_selector = "//table/tbody/tr"
Balance_selector = 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)'
Account_id = "accountSelect"
Account_1004 = "number:1004"
Account_1005 = "number:1005"
Account_1006 = "number:1006"
Transaction_menu = 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)'
Transactions = "//table/tbody/tr"
Deposit100 = '100'
Home_selector = 'body > div > div > div.box.mainhdr > button.btn.home'
Firstext = None


def open_site(driver, url):
    driver.get(url)
    time.sleep(3)
    return driver.current_url

def customer_login(driver,selector,):
    Customer_Login = driver.find_element(By.CSS_SELECTOR,selector)
    Customer_Login.click()
    # time.sleep(1)

def user_selection(driver,selector,value,click_selector):
    Your_Name = Select(driver.find_element(By.ID, selector))
    Your_Name.select_by_value(value)
    Login_Button = driver.find_element(By.CSS_SELECTOR, click_selector)
    Login_Button.click()
    # time.sleep(1)

def login_click(driver,selector):
    Login_Button = driver.find_element(By.CSS_SELECTOR, selector)
    Login_Button.click()

def deposit_menu(driver,selector):
    Deposit_Menu_Button = driver.find_element(By.CSS_SELECTOR,selector)
    Deposit_Menu_Button.click()
    # time.sleep(1)

def amount_Box(driver, selector,text):
    Amount_Box = driver.find_element(By.CSS_SELECTOR,selector)
    Amount_Box.click()
    Amount_Box.send_keys(text)
    # time.sleep(1)

def deposit_click(driver,selector):
    Deposit_Button = driver.find_element(By.CSS_SELECTOR,selector)
    Deposit_Button.click()
    time.sleep(1)

def manager_login(driver,selector):
    Manager_Login = driver.find_element(By.CSS_SELECTOR,selector)
    Manager_Login.click()

def add_customer(driver, addSelector,firstSelector,lastSelector,postSelector,buttonSelector,firstext,text,value):
    Add_Customer_Menu = driver.find_element(By.CSS_SELECTOR,addSelector)
    Add_Customer_Menu.click()
    time.sleep(1)
    Last_Name_Box = driver.find_element(By.CSS_SELECTOR,lastSelector)
    Last_Name_Box.click()
    Last_Name_Box.send_keys(text)
    Post_Code_Box = driver.find_element(By.CSS_SELECTOR,postSelector)
    Post_Code_Box.click()
    Post_Code_Box.send_keys(value)
    Add_Customer_Button = driver.find_element(By.CSS_SELECTOR,buttonSelector)
    Add_Customer_Button.click()

def customer_manu(driver,selector):
    Customer_Menu = driver.find_element(By.CSS_SELECTOR,selector)
    Customer_Menu.click()

def row_count(driver, selector):
    Rows = driver.find_elements(By.XPATH, selector)
    return Rows

def balance(driver,selector):
    Balance = driver.find_element(By.CSS_SELECTOR,selector).text
    return int(Balance)

def account_select(driver,id,accountNumber):
    Account = Select(driver.find_element(By.ID,id))
    Account.select_by_value(accountNumber)

def transaction1_menu_len(driver,selector,TransactionsNU):
    Transaction_menu = driver.find_element(By.CSS_SELECTOR,selector)
    Transaction_menu.click()
    Transactions1 = driver.find_elements(By.XPATH, TransactionsNU)
    return len(Transactions1)
    driver.back()

def transaction2_menu_len(driver,selector,TransactionsNU):
    Transaction_menu = driver.find_element(By.CSS_SELECTOR,selector)
    Transaction_menu.click()
    Transactions2 = driver.find_elements(By.XPATH, TransactionsNU)
    return len(Transactions2)


def transaction3_menu_len(driver,selector,TransactionsNU):
    Transaction_menu = driver.find_element(By.CSS_SELECTOR,selector)
    Transaction_menu.click()
    Transactions3 = driver.find_elements(By.XPATH, TransactionsNU)
    return len(Transactions3)
    driver.back()

def home_button(driver, selector):
    Home = driver.find_element(By.CSS_SELECTOR,selector)
    Home.click()
