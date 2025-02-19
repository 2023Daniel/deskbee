from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
import os

def calcular_data_valida():
    data_atual = datetime.now()
    data_valida = data_atual + timedelta(days=30)
    
    while data_valida.weekday() in [5, 6]:  # Evitar sábado e domingo
        data_valida += timedelta(days=1)
    
    return data_valida.strftime("%d%m%Y")

# Configurar WebDriver no ambiente do GitHub Actions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Rodar sem interface gráfica
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/local/bin/chromedriver")  # Caminho do ChromeDriver no GitHub Actions
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.maximize_window()
    driver.get("https://fiserv.deskbee.app/login")

    # Clicar no botão "Lista"
    inicio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='q-app']/div/div/div/main/form/div/div/div[2]/div[2]/div/div[2]/button"))
    )
    inicio_button.click()

    # Preencher e-mail e senha
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite seu e-mail']"))
    )
    email_input.send_keys(os.getenv("EMAIL"))

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite sua senha']"))
    )
    password_input.send_keys(os.getenv("SENHA"))

    # Clicar no botão "Entrar"
    entrar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Entrar')]"))
    )
    entrar_button.click()

    # Aguardar e clicar no botão "Reserva Estação"
    reserva_estacao_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Reserva Estação']"))
    )
    reserva_estacao_button.click()

    # Inserir data válida
    data_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Data da reserva, inserir dia, mês e ano']"))
    )
    data_input.clear()
    data_input.send_keys(calcular_data_valida())

    # Inserir horários
    hora_inicio_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de início, inserir somente números']"))
    )
    hora_inicio_input.send_keys("0900")

    hora_fim_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de fim, inserir somente números']"))
    )
    hora_fim_input.send_keys("1800")

    # Clicar no botão "Lista"
    lista_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Lista']"))
    )
    lista_button.click()

    # Buscar estação
    busca_estacao_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Buscar estação de trabalho pelo nome, pressione enter para completar sua busca']"))
    )
    busca_estacao_input.send_keys("EST 8.128")

    # Esperar o botão de seleção aparecer
    selecionar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Selecionar EST 8.128, Paulista › São Paulo › 8º Andar']"))
    )
    selecionar_button.click()

    # Confirmar a reserva
    confirmar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn') and contains(., 'CONFIRMO QUE LI E ESTOU DE ACORDO')]"))
    )
    confirmar_button.click()

    # Esperar a reserva ser concluída antes de fechar
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[contains(text(), 'Reserva concluída')]"), "Reserva concluída")
    )

finally:
    time.sleep(5)  # Tempo reduzido para uma execução mais eficiente
    driver.quit()
