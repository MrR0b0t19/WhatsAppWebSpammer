# WHATSAPP WEB SPAMMER

Este script de Python te permite enviar mensajes y/o imágenes a múltiples contactos en WhatsApp Web de forma automática. Puedes usarlo para enviar mensajes o imágenes a una lista de contactos predefinida.

# Nota: Este script se creó con fines educativos y no se debe utilizar para enviar spam no solicitado o cualquier actividad ilegal o no ética. El uso indebido del script puede violar los términos de servicio de WhatsApp y de otras plataformas, así que úsalo con responsabilidad.

# Requisitos previos

Asegúrate de tener Python 3.x instalado en tu sistema.
Tener instalador selenium 

        pip install selenium
    
Descarga e instala el navegador Google Chrome si aún no lo tienes.

# Configuración

Clona o descarga este repositorio en tu sistema.

Abre el archivo Whatweb.py en un editor de texto y modifica los siguientes parámetros según tus necesidades:
        contactos: Agrega los nombres de los contactos a los que deseas enviar mensajes.
        mensaje: Especifica el mensaje que deseas enviar.
        archivo_errores y archivo_enviados: Estos archivos se utilizan para rastrear los contactos a los que se enviaron mensajes con éxito y los errores encontrados.
        delay_entre_mensajes: Tiempo de espera entre el envío de mensajes en segundos.
        ruta_imagen (opcional): Si deseas enviar una imagen junto con el mensaje, proporciona la ruta de la imagen.

Guarda los cambios en el archivo Whatweb.py.

# Uso

1.- Abre una terminal en la ubicación donde se encuentra el script script.py.
2.- Ejecuta el script utilizando el siguiente comando:

    python Whatweb.py

Sigue las instrucciones en la terminal para escanear el código QR de WhatsApp Web manualmente. Esto es necesario para iniciar la sesión de WhatsApp Web.

si envias una imagen debes copiar la imagen con ctrl + C para que el script lo copie usando Ctrl + V 

El script comenzará a enviar mensajes a los contactos en la lista. Verás el progreso en la terminal, incluyendo los contactos a los que se envían mensajes con éxito y los errores, si los hay.

Una vez que se complete el envío de mensajes, el script mostrará un mensaje de éxito.

Puedes verificar los archivos enviados.txt y no_enviados.txt para obtener una lista de contactos a los que se enviaron mensajes y aquellos que experimentaron errores.

# Notas

Asegúrate de que el número de contactos en la lista coincida con la cantidad de contactos a los que deseas enviar mensajes.
Asegúrate de que el navegador Google Chrome esté instalado y configurado correctamente.

# Advertencia

Este script debe utilizarse con responsabilidad y respetando las leyes y regulaciones aplicables. No lo uses para enviar spam no solicitado o cualquier actividad ilegal o no ética. El mal uso de este script puede tener consecuencias legales y violar los términos de servicio de WhatsApp u otras plataformas.
