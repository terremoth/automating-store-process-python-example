from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chama o driver do chrome, e se não tiver instalado, já instala:
chrome_driver = ChromeDriverManager().install()

# cria o serviço que o driver vai usar
service = Service(chrome_driver)

# Cria uma variável de opções para mandar para o WebDriver 
options = webdriver.ChromeOptions() 
#options.add_argument("--headless") # this line makes chrome runs in backend, comment it if you want to see the window opening

options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# previne erros/alertas no terminal:
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# mantém o navegador aberto:
# options.add_experimental_option("detach", True) # will not close after script finishes

