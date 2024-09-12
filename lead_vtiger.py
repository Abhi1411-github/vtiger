from auto import Demo

class Lead:

    def __init__(self,driver):
        self.driver = driver

    def lead(self,f_name,l_name,mobile,company):
        s = Demo(self.driver)
        s.click_button(("xpath", "//a[@href='index.php?module=Leads&action=index']"))  # craete lead
        s.click_button(("xpath", "//img[@src='themes/softed/images/btnL3Add.gif']"))
        s.select_dropdown(("xpath", "(//select[@class='small'])[2]"), 1)
        s.text_fill(("xpath", "(//input[@class='detailedViewTextBox'])[1]"), value=f_name)
        s.text_fill(("xpath", "(//input[@class='detailedViewTextBox'])[2]"), value=l_name)
        s.text_fill(("xpath", "(//input[@class='detailedViewTextBox'])[4]"), value=mobile)
        s.text_fill(("xpath", "(//input[@class='detailedViewTextBox'])[5]"), value=company)
        s.click_button(("xpath", "//input[@class='crmButton small save']"))
