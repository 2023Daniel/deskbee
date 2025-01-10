from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import logging
import time

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Instala automaticamente o ChromeDriver correto
chromedriver_autoinstaller.install()

# Configuração para rodar no ambiente headless
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Inicializa o driver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)

try:
    logging.info("Iniciando o script Selenium.")

    # Acessar a página de login
    driver.get("https://fiserv.deskbee.app/login")
    logging.info("Página de login acessada.")

    # Preencher o campo de e-mail
    email_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite seu e-mail']"))
    )
    email_input.send_keys("danielluis.david@fiserv.com")
    logging.info("E-mail preenchido.")

    # Preencher o campo de senha
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite sua senha']"))
    )
    password_input.send_keys("Welcome@3")
    logging.info("Senha preenchida.")

    # Clicar no botão "Entrar"
    entrar_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Entrar')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", entrar_button)  # Garante visibilidade
    ActionChains(driver).move_to_element(entrar_button).click().perform()  # Alternativa para cliques
    logging.info("Botão 'Entrar' clicado.")

    # Clicar no botão "Reserva Estação"
    reserva_estacao_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Reserva Estação']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", reserva_estacao_button)
    reserva_estacao_button.click()
    logging.info("Botão 'Reserva Estação' clicado.")

    # Preencher a data da reserva
    data_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Data da reserva, inserir dia, mês e ano']"))
    )
    data_input.clear()
    data_input.send_keys("01/02/2025")  # Adicionando o formato correto
    logging.info("Data da reserva preenchida.")

    # Pequena pausa para evitar conflitos
    time.sleep(2)

    # Preencher o horário de início
    hora_inicio_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de início, inserir somente números']"))
    )
    hora_inicio_input.clear()
    hora_inicio_input.send_keys("0900")
    logging.info("Horário de início preenchido.")

    # Preencher o horário de fim
    hora_fim_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de fim, inserir somente números']"))
    )
    hora_fim_input.clear()
    hora_fim_input.send_keys("1800")
    logging.info("Horário de fim preenchido.")

    # Clicar no botão "Lista"
    lista_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Lista']"))
    )
    lista_button.click()
    logging.info("Botão 'Lista' clicado.")

    # Buscar pela estação de trabalho
    busca_estacao_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Buscar estação de trabalho pelo nome, pressione enter para completar sua busca']"))
    )
    busca_estacao_input.send_keys("EST 8.127")
    logging.info("Texto 'EST 8.127' digitado no campo de busca.")

    # Aguardar que o botão "Selecionar" esteja disponível e clicá-lo
    selecionar_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Selecionar EST 8.127')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", selecionar_button)
    selecionar_button.click()
    logging.info("Botão 'Selecionar' clicado.")

    # Confirmar a reserva
    confirmar_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn') and contains(., 'CONFIRMO QUE LI E ESTOU DE ACORDO')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", confirmar_button)
    confirmar_button.click()
    logging.info("Reserva confirmada.")

except Exception as e:
    driver.save_screenshot("erro.png")  # Captura um screenshot no caso de erro
    logging.error(f"Erro durante a execução do script: {e}")
finally:
    driver.quit()
    logging.info("Navegador fechado.")
