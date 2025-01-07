from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def realizar_cadastro():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://exemplo.com/cadastro")
        driver.find_element(By.ID, "nome").send_keys("Seu Nome")
        driver.find_element(By.ID, "email").send_keys("seuemail@exemplo.com")
        driver.find_element(By.ID, "senha").send_keys("sua_senha")
        driver.find_element(By.ID, "btnEnviar").click()
        time.sleep(5)
    finally:
        driver.quit()

realizar_cadastro()
