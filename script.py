from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Instala automaticamente o ChromeDriver correto
chromedriver_autoinstaller.install()

# Configuração para rodar no ambiente headless
options = Options()
options.add_argument('--headless')  # Para rodar sem interface gráfica
options.add_argument('--no-sandbox')  # Necessário para CI
options.add_argument('--disable-dev-shm-usage')  # Para evitar falhas de memória

# Inicializa o driver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)  # Espera implícita de 20 segundos para todos os elementos

try:
    # Maximizar a janela do navegador (não visível em modo headless)
    driver.maximize_window()

    # Acessar a página de login
    driver.get("https://fiserv.deskbee.app/login")

    # Preencher o campo de e-mail
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite seu e-mail']"))
    )
    email_input.send_keys("danielluis.david@fiserv.com")

    # Preencher o campo de senha
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Digite sua senha']"))
    )
    password_input.send_keys("Welcome@3")

    # Clicar no botão "Entrar"
    entrar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Entrar')]"))
    )
    entrar_button.click()

    # Clicar no botão "Reserva Estação"
    reserva_estacao_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Reserva Estação']"))
    )
    reserva_estacao_button.click()

    # Preencher a data da reserva
    data_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Data da reserva, inserir dia, mês e ano']"))
    )
    data_input.send_keys("01022025")

    # Preencher o horário de início
    hora_inicio_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de início, inserir somente números']"))
    )
    hora_inicio_input.send_keys("0900")

    # Preencher o horário de fim
    hora_fim_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Horario de fim, inserir somente números']"))
    )
    hora_fim_input.send_keys("1800")

    # Clicar no botão "Lista"
    lista_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-msgid='Lista']"))
    )
    lista_button.click()

    # Buscar pela estação de trabalho
    busca_estacao_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Buscar estação de trabalho pelo nome, pressione enter para completar sua busca']"))
    )
    busca_estacao_input.send_keys("EST 8.127")

    # Clicar no botão "Selecionar"
    selecionar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Selecionar EST 8.127, Paulista › São Paulo › 8º Andar']"))
    )
    selecionar_button.click()

    # Confirmar a reserva
    confirmar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn') and contains(., 'CONFIRMO QUE LI E ESTOU DE ACORDO')]"))
    )
    confirmar_button.click()

finally:
    # Fechar o navegador
    driver.quit()