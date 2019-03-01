from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class NotaFiscalPaulista():

    URL_LOGIN      = "https://www.nfp.fazenda.sp.gov.br/login.aspx"
    URL_CUPOM      = "https://www.nfp.fazenda.sp.gov.br/EntidadesFilantropicas/CadastroNotaEntidadeAviso.aspx"

    entidade_teste = "ASSOCIACAO COMUNITARIA E BENEFICENTE PE JOSE AUGUSTO MACHADO MOREIRA"
    mes_teste      = "02"
    xml_code       = "35190112875486000190590002449750346665260479"

    #sethings
    chorome_options = Options()
    chorome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install())

    #driver = webdriver.Firefox()

    def __init__(self, cpf, password):
        self.__cpf      = cpf
        self.__password = password


    def close(self):
        self.driver.close()

    def login(self):
        self.driver.get(self.URL_LOGIN)
        time.sleep(3)

        #set CPF
        self.driver.find_element_by_id('UserName').send_keys(self.__cpf)
        #set Password
        self.driver.find_element_by_id('Password').send_keys(self.__password)
        self.driver.find_element_by_id('Login').click()
        time.sleep(1)
        self.gerarCupom()


    def gerarCupom(self):
        self.driver.get(self.URL_CUPOM)
        time.sleep(1)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        self.driver.find_element_by_id('ctl00_ConteudoPagina_btnOk').click()
        time.sleep(1)
        self.selectEntidade()


    def selectEntidade(self):
        # select
        self.driver.find_element_by_xpath( "//select[@name='ctl00$ConteudoPagina$ddlEntidadeFilantropica']/option[text()='" + self.entidade_teste + "']").click()
        self.driver.find_element_by_xpath("//select[@name='ctl00$ConteudoPagina$ddlMes']/option[text()='" + self.mes_teste + "']").click()
        self.driver.find_element_by_id("ctl00_ConteudoPagina_btnNovaNota").click()
        time.sleep(1)

    def salvarCupom (self, cupom):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@title='Digite ou Utilize um leitor de código de barras ou QRCode']").send_keys(Keys.HOME, cupom)
        self.driver.find_element_by_id('btnSalvarNota').click()

        try:
            response = self.driver.find_element_by_id('lblInfo')
            response = "REALIZADO"
        except:
            response = 'ERRO'
        print(response)
        time.sleep(2)