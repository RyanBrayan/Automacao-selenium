from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# navegar ate o whatsapp web
driver =  webdriver.Chrome()
driver.get("https://web.whatsapp.com")
sleep(30)

# Definir contatos/grupos e mensagem a ser enviada
contatos = ['Nome do contato']
mensagem = 'Mensagem que você deseja enviar'

# Buscar contato ou grupo 
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    sleep(4)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
    campo_mensagem.click()
    sleep(3)
    campo_mensagem.send_keys(mensagem)
    sleep(2)
    campo_mensagem.send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
