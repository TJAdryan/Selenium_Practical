import selenium
import datetime
from datetime import timedelta
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import shutil
import cred
import os
import runpy
import chromedriver_autoinstaller
import polling2

#Headless support


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


runpy.run_path('C:/Users/.../removepopup.py')
#edit pop up scripts


#Automatically add the latest version of chromedrive to the path as needed
chromedriver_autoinstaller.install()


dropdown = Select(driver.find_element(By.ID, "dropdown_id"))
dropdown.select_by_visible_text("Option Text")
dropdown.select_by_value("option_value")
dropdown.select_by_index(0)

##Get beginning and ending date for report
Curr_date_Less14 = datetime.date.today() + datetime.timedelta(-14)
Curr_date_Less7 = datetime.date.today() + datetime.timedelta(-7)
Curr_date_Less1 = datetime.date.today() + datetime.timedelta(-1)
Curr_date= datetime.date.today()
Curr_date_Plus6 = datetime.date.today() + datetime.timedelta(+6)
Curr_date_Plus14 = datetime.date.today() + datetime.timedelta(+14)


#Variables to be changed for each script
dwnldpath=('C:/Users/dreport/...')
upldpath =("K:/Reporting/...)
currentscript=('C:/users/dreport/...')


#Delete old file from downloads folder if exists
if os.path.exists(dwnldpath):
    os.remove(dwnldpath)
else:
    print('I cannot remove, what is not there')

#Checks for pop up window and closes if found, on pop up close end script and rerun from beginning
def removepopup():
    try:
        len(driver.find_elements_by_xpath("//input[@id='btnRead']"))>0 
        el = driver.find_element_by_xpath("//input[@id='btnRead']")
        driver.execute_script("arguments[0].click();", el)
    except NoSuchElementException:
        pass
    finally:    
        driver.quit()
        runpy.run_path(currentscript)


#Set testvalue global value to 0
def stest():
    global inum
    inum =0

#Iterate testvalue to wait for report to be downloaded
def itest():
    global inum
    inum +=5
    
#Finish testvalue by exceeding value to wait
def ftest():
    global inum
    inum = 121

##To deal the unkind extra windows that have no relevance but draw the cursor


#go to the window that was just opened
driver.switch_to.window(driver.window_handles[-1])


deadwindow = gw.getWindowsWithTitle('Open')[0]
deadwindow.close()
driver.switch_to.window(driver.window_handles[0])
#driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\users\\somedirectory\\andother.csv")

##Save a picture of why something didn't work 
driver.refresh()
sleep(5)
driver.save_screenshot("C:/users/.../downloads/afterupload.png")


#Wait for download link and try to click  ~ every 5 seconds for up to 2 minutes
def gagain():
    while inum <120:
        try:
            driver.implicitly_wait(5)
            
            # driver.find_element_by_xpath("//a[@id='ReportViewer_ctl05_ctl04_ctl00_ButtonLink']/span").click()
            driver.find_element_by_id("ReportViewer_ctl05_ctl04_ctl00_ButtonImgDown").click()
            driver.find_element_by_link_text("CSV (comma delimited)").click()
            ftest()
            print("Finally")
            sleep(6)
            
        except NoSuchElementException:
            print("Not yet"+" " + str(inum))
            itest()
            gagain()

        else:
            pass



try:
     driver = webdriver.Chrome()
     driver.implicitly_wait(120)
     driver.find_element_by_id("login").submit()
     sleep(1)
     try:
         driver.find_element_by_link_text("Report").click()
     except ElementClickInterceptedException:
          removepopup()


except NoSuchElementException:
     print("Element not Found")
     driver.quit()
     

     
driver.quit()


#Move file if it is downlaoded, or rerun python script
def mvfile():
    if os.path.exists(dwnldpath):
        shutil.move(dwnldpath,upldpath)
    else:
        #try to run whole script 1 additional time
        print('File not here - starting over')
    
        
        
stest()

if inum < 10:
     mvfile()
else:
     pass  

     #Move File


