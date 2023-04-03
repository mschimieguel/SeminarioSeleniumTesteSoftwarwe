from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#codigo Não funcional
#apenas para exemplificar


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.youtube.com.br/")




elemento = driver.find_element(By.CLASS_NAME, "class_name_value")
elemento.click()




caixaPesquisa = driver.find_element(By.ID, "id_name_value")
caixaPesquisa.send_keys("Eletrônico")
caixaPesquisa.send_keys(Keys.RETURN)




caixaPesquisa = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.ID, "cb1-edit")
    )
)
caixaPesquisa.send_keys("Eletrônico")
caixaPesquisa.send_keys(Keys.RETURN)
