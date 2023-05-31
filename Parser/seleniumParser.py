import pickle
from selenium import webdriver

from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument("--disable-notifications")
options.add_argument(f'user-argent={useragent.random}')
driver = webdriver.Chrome(r'C:\Users\den-s\OneDrive\Desktop\HackathonFinal\Parser\chromedriver',options=options)
driver.maximize_window()
try:   
    driver.get("https://www.facebook.com/groups/708481315831119?sorting_setting=CHRONOLOGICAL")
    for cookie in pickle.load(open('Parser\cookies','rb')):
            driver.add_cookie(cookie)
    driver.refresh()
    timer = 1
    while True:
            searching_element = driver.find_elements(By.LINK_TEXT,'1 д.')
            if len(searching_element) == 0:
                timer+=1
                print(timer)
                driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(1)
            else:
                print('Success')
                resp = driver.page_source
                with open(r'C:\Users\den-s\OneDrive\Desktop\HackathonFinal\Parser\FacebookPage.html','w',encoding = 'utf-8') as file:
                    file.write(resp)
                time.sleep(1)
                break
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

