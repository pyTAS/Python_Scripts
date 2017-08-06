import time
import selenium
from selenium import webdriver


driver = webdriver.Chrome("d:/02_IT/04_Projects_py_win/00_seleniumChromeWebDriver/chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Main_Page")

tperiod = 60
tincr = 3
tstart = 0

while tstart < tperiod:
    time.sleep(tincr)
    driver.refresh()
    tstart += tincr

if tstart == tperiod:
    driver.close()
