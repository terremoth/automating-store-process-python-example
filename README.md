# [EN] Automating Stuff Python - Example
An attempt to convince my friend that he can automate his boring work learning python

## Some User Story
- You are a clothing store administrative employee, you do some boring manual and repetitive task everyday
- this clothing store has 2 branches, you work in the main (1).
- your job:
  - you need to access (login) in the company's system (web app) from branch 2
  - the system has only one page and only shows a random report in a table from clothes and its quantity left 
  - you need to get the top 3 products that has less quantity, insert in 3 specific cells in an Excel (xlsx) spreadsheet (that you have in your desktop predefined)
  - then you need to multiply the price of the product (you already have/know the prices inside the excel file) from those you got by its quantity left, mutiplied by the actual dollar value. (The original currency format is in BRL (reais))
  - then you need to generate a PDF from this spreadsheet with the day, month and year in the report file name, like: report-running-out-27-08-2022.pdf
  - send this PDF to your boss by email
  
### Instructions 
- If you use GMAIL, you will need to create an unique password for only this app to send emails, so:
    - go to: https://myaccount.google.com/security
    - now go to the section "How to login to Google"
    - go to "App Passwords" (https://myaccount.google.com/apppasswords)
    - from the list to generate, select "other" then click "generate"
    - this password will be used by you to type/paste when our script asks for it so it can connect to Google and send the email
    - With admin rights, in your terminal/cmd, install the requirements on this folder with: ```pip3 install -r requirements.txt``` 

---

# [PT-BR] Automatizando coisas com Python - Exemplo
Uma tentativa de convencer meu amigo que ele pode automatizar o trabalho tedioso dele e de quebra aprender Python

## Histórias do usuário, o que ele tem que fazer:
- Você trabalha como colaborador numa loja de roupas, você faz algumas tarefas tediosas manuais e repetitivas todo dia
- essa loja de roupas tem 2 filiais, você trabalha na filial 1
- seu trabalho:
  - você precisa logar no sistema (aplicação web) da filial 2
  - o sistema só tem uma página e mostra um relatorio randomiconuma tabela de roupas e suas quantidades restantes
  - você precisa pegar os 3 produtos que tenham menos quantidades, inserir em 3 celulas específica em uma planilha de excel (xlsx) que você já tem na sua área de trabalho
  - então você precisa multiplicar o preço de cada produto (você já tem/sabe os preços dentro da planilha) pelas quantidades deles e depois multiplicado pelo preço atual do dolar que você precisa olhar todo dia
  - então você precisa gerar um PDF dessa planilha com o dia, mês e ano no nome do relatório, como por exemplo: relatorio-acabando-27-08-2022.pdf
  - enviar por email este PDF gerado para seu chefe
  
