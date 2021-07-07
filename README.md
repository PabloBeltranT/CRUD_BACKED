# CRUD_BACKED


- mb_mini_super:
    - asgi: Default
    - settings: Separe urlpatterns[] para tener las aplicaciones base, propias y de terceros mejor ordenadas. Agregue la url necesaria para tomar los templates de la aplicacion       mini_super_app. Mantuve la configuracion de la base de datos, archivos estaticos y middleware por default e integre la variable de entorno para configurar rest_framework, REST_FRAMEWORK.
    - urls: importe la funcion include() para incluir los archivos urls.py de la aplicacion mini_super_app y router.py de api.
    - wsgi: Default


- api: Cree un directorio para implementar rest_api, donde cree tres archivos:
    - api: Defini las diferentes vistas api para hacer CRUD (GET, POST, PUT, DELETE), tales vistas las base en funciones con ayuda del decorador @api_view.
    - routers: Este script reemplaza al script urls.py normal que se usan con vistas normales de Django, debido que cumplen la misma funcion se encarga de apuntar una url a una vista en especifico.
    - serializers: En este script defini una sola clase instanciada de ModelSerializer donde defini el modelo a utilizar en el atributo de la clase Meta, model, tambien en el atributo fields lo defini como '__all__' para que el serializador tome todos los campos del modelos e incluirlos en la serializacion, en este caso elegi una configuracion y aitenticacion por default ya que el proyecto no requeria autenticaciones especificas, tales autenticaciones se realizarian creando una instancia de serializers.Serializer donde se podria reescribir la autenticacion de cada campo y el metodo save entre otros.


- apps: Cree este directorio para almacenar las aplicaciones del proyecto y mostrar de manera mas prolija el mismo:
    - templates: En este directorio almacene los archivos html que serviran las viw solicitadas, en dichos templates inclui bootstrap para dar diseno, por lo que no cree el directoria para los archivos estaticos como css o js.
    - admin: En admin registre el modelo miniSuperModel para poder administrarlo desde el sitio administrativo de Django, para acceder al sitio administrativo cree un superusuario con nombre: superuser y contrasena: superuserpasswd.
    - apps: Aqui modifique el name de MiniSuperAppConfig para redireccionarlo a app.mini_super_app.
    - models: Aqui defini una clase intancia da models.Model llamada miniSuperMOdel donde defini los campos nombre, apellido paterno y materno, email, edad y telefono, cada uno con los requisitos propios de cada dato, tambien defini un metodo str para retornar el nombre de cada usuario.
    - objects: Aqui defini dos clases una (sortAlphabetically) para ordenar los usuarios alfabeticamente y retornar una lista de objetos o diccionarios que posteriormente las vistas la utilizan para iterar los usuairos, y (sortNumerically) que se encarga de ordenar numericamente segun la edad de menor a mayor los usuarios y retornando una lista con estos objetos o diccionarios.
    - test: Default
    - urls: Aqui defini las vistas que debieran retornan especificas url.
    - viewaa: Aqui defini seis vistas cada una encargada de ejecutar cuatro metos del request, 
    list_users(se encarga de hacer un get a la api del proyecto con ayuda de el modulo requests, serializar el response y pasar por contexto el objeto al template), 
    add_user(se encarga realizar un post con ayuda de el modulo requests, para agregar un nuevo usuario, mandando un diccionario serializado con los datos obtenidos de request.POST),
    edit_user(se encarga de editar un usuario obteniendo como parametro un primary key y haciendo un request.put de un diccionario serializado con los datos de request.POST, con ayuda de el modulo requests, a la api del proyecto y devolviendo un template de los usuarios listados),
    delete_user(se encarga de eliminar un usuario, recibiendo de como parametro el primary key del ususario),
    sort_alphabetically(se encarga de llamar al modulo objects y a una de las dos clases anterioemente mencionadas, para retornar un renderizado y pasando por contexto al template, la lista de ususarios ordenados alfabeticamente),
    sort_numerically(se encarga de instanciar a una clase del modulo objects y pasarle como parametro un request obtenido de un get hecho a la api y llamando un metodo del mismo para ordenar la lista de usuarios de menor a mayor segun la edad).


- NOTA: Este proyecto esta enfocado a la funcionalodad, simpre habra oportunidad de mejora, en aspectos como autenticacion para los metodos post, put o delete para la api rest y aspectos de optimizacion de codigo. 