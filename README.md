# Vinuesa-TerceraEntregaCoder
Se realiza la entrega final para el curso de Python en CoderHouse

En el proyecto se utiliza Django para la creación de una pagina, en este caso, la creación de un sistema el cual almacena datos de alumnos.

[!TIP]
Como inicializar el proyecto.

# INICIALIZAR PROYECTO

1. creamos una carpeta donde vamos a meter el proyecto

2. entramos en la carpeta y la abrimos con vscode

3. clonamos el repositorio en la carpeta git clone <url repositorio>

4. creamos el entorno virtual python -m venv <nombre_de_la_carpeta_que_contiene_el_entorno_virtual>

5. activamos el entorno virtual

### Windows
source .venv/Scripts/activate
. .venv/Scripts/activate

### Linux/Mac
source .venv/bin/activate
. .venv/bin/activate

6. crear la base de datos con python manage.py makemigrations y luego `python manage.py migrate`

7. si desea crear un usuario puede hacerlo con python `manage.py createsuperuser`

8. Inicializar el proyecto (LocalHost) `python manage.py runserver`

## MODO DE USO

Para poder utilizar correctamente el proyecto es importante iniciar sesión con el superusuario o crear uno mismo. Si no realizamos el logueo no podremos utilizar las distintas funciones del proyecto ya que esta limitado para usuarios logueados.

## INFORMACIÓN DEL PROYECTO
$TEMPLATES/HOME$: El mismo se encuentra construido con Django, por lo tanto respeta el patrón MVT
Dentro del mismo podemos encontrar la aplicación llamada *home* la cual cuenta con diferentes archivos. Entre ellos podemos encontrar la carpeta *templates/home* la cual cuenta con los archivos HTML.

$FORMS$:  El archivo *forms* donde en la misma es creado el formulario para el ingreso de los datos.

$MODELS$: Dentro del archivo *models* podemos encontrarnos con la creación de los modelos para la base de datos sql.

$URLS$: Dentro de este archivo es donde tendremos y manejaremos las distintas páginas que vamos a mostrar.

$VIEWS$: Dentro de este archivo tenemos un poco lo que es el comportamiento que van a tener las páginas, asi también, la muestra y la obtención de datos a entre HTML y la base de dato.


