# Descarga los precios de todas las gasolineras de España desde el servicio
# REST del Ministerio y los guarda en un CSV.
# Solo usa librerías que vienen con Python: no hay que instalar nada.

import csv
import json
import urllib.request
from datetime import date

URL = ("https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/"
       "PreciosCarburantes/EstacionesTerrestres/")

# Pedimos los datos en formato JSON
peticion = urllib.request.Request(
    URL, headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0"}
)

print("Descargando datos del Ministerio (puede tardar unos segundos)...")
with urllib.request.urlopen(peticion, timeout=120) as respuesta:
    texto = respuesta.read().decode("utf-8-sig")

datos = json.loads(texto)
lista = datos["ListaEESSPrecio"]  # una entrada por gasolinera

# Reunimos todos los nombres de columna, en el orden en que aparecen
columnas = []
for gasolinera in lista:
    for clave in gasolinera:
        if clave not in columnas:
            columnas.append(clave)

nombre_fichero = f"gasolineras_{date.today().isoformat()}.csv"
with open(nombre_fichero, "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(lista)

print(f"Fecha de los datos según el Ministerio: {datos.get('Fecha')}")
print(f"{len(lista)} gasolineras guardadas en {nombre_fichero}")
print("Columnas:", columnas)