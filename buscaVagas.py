from selenium import webdriver
import openpyxl
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://www.advancerh.com.br/vagas.php")

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

divs = soup.find_all("div", {"class": "card-body"})

workbook = openpyxl.Workbook()
workbook.create_sheet('vagas')
sheet_vagas = workbook['vagas']
sheet_vagas['A1'].value = 'Vagas'
sheet_vagas['B1'].value = 'E-mail'

for item in divs:
    for i, z in zip(item.find_all("a"), item.find_all("h5")):
        sheet_vagas.append([z.text, i.text])
        print(z.text+" : "+i.text)

workbook.save('Selecao.xlsx')

