from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho do ChromeDriver - Alterar para o caminho real no seu sistema
driver_path = "C:\\webdrivers\\chromedriver.exe"  # Exemplo, altere conforme seu sistema

# Inicia o navegador com a forma correta de passar o caminho do ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Maximizar a janela do navegador
    driver.maximize_window()

    # Acessar a página de login
    driver.get("https://fiserv.deskbee.app/login")

    # Esperar até o campo de e-mail estar visível e preencher
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite seu e-mail']"))
    )
    email_input.send_keys("danielluis.david@fiserv.com")

    # Esperar até o campo de senha estar visível e preencher
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite sua senha']"))
    )
    password_input.send_keys("Welcome@3")

    # Esperar até o botão "Entrar" estar visível e clicar
    entrar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Entrar')]"))
    )
    entrar_button.click()

    # Esperar a página carregar e clicar no botão "Reserva Estação"
    reserva_estacao_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Reserva Estação']"))
    )
    reserva_estacao_button.click()

    # Esperar a página carregar e localizar o campo de data
    data_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Data da reserva, inserir dia, mês e ano']"))
    )
    data_input.send_keys("01022025")

    # Localizar o campo de horário de início e digitar o horário
    hora_inicio_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de início, inserir somente números']"))
    )
    hora_inicio_input.send_keys("0900")

    # Localizar o campo de horário de fim e digitar o horário
    hora_fim_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de fim, inserir somente números']"))
    )
    hora_fim_input.send_keys("1800")

    # Esperar a página carregar e clicar no botão "Lista"
    lista_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Lista']"))
    )
    lista_button.click()

 # Esperar a página carregar e localizar o campo de busca da estação
    busca_estacao_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Buscar estação de trabalho pelo nome, pressione enter para completar sua busca']"))
    )

    # Digitar o texto "EST 8.127" para buscar pela estação
    busca_estacao_input.send_keys("EST 8.127")

    # Esperar que a busca seja realizada, se necessário
    time.sleep(3)  # Ajuste o tempo dependendo da resposta do sistema
    
    # Localizar o botão "Selecionar" e clicar
    selecionar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Selecionar EST 8.127, Paulista › São Paulo › 8º Andar']"))
    )
    selecionar_button.click()
    
    # Localizar e clicar no botão "CONFIRMO QUE LI E ESTOU DE ACORDO"
    confirmar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn') and contains(., 'CONFIRMO QUE LI E ESTOU DE ACORDO')]"))
    )
    confirmar_button.click()



finally:
    # Aguardar alguns segundos antes de fechar o navegador
    time.sleep(5)  # Tempo reduzido para uma execução mais rápida
    driver.quit()
