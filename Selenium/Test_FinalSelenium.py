from FinalSelenium import *


class TestXYZBank:
    def test_sanity(self):
        driver = webdriver.Safari()
        open_site(driver,url)
        driver.maximize_window()
        expected = url
        actual = driver.current_url
        driver.close()
        assert expected == actual
        time.sleep(1)

    def test_Costumer_Count(self):
        driver = webdriver.Safari()
        open_site(driver,url)
        driver.maximize_window()
        time.sleep(1)
        manager_login(driver,Manager_Login_selector)
        time.sleep(1)
        customer_manu(driver,Customer_Menu_selector)
        time.sleep(1)
        Rows = row_count(driver,Row_count_selector)
        expected = 5
        actual = len(Rows)
        driver.close()
        assert expected == actual

    def test_3Deposit(self):
        driver = webdriver.Safari()

        open_site(driver, url)
        driver.maximize_window()
        time.sleep(1)
        customer_login(driver,Customer_Login_selector)
        time.sleep(1)
        user_selection(driver,User_selection_selector,User_selection_value1,Login_click_selector)
        time.sleep(1)
        deposit_menu(driver,Deposit_Menu_Button_selector)
        time.sleep(1)
        Old_Balance = balance(driver,Balance_selector)
        time.sleep(1)
        #1
        amount_Box(driver,Amount_Box_selector,Deposit100)
        time.sleep(1)
        deposit_click(driver,Deposit_click_selector)
        #2
        amount_Box(driver, Amount_Box_selector, Deposit100)
        time.sleep(1)
        deposit_click(driver, Deposit_click_selector)
        #3
        amount_Box(driver, Amount_Box_selector, Deposit100)
        time.sleep(1)
        deposit_click(driver, Deposit_click_selector)
        New_Balance = balance(driver, Balance_selector)
        expected = (Old_Balance) + 300
        actual = (New_Balance)
        driver.close()
        assert expected == actual

    def test_HarryPoter_Account1(self):
        driver = webdriver.Safari()

        open_site(driver, url)
        driver.maximize_window()
        time.sleep(1)
        customer_login(driver, Customer_Login_selector)
        time.sleep(1)
        user_selection(driver, User_selection_selector, User_selection_value2, Login_click_selector)
        time.sleep(1)
        #Account 1004
        account_select(driver,Account_id,Account_1004)
        time.sleep(1)
        First = transaction1_menu_len(driver,Transaction_menu,Transactions)
        time.sleep(1)
        driver.back()
        # Account 1005
        account_select(driver, Account_id, Account_1005)
        time.sleep(1)
        Second = transaction2_menu_len(driver, Transaction_menu, Transactions)
        time.sleep(1)
        driver.back()
        # Account 1006
        account_select(driver, Account_id, Account_1006)
        time.sleep(1)
        Third = transaction3_menu_len(driver, Transaction_menu, Transactions)
        expected = 1
        actual = First + Second + Third
        driver.close()
        assert expected == actual

    def test_AddNew_Costumer(self):
        driver = webdriver.Safari()

        open_site(driver, url)
        driver.maximize_window()
        time.sleep(1)
        manager_login(driver, Manager_Login_selector)
        time.sleep(1)
        customer_manu(driver, Customer_Menu_selector)
        time.sleep(1)
        Customers1 = row_count(driver, Row_count_selector)
        home_button(driver,Home_selector)
        time.sleep(1)
        manager_login(driver, Manager_Login_selector)
        time.sleep(1)
        add_customer(driver,Add_Customer_selector,First_Name_selector,Last_Name_selector,Post_Code_selector,Add_Customer_Button_selector,Firstext,Last_Name_text,Post_Code_value)
        home_button(driver, Home_selector)
        time.sleep(1)
        manager_login(driver, Manager_Login_selector)
        time.sleep(1)
        customer_manu(driver, Customer_Menu_selector)
        time.sleep(1)
        Customers2 = row_count(driver, Row_count_selector)
        expected = len(Customers1) + 1
        actual = len(Customers2)
        driver.close()
        assert expected == actual
