from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Caminho para o ChromeDriver no Windows
driver_path = "C:\\Projects\\web-crawler-github-tasks\\driver\\chromedriver.exe"

# Inicializar o WebDriver do Selenium
driver = webdriver.Chrome(service=Service(executable_path=driver_path))

try:
    # Abrir uma página web
    driver.get("http://www.google.com")

    # Esperar um momento para garantir que a página esteja carregada
    time.sleep(2)

    # Localizar um elemento na página (por exemplo, a barra de pesquisa do Google)
    search_box = driver.find_element(By.NAME, 'q')

    # Interagir com o elemento (por exemplo, enviar uma pesquisa)
    search_box.send_keys('Thiago Artur Schumann' + Keys.RETURN)

    # Esperar um momento para ver o resultado
    time.sleep(5)

finally:
    # Fechar o navegador ao finalizar, mesmo se ocorrer um erro
    driver.quit()
