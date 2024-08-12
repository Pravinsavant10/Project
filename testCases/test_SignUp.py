import time

from pageObjects.SignUp_Page import SignUp_Class


class Test_SignUp:

    def test_BankApp_Url_001(self, setup):
        self.driver = setup
        if self.driver.title == "Bank Application":
            assert True
        else:
            assert False

    def test_Signup_002(self, setup):
        self.driver = setup
        self.su = SignUp_Class(self.driver)
        self.su.Click_Signup()
        self.su.Enter_Username("Demo555")
        self.su.Enter_Password("Demo555@")
        self.su.Enter_Email("Demo555@credence.in")
        self.su.Enter_Phone("7656765456")
        self.su.Click_CreateUser_Button()
        time.sleep(5)
        if self.su.Validate_User_Creation() == "User created successfully":
            assert True
        else:
            assert False

