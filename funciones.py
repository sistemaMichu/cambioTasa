import requests, datetime, bs4, urllib3
from selenium import webdriver

def tasaDelDia():
    urllib3.disable_warnings()
    url = 'https://www.bcv.org.ve'
    response = requests.get(url, verify=False)
    html = response.content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', {'id': 'dolar'})
    for div in divs:
        strong = div.find('strong')
        if strong:
            value = strong.text.replace(',', '.')
    contar = 0
    redondeo = ""
    aux = 0   
        
    for lugar in value:
        if contar <= 2:
            redondeo += lugar
            if lugar == ".":
                aux = True
            if aux:
                contar += 1
                
    redondeo = str(float(redondeo) + 0.01)

    contar = 0
    tasa = ""
    aux = 0      
    for lugar in redondeo:
        if contar <= 2:
            tasa += lugar
            if lugar == ".":
                aux = True
            if aux:
                contar += 1
    return tasa

def fechaTasa():
    # Obtener la fecha actual
    fechaHoy = datetime.datetime.now()
    diaSiguiente = fechaHoy + datetime.timedelta(days=1)
    fechaFinal = diaSiguiente.strftime('%d-%m-%Y')
    return fechaFinal




def enviarMessage():
# Iniciar el navegador Chrome
    driver = webdriver.Chrome("X:\Recursos Sistema\cambioTasa\chromedriver_win32\chromedriver.exe")

    # Navegar a la página web de WhatsApp
    driver.get("https://web.whatsapp.com/")

    # Esperar a que el usuario escanee el código QR con su dispositivo móvil
    input("Escanea el código QR y presiona Enter cuando hayas iniciado sesión...")

    # Buscar el grupo al que quieres enviar el mensaje y hacer clic en él
    search_box = driver.find_element_by_xpath('//input[@title="Cuadro de texto para ingresar la búsqueda"][@data-tab="3"]')
    search_box.send_keys("Rebels Without a Cause")
    search_box.click()

    # Escribir y enviar el mensaje al grupo
    message_box = driver.find_element_by_xpath('//span[@class="selectable-text copyable-text"][@data-tab="10"]')
    message_box.send_keys("Mensaje de ejemplo")
    send_button = driver.find_element_by_xpath('//span[@data-testid="send"]')
    send_button.click()

    # Cerrar el navegador
    driver.quit()

                

    