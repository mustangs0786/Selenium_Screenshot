from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
width = 3840
height = 2160
import time
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
# chrome_options.add_argument('window-size=3840x2160')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(width, height)
url = "https://en.wikipedia.org/wiki/Economy_of_Asia"
driver.get(url)
# time.sleep(3)
S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+ X)
driver.set_window_size(S('Width'), S('Height'))
# print('Window size', driver.get_window_size())
# Window size {'width': 1024, 'height': 768}

driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[4]").screenshot('screenshot.png')