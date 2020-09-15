import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
from traceback import print_stack


class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):

        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + result_message)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + result_message)
                    self.screen_shot(result_message)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + result_message)
                self.screen_shot(result_message)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, result_message):

        self.set_result(result, result_message)

    def markFinal(self, test_name, result, result_message):

        self.set_result(result, result_message)

        if "FAIL" in self.resultList:
            self.log.error(test_name + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
