from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
driver = webdriver.Safari()
#-----------Selector
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










# open_site(url)
# customer_login()












#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
# url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login/'
# driver = webdriver.Safari()

# def open_site(driver, url):
#     driver.get(url)
#     time.sleep(3)
#     return driver.current_url

####################################### (1) Without string #######################################
# open_site(driver,url)
# # driver.maximize_window()
# time.sleep(1)
# Customer_Login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
# Customer_Login.click()
# time.sleep(1)
# Your_Name = Select(driver.find_element(By.ID,"userSelect"))
# Your_Name.select_by_value("1")
# time.sleep(1)
# Login_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > form > button')
# Login_Button.click()
# time.sleep(1)
# Deposit_Menu_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
# Deposit_Menu_Button.click()
# time.sleep(1)
# Amount_Box = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
# Amount_Box.click()
# Amount_Box.send_keys('AAAA')
# # time.sleep(1)
# Deposit_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
# Deposit_Button.click()
# time.sleep(1)
# driver.close()
####################################### (1) Without string - !!!Need to be done!!!! #######################################



####################################### (2) Add user without first name #######################################
# open_site(driver,url)
# # driver.maximize_window()
# time.sleep(1)
# time.sleep(1)
# Manager_Login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
# Manager_Login.click()
# time.sleep(1)
# Customer_Menu = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)')
# Customer_Menu.click()
# time.sleep(2)
# Customers1 = driver.find_elements(By.XPATH,"//table/tbody/tr")
# print(len(Customers))
# Home = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.box.mainhdr > button.btn.home')
# Home.click()
# time.sleep(1)
# Manager_Login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
# Manager_Login.click()
# time.sleep(1)
# Add_Customer_Menu = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)')
# Add_Customer_Menu.click()
# time.sleep(1)
# Last_Name_Box = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input')
# Last_Name_Box.click()
# Last_Name_Box.send_keys('israel')
# Post_Code_Box = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input')
# Post_Code_Box.click()
# Post_Code_Box.send_keys('1234')
# time.sleep(1)
# Add_Customer_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button')
# Add_Customer_Button.click()
# time.sleep(1)
# ######
# Home = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.box.mainhdr > button.btn.home')
# Home.click()
# Manager_Login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
# Manager_Login.click()
# time.sleep(1)
# Customer_Menu = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)')
# Customer_Menu.click()
# time.sleep(2)
# Customers2 = driver.find_elements(By.XPATH,"//table/tbody/tr")
# print(len(Customers2))
# driver.close()
####################################### (2) Add user without first name - !!!Need to be done!!!! #######################################



####################################### !!DONE!! (3) Sanity !!DONE!! #######################################
# open_site(driver,url)
# # driver.maximize_window()
# time.sleep(3)
# driver.close()
####################################### !!DONE!! (3) Sanity !!DONE!! #######################################



############################# !!DONE!! (4) Costumer Count !!DONE!! #######################################
# open_site(driver,url)
# # driver.maximize_window()
# time.sleep(1)
# Manager_Login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
# Manager_Login.click()
# time.sleep(1)
# Customer_Menu = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)')
# Customer_Menu.click()
# time.sleep(2)
# Rows = driver.find_elements(By.XPATH,"//table/tbody/tr")
# print(len(Rows))
# driver.close()
############################# !!DONE!! (4) Costumer Count !!DONE!! #######################################



# #######################################  (5) 3 Deposit  #######################################
# open_site(driver,url)
# # driver.maximize_window()
# time.sleep(1)
# Customer_Login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
# Customer_Login.click()
# time.sleep(1)
# Your_Name = Select(driver.find_element(By.ID,"userSelect"))
# Your_Name.select_by_value("1")
# time.sleep(1)
# Login_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > form > button')
# Login_Button.click()
# time.sleep(1)
# Deposit_Menu_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
# Deposit_Menu_Button.click()
# time.sleep(1)
# Current_Balance = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)').text
# print('Current Balance -',Current_Balance,'$')
# # #--------------- Deposit 1 ----------------
# Amount_Box = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
# Amount_Box.click()
# Amount_Box.send_keys('100')
# # time.sleep(1)
# Deposit_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
# Deposit_Button.click()
# # #--------------- Deposit 2 ----------------
# Amount_Box = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
# Amount_Box.click()
# Amount_Box.send_keys('100')
# # time.sleep(1)
# Deposit_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
# Deposit_Button.click()
# # #--------------- Deposit 3 ----------------
# Amount_Box = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
# Amount_Box.click()
# Amount_Box.send_keys('100')
# # time.sleep(1)
# Deposit_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
# Deposit_Button.click()
# time.sleep(1)
# New_Balance = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)').text
# print('New Balance -',New_Balance,'$')
# driver.close()
#######################################  (5) 3 Deposit  #######################################



############################### !!DONE!! (6) Harry Potter !!DONE!! #######################################
# open_site(driver,url)
# # driver.maximize_window()
# time.sleep(1)
# Customer_Login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
# Customer_Login.click()
# time.sleep(1)
# Your_Name = Select(driver.find_element(By.ID,"userSelect"))
# Your_Name.select_by_value("2")
# time.sleep(1)
# Login_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > form > button')
# Login_Button.click()
# time.sleep(1)
# #--------------- Account 1 ----------------
# Account = Select(driver.find_element(By.ID,"accountSelect"))
# Account.select_by_value("number:1004")
# First_Account = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(1)').text
# Transaction_Menu_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)')
# Transaction_Menu_Button.click()
# time.sleep(1)
# Transactions = driver.find_elements(By.XPATH,"//table/tbody/tr")
# print('Account',First_Account,'has',len(Transactions),'transactions ')
# driver.back()
# time.sleep(1)
# # #--------------- Account 2 ----------------
# Account = Select(driver.find_element(By.ID,"accountSelect"))
# Account.select_by_value("number:1005")
# Second_Account = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(1)').text
# Transaction_Menu_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)')
# Transaction_Menu_Button.click()
# time.sleep(1)
# Transactions = driver.find_elements(By.XPATH,"//table/tbody/tr")
# print('Account',Second_Account,'has',len(Transactions),'transactions ')
# driver.back()
# time.sleep(1)
# #--------------- Account 3 ----------------
# Account = Select(driver.find_element(By.ID,"accountSelect"))
# Account.select_by_value("number:1006")
# Third_Account = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(1)').text
# Transaction_Menu_Button = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)')
# Transaction_Menu_Button.click()
# time.sleep(1)
# Transactions = driver.find_elements(By.XPATH,"//table/tbody/tr")
# print('Account',Third_Account,'has',len(Transactions),'transactions ')
# driver.back()
# time.sleep(1)
############################### !!DONE!! (6) Harry Potter !!DONE!! #######################################

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

