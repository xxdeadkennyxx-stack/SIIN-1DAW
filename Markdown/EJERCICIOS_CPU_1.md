# Ejercicios CPU1

## 1) **Realiza una búsqueda de “explicación memoria cache”, en Google y lo mismo en Perplexity.ai ¿Cuál da mejores respuestas?**
### Explicaión memoria cache.
## Google.
La memoria caché es un tipo de almacenamiento de datos utilizado para almacenar información de acceso frecuente para un tiempo de respuesta más rápido.

## Perplexity.

Una caché (o memoria caché) es un componente de hardware o software que almacena temporalmente datos de acceso frecuente para que las solicitudes futuras de esos datos se puedan atender mucho más rápido. Funciona como una capa intermedia entre el usuario (o el procesador) y la fuente original de los datos (como la RAM, el disco duro o un servidor), reduciendo el tiempo de espera y mejorando el rendimiento general.

¿Cómo funciona?
El principio básico es simple: cuando se solicita un dato por primera vez, el sistema lo obtiene de la fuente original (que puede ser lenta) y guarda una copia en la caché. Las siguientes veces que se necesite ese mismo dato, el sistema lo recupera directamente de la caché, que es mucho más rápida, en lugar de volver a buscarlo en la fuente original. Este proceso se llama almacenamiento en caché o caching.

## Mi opinion 

La respuesta de Perplexity es demasiado extensa deberia de ser mas concisa deberia de ser mas tipo "Una cache es un componente de hardware o software que almacena información de forma temporal para datos de uso recurrente"

## 2) **Emplea en Perplexity el siguiente prompt**
 *“Hola, buenos dias . A partir de ahora serás un experto en Hardware de
ordenadores. Quiero que mantengamos una conversación escrita. Te haré
preguntas sobre temas básicos de informática y quiero respuestas entendibles y
concisas.”*

1. ¿Qué partes froma la CPU y a que se dedica cada una de ellas?

La CPU se compone principalmente de la **unidad de control**, que coordina las instrucciones; la **ALU**, que realiza cálculos y comparaciones; y los **registros y caché**, que guardan datos temporales muy rápido.
Los **núcleos** permiten que la CPU ejecute varias tareas al mismo tiempo 

2. ¿Cómo funciona una ALU y porqué debe sincronizarse con la Unidad control?

La ALU (Arithmetic Logic Unit) recibe datos y realiza cálculos o comparaciones, como sumar, restar o decidir si un número es mayor que otro.
Debe sincronizarse con la **Unidad de Control** porque esta le indica qué operación hacer, con qué datos y cuándo; así la CPU ejecuta las instrucciones en el orden correcto.

3. ¿Qué es el direccionamiento? ¿Qué tipos existen?

El direccionamiento es la forma en que una instrucción indica a la CPU dónde está el dato con el que debe trabajar.

Tipos principales: **inmediato** (el dato va en la instrucción), **directo** (indica su dirección en memoria), **indirecto** (indica dónde encontrar la dirección), **por registro, indexado y relativo** (calculan la dirección usando registros y desplazamientos).

4. ¿Qué tienen que ver los registros con el sincronismo?

Los registros guardan temporalmente datos, instrucciones y resultados mientras la CPU trabaja.
El **reloj** marca cuándo pueden actualizarse esos registros; así, la Unidad de Control, la ALU y la memoria intercambian información ordenadamente, sin mezclar pasos de distintas instrucciones.

5. ¿Qué es el zócalo de una placa base?

El zócalo o socket es la zona de la placa base donde se coloca y conecta la CPU.
La sujeta y permite que reciba energía y se comunique con la RAM y los demás componentes; por eso, el zócalo de la placa y el procesador deben ser compatibles.

## 3) Explica, con tus propias palabras, el siguiente gráfico:

![Grafico](assets/imagen_grafico.jpg)

El grafico esta dividido en dos, la parte de arriba es sin tecnologia **HT Technology** y la parte de abajo con **HT Technology**, en la parte alta del grafico se puede ver como el proceso es de forma lineal lo que provoca que el flujo de **throughput** sea mas lente, en la parte inferior del grafico se ve como el proceso deja de ser lineal para pasar a ser en paralelo haciendo el trabajo mucho mas eficiente.

## 4) Explica, con un gráfico de creación propia, porqué es importante la memoria caché y cuantos tipos existen.

![](assets/{733BADBE-941A-4921-AD12-6FA6D361DBA9}.png)

La caché es un "conector" entre el procesador y el almacenaje, tenemos caché de tipo "Hardware" y "Software"

- **HARDWARE**

1. **L1**: Es la memoria mas cercana al procesador es la memoria mas rapida pero la que menos espacio tiene-
2. **L2**: Es una memoria un poco mas lenta pero con mas almacenaje (256KB y 8MB)
3. **L3**: ES mas lenta que las anteriores pero con mas almacenaje (4MB y +50MB)

- **SOFTWARE**

1. **CACHÉ WEB**: Es la que almacena las partes de las páginas web que se visitan frecuentemente (imagenes, scripts)
2. **CACHÉ DE DISCO**: Utiliza una porción de la memoria RAM libre para retener datos leídos recientemente de una unidad de almacenamiento físico
3. **CACHÉ EN UNIDADES SSD**: Memoria interna o reservada (como DRAM o HMB en unidades de estado sólido) que acelera la lectura y escritura de los datos antes de pasarlos a las celdas de memoria permanentes

## 5) Pedir a una IA explicación de “ancho de banda” y algún ejercicio fácil de entender para después exponerlo en clase.

**¿Qué es el ancho de banda?**
Es la cantidad máxima de datos que pueden viajar por una conexión a la vez. Se mide en bits por segundo (bps, Kbps, Mbps, Gbps)

Analogía: imagina una tubería de agua. El ancho de banda es el grosor de la tubería: cuanto más ancha, más agua (datos) puede pasar al mismo tiempo.

## 6) Pedir a alguna IA un ejemplo real de la necesidad de conocer el “ancho de banda” en una empresa informática.

**¿Por qué es importante el ancho de banda para una empresa informática?**
Porque determina cuántos datos pueden moverse a la vez por su red, y eso afecta directamente a:

- **Productividad**: si el ancho de banda es insuficiente, las aplicaciones van lentas y los empleados pierden tiempo.

- **Operaciones en la nube**: casi todo el software empresarial actual (correo, videollamadas, copias de seguridad) depende de tener capacidad suficiente.

- **Atención al cliente**: una red lenta afecta la experiencia del usuario y del cliente.

- **Seguridad**: para que firewalls, antivirus y detección de intrusos funcionen bien, hace falta una conexión estable y con capacidad suficiente.

- **Prevención de cuellos de botella**: si muchos empleados usan la red a la vez y no hay ancho de banda, la red se congestiona y se bloquea.

En resumen: conocer y gestionar el ancho de banda permite a la empresa trabajar sin interrupciones, proteger sus datos y dar un buen servicio.




