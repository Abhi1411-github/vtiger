from selenium import webdriver
from time import sleep
from pytest import mark
from auto import Demo
from login import LoginPage
from lead_vtiger import Lead

# driver = webdriver.Firefox()
# driver.get("http://49.249.28.218:8888/index.php?module=Leads&action=index")
# driver.maximize_window()


# def login(_driver,config):
#     s = Demo(_driver)
#     s.text_fill(("xpath","//input[@type='text']"),config.username)
#     s.text_fill(("xpath","//input[@type='password']"),config.password)
#     s.click_button(("xpath","//input[@id='submitButton']"))



header = "f_name, l_name, mobile, company"
data = [("rahul", "pandey", "909026191", "itc"), ("akhil", "raj", "6907690122", "LG")]

@mark.parametrize(header,data)
def test_lead(_driver,_config,f_name,l_name,mobile,company):
    s = Demo(_driver)

    login = LoginPage(_driver)                         # _driver is a setup_tear_down function in conftest file
    login.login("admin","admin")
    led = Lead(_driver)
    led.lead(f_name, l_name, mobile, company)




def test_organization(_driver):
    s = Demo(_driver)

    login_ = LoginPage(_driver)
    login_.login("admin", "admin")

    s.click_button(("xpath","//a[text()='Organizations']"))
    sleep(2)                                                                        #organization
    s.click_button(("xpath","//input[@id='2008']"))
    s.click_button(("xpath","//input[@id='2023']"))
    sleep(2)
    s.click_button(("xpath","(//input[@class='crmbutton small delete'])[1]"))
    sleep(1)
    s.alert_accept()
    sleep(3)

def test_contact(_driver):
    s = Demo(_driver)

    login_ = LoginPage(_driver)
    login_.login("admin", "admin")


    s.click_button(("xpath","(//a[text()='Contacts'])[1]"))
    s.click_button(("xpath","//a[text()='Kishore_2869']"))
    s.click_button(("xpath","//a[text()='Send Mail']"))
    s.click_button(("xpath","(//input[@class='crmbutton small create'])[4]"))
    s.change_window(0)
    sleep(4)
    s.select_dropdown(("xpath","//select[@name='parent_type']"),4)
    sleep(2)
    s.click_button("xpath","//img[@src='themes/softed/images/select.gif']")
    s.change_window(2)
    sleep(3)
    s.click_button(("xpath","//a[text()='Mark Henry']"))
    sleep(1)
    s.change_window(1)
    sleep(3)
    s.text_fill(("xpath","//input[@id='cc_name']","abc.12@gmail.com"))
    s.text_fill(("xpath","//input[@id='subject']"),"new opening ..... ")
    sleep(1)
    s.click_button(("xpath","(//input[@class='crmbutton small save'])[2]"))


def test_opportunity(_driver):
        s = Demo(_driver)
        login_ = LoginPage(_driver)
        login_.login("admin", "admin")

        s.click_button(("xpath","(//a[text()='Opportunities'])[1]"))
        s.click_button(("xpath","//img[@src='themes/softed/images/btnL3Add.gif']"))
        s.text_fill(("xpath","(//input[@class='detailedViewTextBox'])[1]"),"tarzan")
        s.click_button(("xpath","(//img[@src='themes/softed/images/select.gif'])[1]"))
        s.change_window(1)
        s.click_button(("xpath","//a[@id='1']"))
        s.change_window(0)
        s.click_button(("xpath","//img[@id='jscal_trigger_closingdate']"))
        s.click_button(("xpath","//td[text()='11']"))
        s.select_dropdown(("xpath","(//select[@class='small'])[7]"),2)
        sleep(2)
        s.click_button(("xpath","(//input[@class='crmbutton small save'])[1]"))


def test_more(_driver):
        s = Demo(_driver)
        login_ = LoginPage(_driver)
        login_.login("admin", "admin")

        s.cursor_move(("xpath","(//a[@href='javascript:;'])[1]"))
        sleep(5)
        s.click_button(("xpath","(//a[@id='more'])[2]"))
        sleep(5)

def test_trouble_ticket(_driver):
    s = Demo(_driver)
    login_ = LoginPage(_driver)
    login_.login("admin","admin")

    s.click_button(("xpath","//a[text()='Trouble Tickets']"))
    s.click_button(("xpath","//img[@src = 'themes/softed/images/btnL3Add.gif']"))
    s.select_dropdown(("xpath","(//select[@class='small'])[5]"),2)
    s.select_dropdown(("xpath","(//select[@class='small'])[7]"),"2")
    s.select_dropdown(("xpath","(//select[@class='small'])[8]"),1)
    s.text_fill(("xpath","//textarea[@name='ticket_title']"),"application not working properly")
    s.click_button(("xpath","//input[@class='crmButton small save']"))











