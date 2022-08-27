# importar as bibliotecas que serão usadas no programa:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# chama o driver do chrome, e se não tiver instalado, já instala:
chrome_driver = ChromeDriverManager().install()

# cria o serviço que o driver vai usar
service = Service(chrome_driver)

# Cria uma variável de opções para mandar para o WebDriver 
options = webdriver.ChromeOptions() 

# previne erros/alertas no terminal:
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# mantém o navegador aberto:
options.add_experimental_option("detach", True)

# cria o WebDriver e abre o navegador
driver = webdriver.Chrome(service=service, options=options)

# vai até a URL:
driver.get("https://www.geeksforgeeks.org/")

# põe o navegador em tela cheia (maximiza a janela):
driver.maximize_window()

# uma pausa de 5 segundos para esperar a página carregar:
time.sleep(5)

# acha um elemento que é um link com texto dentro, escrito "Sign In"
button = driver.find_element("link text", "Sign In")

# faz clicar no botão
button.click()
