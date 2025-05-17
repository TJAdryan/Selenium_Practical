# practical selenium, xlsxwriter and pandas snippets
### functions I find myself needing to reference from time to time
### I know it needs to be cleaned up

Getting started:
from selenium import webdriver
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()  
driver = webdriver.Chrome()
driver.get("http://www.google.org")


