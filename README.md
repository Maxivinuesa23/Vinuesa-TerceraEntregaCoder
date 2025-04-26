# Vinuesa-TerceraEntregaCoder
Se realiza la entrega final para el curso de Python en CoderHouse

En el proyecto se utiliza Django para la creación de una pagina, en este caso, la creación de un sistema el cual almacena datos de alumnos.

El mismo cuenta con tres archivos HTML donde contamos con:

1. inicio.html: En el mismo veremos la primer página que nos comenta como utilizar el sistema.

2. crear_alumno.html: En el mismo tenemos la segunda página la cual contiene un formulario creado de forma que sea intuitiva con la ayuda de Bootstrap.

3. mostrar_alumno.html: Por ultimo podemos ver la tercer página la cual muestra todos los alumnos cargados previamente. En caso de no tener alumnos cargados la misma página se encarga de mostrar un mensaje especificando este.

## MODO DE USO

1. Al ejecutar el programa por primera vez, nos encontraremos dentro de la sección "Inicio". Es importante situarnos en la barra de navegación superior la cual cuenta con 3 opciones comentadas anteriormente.

2. Una vez situados en la barra de navegación debemos ir al apartado que dice "Crear Alumno".

3. Dentro del apartado "Crear Alumno" debemos rellenar los campos (nombre, apellido, dni, carrera). Una vez rellenado los campos debemos cargar al alumno haciendo click en el botón "Cargar Alumno".

4. Una vez cargado el alumno la misma aplicación nos llevara al apartado "Mostrar Alumno" con el o los datos cargados.

## INFORMACIÓN DEL PROYECTO
$TEMPLATES/HOME$: El mismo se encuentra construido con Django, por lo tanto respeta el patrón MVT
Dentro del mismo podemos encontrar la aplicación llamada *home* la cual cuenta con diferentes archivos. Entre ellos podemos encontrar la carpeta *templates/home* la cual cuenta con los archivos HTML.

$FORMS$:  El archivo *forms* donde en la misma es creado el formulario para el ingreso de los datos.

$MODELS$: Dentro del archivo *models* podemos encontrarnos con la creación de los modelos para la base de datos sql.

$URLS$: Dentro de este archivo es donde tendremos y manejaremos las distintas páginas que vamos a mostrar.

$VIEWS$: Dentro de este archivo tenemos un poco lo que es el comportamiento que van a tener las páginas, asi también, la muestra y la obtención de datos a entre HTML y la base de dato.


