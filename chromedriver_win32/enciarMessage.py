from selenium import webdriver

driver = webdriver.Chrome("X:\Recursos Sistema\cambioTasa\chromedriver_win32\chromedriver.exe")

# Navegar a la página web de WhatsApp
driver.get("https://web.whatsapp.com/")

# Esperar a que el usuario escanee el código QR con su dispositivo móvil
input("Escanea el código QR y presiona Enter cuando hayas iniciado sesión...")

# Buscar el grupo al que quieres enviar el mensaje y hacer clic en él
search_box = driver.find_element_by_xpath('//div[@data-testid="chat-list-search"][@data-tab="3"]')
search_box.send_keys("Rebels Without a Cause")
search_box.click()

# Escribir y enviar el mensaje al grupo
message_box = driver.find_element_by_xpath('//span[@class="selectable-text copyable-text"][@data-tab="10"]')
message_box.send_keys("Mensaje de ejemplo")
send_button = driver.find_element_by_xpath('//span[@data-testid="send"]')
send_button.click()

# Cerrar el navegador
driver.quit()