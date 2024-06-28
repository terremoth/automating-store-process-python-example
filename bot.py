from driver import *
from dollar import *
from email_sender import send_email_with_attach
from math import nan
from dotenv import dotenv_values
from selenium.webdriver.common.by import By
import pandas
import time
from html_to_pdf import convert_html_to_pdf

config = dotenv_values(".env")
url = config["clothing_store_url"]
email = config["clothing_store_email"]
password = config["clothing_store_password"]

# cria o WebDriver e abre o navegador
driver = webdriver.Chrome(service=service, options=options)

# vai até a URL:
driver.get(url)

# põe o navegador em tela cheia (maximiza a janela):
driver.maximize_window()

# uma pausa de 5 segundos para esperar a página carregar:
time.sleep(2)

email_input = driver.find_element(by=By.ID, value="email")
email_input.send_keys(email)

password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(password)

submit_button = driver.find_element(By.TAG_NAME, 'button')

# faz clicar no botão
submit_button.click()
time.sleep(2)
# Agora vai abrir a página do relatório...

table = driver.find_element(By.TAG_NAME, 'table')

products_list = {}

for row in table.find_elements(By.TAG_NAME, 'tr'):

    cells_in_this_row = []
    last_property = None

    for index, cell in enumerate(row.find_elements(By.TAG_NAME, 'td')):

        if cell.text is not None:
            if index == 0:
                last_property = cell.text
                products_list[cell.text] = None
            else:
                products_list[last_property] = int(cell.text)

sorted_products_by_less_quantity = sorted(products_list.items(), key=lambda item: item[1])
only_three_less_quantity = dict(sorted_products_by_less_quantity[0:3])

print(only_three_less_quantity)

# import pdfkit
excel_file_name = 'running-out-template.xlsx'
df = pandas.read_excel(excel_file_name, header=None)

for index, product in enumerate(only_three_less_quantity):
    df.at[index + 1, 0] = product
    df.at[index + 1, 1] = only_three_less_quantity[product]

df.at[6, 1] = dolar_price()

for index, product in enumerate(only_three_less_quantity):
    df.at[index + 1, 2] = round(float(only_three_less_quantity[product]) * dolar_price(), 2)

df = df.replace(nan, '', regex=True)

print(df)

test_name = "{}_{}".format(int(time.time()), excel_file_name)
df.to_excel(test_name, index=False)

html_file_name = "{}.html".format(test_name)
pdf_file_name = "{}.pdf".format(test_name)
df.to_html(html_file_name)
time.sleep(1)

convert_html_to_pdf(open(html_file_name, "r+b"), pdf_file_name)

from_email = config["my_work_email"]
to_email = config["boss_email"]

send_email_with_attach(from_email, to_email, pdf_file_name)
