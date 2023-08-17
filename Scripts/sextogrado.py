#libros de sexto grado
import os
import requests

urlBase = "https://www.conaliteg.sep.gob.mx"
links = [
    "/2023/P5LPM.htm",
    "/2023/P6MLA.htm",
    "/2023/P6PAA.htm",
    "/2023/P6PCA.htm",
    "/2023/P6PEA.htm",
    "/2023/P6SDA.htm",
    "/2023/P0SHA.htm",
    "/2023/P0CMA.htm",
    # Agrega más enlaces aquí
]

# Rango de imágenes a descargar (por ejemplo, del 1 al 100)
inicioIndex = 1
finalIndex = 300

# Carpeta de destino para guardar las imágenes descargadas
folderDestino = "./sextoGrado"
os.makedirs(folderDestino, exist_ok=True)

for link in links:
    full_url = urlBase + link

    for imagenIndex in range(inicioIndex, finalIndex + 1):
        imagenUrl = f"{full_url}#{imagenIndex:03d}.jpg"

        response = requests.get(imagenUrl)
        if response.status_code == 200:
            imagenNombreSecuencia = f"{link.split('/')[-1]}_{imagenIndex:03d}.jpg"
            imagenPath = os.path.join(folderDestino, imagenNombreSecuencia)

            with open(imagenPath, "wb") as img_file:
                img_file.write(response.content)

            print(f"Imagen {imagenNombreSecuencia} descargada")
        else:
            print(f"Error al descargar la imagen {imagenUrl}")

print("Proceso de descarga de imágenes completado.")

