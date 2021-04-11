import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


#1.Pegar conteúdo HTML a partir da URL

url = "https://www.guiainvest.com.br/lista-acoes/default.aspx?listaacaopage=1"


option = Options()

option.headless = True

driver = webdriver.chrome()

driver.get(url)

time.sleep(10)



driver.find_element_by_xpath("//div[@class='rgMasterTable']//tr//td//[@hlNome]").click()

element = driver.find_element_by_xpath("//div[@class='rgMasterTable']//tr")

html_content = element.get_attribute('outerHTML')

#2. Parsear o conteúdo HTML - BeatifulSoup

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find(name='table')

#3. Estrurar contpudo em uma Data Frame - Pandas

df_full = pd.red_html( str(table) )[0].head('10')

driver.quit()