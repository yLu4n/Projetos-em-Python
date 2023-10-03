# Passo a Passo do projeto
#Passo 1: Entrar no sistema da empresa
            #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
pyautogui.PAUSE= 0.9


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#Passo 2: Fazer Login
time.sleep(3)

pyautogui.click(x=551, y=368)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste280923")
pyautogui.press("enter")
#Passo 3: Importar a base de dados do produto
import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index: 
    #Passo 4: Cadastrar um produto
    pyautogui.click(x=490, y=249)

    #preencher código

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    #apertar enviar

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(550)
