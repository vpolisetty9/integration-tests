from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
from src.framework import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from src.framework.env_helper import EnvHelper
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.expected_conditions import staleness_of
import time
from contextlib import contextmanager
from selenium.webdriver.support.ui import Select

class BasePage:


    APP_URL = EnvHelper.get_app_url()
    preloader = (By.CSS_SELECTOR, '#preloader')

    def wait_preloader_not_present(self, timeout=config.SHORT_TIMEOUT):
        self.wait_for_element_not_to_be_present(self.preloader, timeout)

    @contextmanager
    def wait_for(self,  timeout=config.TIMEOUT):
        old_url = self.get_current_url()
        yield
        WebDriverWait(config.DRIVER, timeout).until(expected_conditions.url_changes(old_url))

    def wait_for_condition(self, condition_function, timeout=config.TIMEOUT):
        start_time = time.time()
        while time.time() < start_time + timeout:
            if condition_function:
                return True
            else:
                time.sleep(0.1)
        raise Exception('Timeout waiting for {}'.format(condition_function.__name__))

    def ajax_complete(self):
        try:
            return 0 == config.DRIVER.execute_script("return jQuery.active")
        except Exception:
            pass

    def document_complete(self):
        try:
            return 'complete' == config.DRIVER.execute_script('return document.readyState')
        except Exception:
            pass

    def wait_for_page_load(self, timeout=config.SHORT_TIMEOUT):
        self.wait_preloader_not_present()
        try:
            self.wait_for_condition(self.document_complete(), timeout=timeout)
            self.wait_for_condition(self.ajax_complete(), timeout=timeout)
        except Exception as e:
            print(e)

    # return the element if its present on the dom
    def find_presence_of_element(self, selector, timeout=config.TIMEOUT):
        element = WebDriverWait(config.DRIVER, timeout).until(expected_conditions.presence_of_element_located(selector))
        assert element is not None
        return WebElement(element)

    # return element if its visible on the view port
    def find_element(self, selector, timeout=config.TIMEOUT):
        element = WebDriverWait(config.DRIVER, timeout).until(expected_conditions.visibility_of_element_located(selector))
        assert element is not None
        return element

    def find_elements(self, selector, timeout=config.TIMEOUT):
        elements = WebDriverWait(config.DRIVER, timeout).until(expected_conditions.presence_of_all_elements_located(selector))
        assert elements is not None
        return elements

    def scroll_to_element(self, selector, timeout=config.TIMEOUT):
        element = self.find_presence_of_element(selector, timeout)
        actions = ActionChains(config.DRIVER)
        actions.move_to_element(element).perform()

    def wait_for_presence(self, locator, timeout=config.TIMEOUT):
        element = WebDriverWait(config.DRIVER, timeout,
                                poll_frequency=1,
                                ignored_exceptions=[ElementNotVisibleException,
                                                    ElementNotSelectableException]).until(expected_conditions.visibility_of_element_located(locator))
        assert element is not None
        return element

    def wait_for_element_not_to_be_present(self, selector, timeout=config.SHORT_TIMEOUT):
        status = WebDriverWait(config.DRIVER, timeout,
                                poll_frequency=1).until(expected_conditions.invisibility_of_element_located(selector))
        assert status is True
        return status

    def click(self, selector, timeout=config.TIMEOUT):
        self.find_element(selector, timeout).click()

    def click_and_wait(self, selector, timeout=config.TIMEOUT):
        self.find_element(selector, timeout).click()
        self.wait_preloader_not_present()

    def click_elements_by_index(self, selector, index=0):
        elements = self.find_elements(selector)
        elements[index].click()
        self.wait_preloader_not_present()

    def clear(self, selector, timeout=config.TIMEOUT):
        self.find_element(selector, timeout).clear()

    def get_text(self, selector, timeout=config.TIMEOUT):
        return self.find_element(selector, timeout).text

    def type(self, selector, text, timeout=config.TIMEOUT):
        element = self.find_element(selector, timeout)
        element.send_keys(text)

    def select(self, locator, timeout=config.TIMEOUT):
        return Select(self.find_element(locator, timeout))

    def get_attribute(self, selector, attribute, timeout=config.TIMEOUT):
        self.find_element(selector, timeout).get_attribute(attribute)

    def is_element_present(self, selector, timeout=config.TIMEOUT):
        return True if self.find_presence_of_element(selector, timeout) else False

    def is_element_displayed(self, selector, timeout=config.TIMEOUT):
        return True if self.find_element(selector, timeout).is_displayed() else False

    def is_element_enabled(self, selector, timeout=config.TIMEOUT):
        return True if self.find_element(selector, timeout).is_enabled() else False

    def is_element_selected(self, selector, timeout=config.TIMEOUT):
        return True if self.find_element(selector, timeout).is_selected() else False

    def navigate_back(self):
        config.DRIVER.execute_script('window.history.go(-1);')

    def open_tab(self):
        config.DRIVER.find_element_by_tag_name('body').send_keys(Keys.COMMNAND + 't')

    def close_tab(self):
        config.DRIVER.find_element_by_tag_name('body').send_keys(Keys.COMMNAND + 'w')

    def open_window(self):
        current_handle = config.DRIVER.current_window_handle
        config.DRIVER.execute_script("window.open('');")
        return current_handle

    def get_window_handles(self):
        handles = config.DRIVER.window_handles
        return handles

    def open_url(self, uri, timeout=config.TIMEOUT):
        config.DRIVER.get(uri)
        self.wait_for_page_load()

    def get_current_url(self):
        config.DRIVER.get(config.DRIVER.current_url)

    def refresh(self):
        self.open_url(self.get_current_url())

    def reload(self):
        config.DRIVER.refresh()
        self.wait_for_page_load()

    def get_title(self):
        return config.DRIVER.title