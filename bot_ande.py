import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options

nro = input('Ingrese el NIS\n')

mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
dir = sys.path[0]
download_folder = dir


path = dir + '/geckodriver.exe'

#No muestra el navegador
options = Options()
options.add_argument('--headless')

fp = webdriver.FirefoxProfile()
#Carpeta de descarga
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", download_folder)
#Descarga Automaticamente PDFs
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
fp.set_preference("pdfjs.disabled", True)

#Abre un navegador
browser = webdriver.Firefox(firefox_profile=fp, options=options, executable_path=path)

#Ingresa en la pagina de la Ande
browser.get('https://www.ande.gov.py/')

elem = browser.find_element_by_id('nis2') 
elem.send_keys(nro + Keys.RETURN)

time.sleep(10)

#Ingresa el NIS en la caja de busqueda
nis = browser.find_element_by_id('in-Factura_nis')
nis.send_keys(nro)

time.sleep(0.2)

nis.send_keys(Keys.RETURN)

time.sleep(10)

#Apreta el boton de descargar
browser.find_element_by_css_selector('a.btn:nth-child(9)').click()

time.sleep(5)
browser.quit()
