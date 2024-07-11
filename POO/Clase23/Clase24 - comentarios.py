# El modelo (base de datos - logica - visual) (3 partes) se llama MVC. En DJANGO se llama MVT
# Como en la clase 18
# M = BD, V = visual, C = logica
# En Django las carpetas son: M = models (BaseD.), V = views (logica), T = templates(visual)

# La carpeta 'templates' hay que crearla manualmente dentro del proyecto, porque python esta diseñado para
# backend por eso no la crea automaticamente
# para crear automaticamente el codigo basico en html hay que poner !
# para poner comentarios en html seleccionas la linea y vas a edit y clickeas en toggle line comment
# <!-- si ponemos {% %} podemos escribir en lenguaje python en un archivo html -->

 # -- todos los comandos se hacen el manage.py desde el cmd, siempre es "python manage.py 'comando' "
# makemigrations: busca si hay nuevos cambios
# migrate: guarda esos cambios
# como el git push y git commit
# python manage.py runserver para iniciar el server, luego entramos a la url del server, ej: http://127.0.0.1:8000/ y le agregamos admin despues de la /.
# para entrar como admin hay que crear un usuario y contraseña. ponemos python manage.py createsuperuser y lo creamos. si le damos enter sin poner nada en el mail no lo pide despues
# para cambiar el lenguaje vamos a settings.py en LANGUAGE_CODE = 'es-arg'

# bootstrap es un framework para usar partes de una pagina html
# para importarlo en el html copiamos los estilos css <link href=etc..> donde dice 2. Include Bootstrap’s CSS and JS.
# arriba del <title>
# luego los scripts que estan justo abajo de eso y lo pegamos adentro del body al final
