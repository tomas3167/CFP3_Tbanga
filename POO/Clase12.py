  # 1) Geolocalizador
#181.14.211.107 -- IP publica
# pip install geocoder
import geocoder as geo

# info = geo.ip("181.14.211.107")
# print(info.city)
# print(info.country)
# print(info.address)
# print(info.hostname)
# print(info.latlng) #La latitud y longitud

  # 2) Descargar videos de youtube
  # Instalar la biblioteca pytube para descargar videos de youtube
# pip install pytube
import pytube
def descargar_video(url, carpeta):
     #Crear un objeto Youtube con la URL proporcionada
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res="240p").first() #-- Filtra los streams de video para obtener el primer stream que tenga resolucion de 720p
    video.download(output_path = carpeta)
    print(f"El video se esta descargando.... en {carpeta}")

    streams = youtube.streams.filter(progressive=True)
    for stream in streams:
        print(stream.resolution)

#C:\Users\admin\Downloads\Videos --- Hay que cambiar las barras invertidas (\) por las /
descargar_video("https://www.youtube.com/watch?v=nNkw3Fo9Aqk","C:/Users/admin/Downloads/Videos")