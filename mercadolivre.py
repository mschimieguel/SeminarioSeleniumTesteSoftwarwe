from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.mercadolivre.com.br/")

caixaPesquisa = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cb1-edit")))

#elemento.click()

caixaPesquisa.send_keys("Eletrônico")
caixaPesquisa.send_keys(Keys.RETURN)


time.sleep(9)
#Clicando para aceitar os termos de cookie
cookies = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "cookie-consent-banner-opt-out__action--key-accept")))
cookies.click()


time.sleep(300)
driver.quit()