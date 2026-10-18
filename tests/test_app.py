import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class StudentRegistrationTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Remote(
            command_executor="http://selenium-chrome:4444",
            options=options
        )
        self.driver.implicitly_wait(5)

    def test_registration_form(self):
        self.driver.get("http://student-registration/")

        self.assertIn(
            "Student Registeration",
            self.driver.page_source
        )

        self.assertEqual(
            len(self.driver.find_elements(
                By.NAME, "firstname"
            )),
            1
        )

        self.assertEqual(
            len(self.driver.find_elements(
                By.NAME, "lastname"
            )),
            1
        )

        self.assertEqual(
            len(self.driver.find_elements(
                By.CLASS_NAME, "registerbtn"
            )),
            1
        )

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
