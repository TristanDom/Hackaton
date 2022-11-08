import requests
from bs4 import BeautifulSoup
import requests 


# URL a la página la cual se desea extraer el código.
url = input("Ingrese la ruta de la página web: ")
#url = "https://blogthinkbig.com/etiquetas-html-importantes-memorizar"
  
#Mandar solicitud a la página y asignarla a una variable.
result = requests.get(url)

#Almacenar el contenido de la página en una variable.
content = result.text

#Crear un objeto BeautifulSoup con el contenido de la página.
soup = BeautifulSoup(content, 'lxml')

#Imprimir el código de la página con un formato legible.
# print(soup.prettify())

with open('ExtractorDeCodigo/IngresoWeb/Web.txt', 'w') as archivo:
    archivo.write(soup.prettify())
    print("La página se ha extraído correctamente.")