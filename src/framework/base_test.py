import pytest
import json
import logging
from unittest import TestCase
from selenium import webdriver
from appium import webdriver as appium_driver
from src.framework.env_helper import EnvHelper
from src.framework.capabilities import capabilities
import src.framework.config as config

class BaseTest(TestCase):
    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger(__name__)


    def setUp(self):
        self.test_env = EnvHelper.get_test_env()
        self.test_target = EnvHelper.get_test_target()
        self.test_target_context = EnvHelper.get_test_target_context()
        self.desired_capabilities = json.loads(capabilities)["target_capabilities"][self.test_target]
        print(self.desired_capabilities)
        if self.test_target_context == "desktop":
            self.logger.info("Desktop Test Target")
            if "desktop_chrome" in self.test_target:
                self.driver = webdriver.Chrome(desired_capabilities=self.desired_capabilities)
            elif "desktop_firefox" in self.test_target:
                self.driver = webdriver.Firefox(desired_capabilities=self.desired_capabilities)
            elif "desktop_safari" in self.test_target:
                self.driver = webdriver.Safari(desired_capabilities=self.desired_capabilities)
        else:
            self.logger.info("Mobile Test Target")


        config.DRIVER = self.driver
        config.DRIVER.set_page_load_timeout(config.TIMEOUT)
        config.DRIVER.implicitly_wait(config.TIMEOUT)
        config.TEST_TARGET = self.test_target
        config.TEST_TARGET_CONTEXT = self.test_target_context

    def tearDown(self):
        self.driver.quit()

