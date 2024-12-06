# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestV16SmokeTetonCoC():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_v16SmokeTetonCoC(self):
    self.driver.get("https://keelw.github.io/teton-coc/index.html")
    self.driver.set_window_size(1800, 800)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
    self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".header-top").click()
    self.driver.find_element(By.LINK_TEXT, "Join Us").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".join-wizard-main")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("Chuck")
    self.driver.find_element(By.NAME, "lname").send_keys("Bartowski")
    self.driver.find_element(By.NAME, "bizname").send_keys("Spy Inc")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("Supreme Chancellor")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("chuckyb")
    self.driver.find_element(By.ID, "password").send_keys("spyislife")
    self.driver.find_element(By.CSS_SELECTOR, ".admin-main").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".errorMessage")
    assert len(elements) > 0
  
