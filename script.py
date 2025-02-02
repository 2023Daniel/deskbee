from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import chromedriver_autoinstaller  # Para instalar o ChromeDriver automaticamente

def calcular_data_valida():
    data_atual = datetime.now()
    data_valida = data_atual + timedelta(days=30)
    
    while data_valida.weekday() in [4, 5, 6]:  # 4=sexta, 5=sábado, 6=domingo
        data_valida += timedelta(days=1)
    
    return data_valida.strftime("%d%m%Y")

# Instalar o ChromeDriver automaticamente e verificar se não ocorre erro
try:
    chromedriver_autoinstaller.install()
except Exception as e:
    print(f"Erro ao instalar o ChromeDriver: {e}")
    exit(1)

options = Options()
options.add_argument('--headless')  # Executar em modo headless
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service()

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.maximize_window()

    driver.get("https://fiserv.deskbee.app/login")

    # Aguardar e preencher e-mail
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite seu e-mail']"))
    )
    email_input.send_keys("danielluis.david@fiserv.com")

    # Aguardar e preencher senha
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite sua senha']"))
    )
    password_input.send_keys("Welcome@3")

    # Aguardar e clicar em Entrar
    entrar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Entrar')]"))
    )
    entrar_button.click()

    # Aguardar e clicar em Reserva Estação
    reserva_estacao_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Reserva Estação']"))
    )
    reserva_estacao_button.click()

    # Aguardar o campo de data
    data_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Data da reserva, inserir dia, mês e ano']"))
    )

    # Preencher a data válida
    data_valida = calcular_data_valida()
    data_input.send_keys(data_valida)

    # Aguardar e preencher horário de início
    hora_inicio_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de início, inserir somente números']"))
    )
    hora_inicio_input.send_keys("0900")

    # Aguardar e preencher horário de fim
    hora_fim_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de fim, inserir somente números']"))
    )
    hora_fim_input.send_keys("1800")

    # Aguardar e clicar em Lista
    lista_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Lista']"))
    )
    lista_button.click()

    # Aguardar e preencher o campo de busca
    busca_estacao_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Buscar estação de trabalho pelo nome, pressione enter para completar sua busca']"))
    )
    busca_estacao_input.send_keys("EST 8.128")

    # Aguardar o tempo necessário para a busca ser realizada
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Selecionar EST 8.127, Paulista › São Paulo › 8º Andar']"))
    )

    # Clicar no botão "Selecionar"
    selecionar_button = driver.find_element(By.XPATH, "//button[@aria-label='Selecionar EST 8.127, Paulista › São Paulo › 8º Andar']")
    selecionar_button.click()

    # Clicar no botão de confirmação
    confirmar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn') and contains(., 'CONFIRMO QUE LI E ESTOU DE ACORDO')]"))
    )
    confirmar_button.click()

finally:
    driver.quit()
