# El Corazón del PC

## FASE 1: Comprender las Métricas Clave 

**Tarea 1.1: Descrubimiento de los  comceptos Clave**

1. GHz (Frecuencia de Reloj)
Qué es: Es el ritmo al que late la CPU. Mide cuántos miles de millones de ciclos de instrucciones puede ejecutar por segundo (1 GHz = 1.000 millones de ciclos/s).

En qué influye: Determina la velocidad pura en tareas de un solo hilo (rendimiento mononúcleo). A mayor frecuencia, más rápido procesa individualmente cada instrucción. Es clave en aplicaciones como juegos o software que no aprovechan múltiples núcleos simultáneamente.

2. Cores y Threads (Núcleos y Hilos)
Qué son:

Cores (Núcleos): Son las "mentes" físicas o unidades de procesamiento independientes dentro del chip.

Threads (Hilos): Son las vías virtuales que permiten a cada núcleo físico gestionar dos tareas o flujos de instrucciones a la vez (tecnología conocida como Hyper-Threading en Intel o SMM/Multithreading en AMD).

En qué influyen: Determinan la capacidad de trabajo en paralelo (multitarea). Tener más núcleos e hilos permite ejecutar aplicaciones pesadas simultáneamente (ej. renderizado 3D, edición de vídeo, compilación de código o streaming mientras juegas) sin que el sistema se colapse.

3. TDP (Thermal Design Power / Potencia de Diseño Térmico)
Qué es: Mide la cantidad máxima de calor (expresada en vatios, W) que el sistema de refrigeración del PC necesita disipar cuando la CPU trabaja bajo carga típica.

En qué influye: Determina el consumo eléctrico y las necesidades de refrigeración. Un TDP más alto exige un disipador o refrigeración líquida de mayor rendimiento y una fuente de alimentación más potente. También condiciona si el procesador es apto para portátiles finos o para ordenadores de sobremesa de alto rendimiento.

## Fase 2: Desafío Interactivo.

**Tarea 2.1: El Juego de Adivinanzas e interrogatorio**

**Paso 1 (Inicia el juego)**

Soy el encargado de coordinar a un auténtico ejército en la sombra: cuando un trabajo pesado como un renderizado 3D o la edición de vídeo llega al procesador, divido el problema en partes para ejecutarlo todo al mismo tiempo. Me verás anunciado en la caja con dos números separados por una barra (como 8/16 ó 16/32), donde la segunda cifra duplica a la primera gracias a la magia del multithreading. Si intentas jugar, quizás no siempre me aproveches entero, pero si me faltan efectivos, todo tu sistema se ralentizará en multitarea.

**Paso 2 (Interactúa y ponla a prueba)**

*¿Como te repartes el trabajo?*

Para abordar el proyecto de forma ordenada, lo ideal es repartir el trabajo en cuatro bloques claros.

**Paso 3 (Adivina y valida)**

*Eres los nucleos y hilos*

¡Premio! Has acertado de lleno. Soy los Núcleos y Hilos (Cores/Threads).

## FASE 3: Encargo de Empresa 

**Tarea 3.1: Elección de CPU (Ofimática vs IA Local)** 

**Opción Caso B:** IA Local (PC para modelos de LLM y código)
Procesador recomendado: AMD Ryzen 9 7900X (o Intel Core i9-14900K)

Justificación:

Ofrece una alta capacidad multihilo gracias a sus 12 núcleos y 24 hilos con velocidades de hasta 5,6 GHz, ideal para la cuantización y precarga de grandes modelos de lenguaje en memoria. Se ubica en la gama alta/entusiasta y cuenta con soporte para instrucciones AVX-512, cruciales para acelerar cargas de trabajo e inferencia de IA en CPU. Permite un gran ancho de banda con memoria RAM DDR5 de alta velocidad, garantizando una ejecución fluida en procesamiento local paralelo

**Tarea 3.2: Registro Técnico**






 










