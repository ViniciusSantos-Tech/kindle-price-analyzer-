#FEITO POR VINICIUS SANTOS-TECH
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

TabPreço = []
TabTitle = []

def Raspagem():
    navegador = webdriver.Chrome()

    try:
        navegador.get("https://www.amazon.com.br/")
        wait = WebDriverWait(navegador, 10)
        navegador.maximize_window()

        Barra = wait.until(Ec.element_to_be_clickable(('id', "twotabsearchtextbox")))
        Barra.click()

        Barra.send_keys("Kindle")
        Barra.send_keys(Keys.ENTER)
        sleep(2)

    except Exception as e:
        print(e)

    try:
        resultados = navegador.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        print("------------RESULTADO-DA-PESQUISA------------------")
        for i, Resultado in enumerate(resultados[:5], 1):

            Preço = Resultado.find_element("class name", "a-price-whole")
            Title = Resultado.find_element("class name", 'a-size-base-plus.a-spacing-none.a-color-base.a-text-normal')
            PreçoLimpo = float(Preço.text.replace(".", "").replace(",", ""))

            print(f'|Preço: R${Preço.text}')
            print(f'|Titulo: {Title.text}')
            print("|----------------------")
            TabPreço.append(PreçoLimpo)
            TabTitle.append({
                'titulo': Title.text,
                'preco': PreçoLimpo
            })
           
    except Exception as e:
        print(e)
    Analizador()

#---------------------------------------------------------------------------------------------

def Analizador():
    if TabPreço:
        mais_barato = min(TabPreço)
        mais_caro = max(TabPreço)

        produto_barato = TabTitle[TabPreço.index(mais_barato)]
        produto_caro = TabTitle[TabPreço.index(mais_caro)]
    
    print("|===============================================")
    print("| RESUMO DA BUSCA:")
    print("|===============================================")
    print(f"|MAIS BARATO: {produto_barato['titulo'][:50]}...")
    print(f"|Preço: R$ {produto_barato['preco']:.2f}")
    print(f"|MAIS CARO: {produto_caro['titulo'][:50]}...")
    print(f"|Preço: R$ {produto_caro['preco']:.2f}")
    print(f"|Diferença: R$ {mais_caro - mais_barato:.2f}")
    print("------------------------------------------------------------------------------------")
Raspagem()
