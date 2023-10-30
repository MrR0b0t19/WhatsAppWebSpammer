from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# URL de WhatsApp Web
whatsapp_url = "https://web.whatsapp.com/"

# Lista de contactos a los que se enviara
contactos = [
    "1uno", "2dos", "3tres", "4cuatro", "5cinco", "6seis", "7siete", "8ocho", "9nueve", "10diez",
    "11once", "12doce", "13trece", "14catorce", "15quince", "16dieciséis", "17diecisiete", "18dieciocho", "19diecinueve", "20veinte",
    "21veintiuno", "22veintidós", "23veintitrés", "24veinticuatro", "25veinticinco", "26veintiséis", "27veintisiete", "28veintiocho", "29veintinueve", "30treinta",
    "31treinta y uno", "32treinta y dos", "33treinta y tres", "34treinta y cuatro", "35treinta y cinco", "36treinta y seis", "37treinta y siete", "38treinta y ocho", "39treinta y nueve", "40cuarenta",
    "41cuarenta y uno", "42cuarenta y dos", "43cuarenta y tres", "44cuarenta y cuatro", "45cuarenta y cinco", "46cuarenta y seis", "47cuarenta y siete", "48cuarenta y ocho", "49cuarenta y nueve", "50cincuenta",
    "51cincuenta y uno", "52cincuenta y dos", "53cincuenta y tres", "54cincuenta y cuatro", "55cincuenta y cinco", "56cincuenta y seis", "57cincuenta y siete", "58cincuenta y ocho", "59cincuenta y nueve", "60sesenta",
    "61sesenta y uno", "62sesenta y dos", "63sesenta y tres", "64sesenta y cuatro", "65sesenta y cinco", "66sesenta y seis", "67sesenta y siete", "68sesenta y ocho", "69sesenta y nueve", "70setenta",
    "71setenta y uno", "72setenta y dos", "73setenta y tres", "74setenta y cuatro", "75setenta y cinco", "76setenta y seis", "77setenta y siete", "78setenta y ocho", "79setenta y nueve", "80ochenta",
    "81ochenta y uno", "82ochenta y dos", "83ochenta y tres", "84ochenta y cuatro", "85ochenta y cinco", "86ochenta y seis", "87ochenta y siete", "88ochenta y ocho", "89ochenta y nueve", "90noventa",
    "91noventa y uno", "92noventa y dos", "93noventa y tres", "94noventa y cuatro", "95noventa y cinco", "96noventa y seis", "97noventa y siete", "98noventa y ocho", "99noventa y nueve", "100cien"
]
#mensaje de texto que deseas enviar 
mensaje = "prueba de envio"
archivo_errores = "no_enviados.txt"
archivo_enviados = "enviados.txt"

#se definen funciones de validaciones de envio y errores

def enviados(contacto):
    with open(archivo_enviados, "a") as archivo:
        archivo.write(f"{contacto}\n")

def errores(contacto):
    with open(archivo_errores, "a") as archivo:
        archivo.write(f"{contacto}\n")

def conteo_envio():
    try:
        with open(archivo_enviados, "r") as archivo:
            lineas  = archivo.read().splitlines()
            return len(lineas)
    except FileNotFoundError:
        return 0 
    
def conteo_errores():
    try:
        with open(archivo_errores, "r") as archivo:
            linea_e = archivo.read().splitlines()
            return len(linea_e)
    except FileNotFoundError:
        return 0



# Tiempo de espera entre mensajes (en segundos)
delay_entre_mensajes = 5  # 1 minuto

# Inicializar el navegador chrome
driver = webdriver.Chrome()
driver.get(whatsapp_url)

# Esperar a que el usuario escanee el código QR manualmente 
input("Escanea el código QR de WhatsApp Web y presiona Enter cuando estés listo...")

print("en proceso")
# Espera implícita de 2 segundos


# Función para enviar una imagen y txt a un contacto
driver.implicitly_wait(2)
def envio(contacto, mensaje): 
    try:
        # campo de búsqueda por xpath
        search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/div[2]/div/div[1]/p')#.double_click()
       # funciones de pantalla con selenium
        search_box.send_keys(Keys.CONTROL, 'a')
        search_box.send_keys(Keys.BACKSPACE)
        search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/div[2]/div/div[1]/p')
        search_box.send_keys(contacto)
        search_box.send_keys(Keys.RETURN)

        # Esperar un momento para que aparezca la conversación
        time.sleep(2)

        # Enviar el mensaje
        input_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        input_box.send_keys(mensaje)
        input_box.send_keys(Keys.RETURN)
        time.sleep(1)


        #envio de la imagen tomando mecanismo de portapapeles
        attachment_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        attachment_button.send_keys(Keys.CONTROL, 'v')
        attachment_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')#.click()
        #time.sleep(.1)
        attachment_button.click()
        time.sleep(.5)
      
        #salir de pantalla de envio 

        cierre = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[3]/div/div[3]/div/div ')
        cierre.click()
        cierre = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]/div')
        cierre.click()

        
        time.sleep(.5)
        #validacion de envio 
        enviados(contacto)

#error con validacion
    except Exception as e:
        errores(contacto)
        print(f"No pude enviar el mensaje   a {contacto} :( ")
       
       

# Loop para enviar imágenes a cada contacto en la lista
for contacto in contactos:
   envio(contacto, mensaje) 
time.sleep(delay_entre_mensajes)

# Cerrar el navegador cuando hayas terminado
correcto = conteo_envio()
incorrecto = conteo_errores()
# Mensaje de éxito
print(f"SE HA COMPLETADO EL SPAM FELICIDADES SOS UN HACKER ATTE: Fan_tasma xD")

#guarda aqui los enviados
with open(archivo_enviados, "a") as archivo:
            archivo.write(f"se envio a: {correcto} contactos\n")
       
#guarda aqui los errores
with open(archivo_errores, "a") as archivo:
            archivo.write(f"no se envio a: {incorrecto} contantos\n")
    

#cierra navegador
driver.quit()

#imprimeme en pantalla los enviados y los errores
print(f"ENVIADOS CON EXITO: {correcto}")
print(f"ERRORES: {incorrecto}")

