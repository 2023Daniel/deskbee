from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Removendo chromedriver_autoinstaller devido ao erro de import

def log(mensagem):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {mensagem}")

def calcular_data_valida():
    data_atual = datetime.now()
    data_valida = data_atual + timedelta(days=30)
    
    while data_valida.weekday() in [4, 5, 6]:  # 4=sexta, 5=sábado, 6=domingo
        data_valida += timedelta(days=1)
    
    return data_valida.strftime("%d%m%Y")

options = Options()
options.add_argument('--headless')  # Executar em modo headless
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service()
driver = webdriver.Chrome(service=service, options=options)
log("Driver iniciado.")

try:
    driver.maximize_window()
    log("Janela maximizada.")

    driver.get("https://fiserv.deskbee.app/login")
    log("Página de login acessada.")

    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite seu e-mail']"))
    )
    email_input.send_keys("danielluis.david@fiserv.com")
    log("E-mail inserido.")

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite sua senha']"))
    )
    password_input.send_keys("Welcome@3")
    log("Senha inserida.")

    entrar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Entrar')]"))
    )
    entrar_button.click()
    log("Botão 'Entrar' clicado.")

    reserva_estacao_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Reserva Estação']"))
    )
    reserva_estacao_button.click()
    log("Acessando tela de reserva de estação.")

    data_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Data da reserva, inserir dia, mês e ano']"))
    )
    data_valida = calcular_data_valida()
    data_input.send_keys(data_valida)
    log(f"Data da reserva inserida: {data_valida}.")

    hora_inicio_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de início, inserir somente números']"))
    )
    hora_inicio_input.send_keys("0900")
    log("Horário de início inserido: 0900.")

    hora_fim_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de fim, inserir somente números']"))
    )
    hora_fim_input.send_keys("1800")
    log("Horário de fim inserido: 1800.")

    lista_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Lista']"))
    )
    lista_button.click()
    log("Botão 'Lista' clicado.")

    busca_estacao_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Buscar estação de trabalho pelo nome, pressione enter para completar sua busca']"))
    )
    busca_estacao_input.send_keys("EST 8.128")
    log("Estação de trabalho buscada: EST 8.128.")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Selecionar EST 8.128, Paulista › São Paulo › 8º Andar']"))
    )
    selecionar_button = driver.find_element(By.XPATH, "//button[@aria-label='Selecionar EST 8.128, Paulista › São Paulo › 8º Andar']")
    selecionar_button.click()
    log("Estação 8.128 selecionada.")

    confirmar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn') and contains(., 'CONFIRMO QUE LI E ESTOU DE ACORDO')]"))
    )
    confirmar_button.click()
    log("Reserva confirmada.")

except Exception as e:
    log(f"Erro: {e}")
finally:
    driver.quit()
    log("Driver encerrado.")
