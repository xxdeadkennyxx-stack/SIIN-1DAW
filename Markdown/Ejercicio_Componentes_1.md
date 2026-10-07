# DEFINICIÓN BÁSICA

## FASE 1: Comprender el componente, comceptors clave 

 * Tarea 1.1: **Definición básica**
La **CPU** es el «cerebro» del ordenador encargado de interpretar y ejecutar las instrucciones de los programas. Su función principal es procesar los datos recibidos, realizar cálculos y coordinar.

 * Tarea 1.1: **Descubrimiento de las Métricas Clave**

 **Hercios (GHz - Gigahertzios)**
 ¿Qué significan? Indican la frecuencia de reloj de la CPU, es decir, el número de ciclos de reloj que realiza en un segundo. $1 \text{ GHz} = 1.000.000.000 \text{ ciclos por segundo}$.¿En qué influyen? Determinan la velocidad bruta con la que un solo núcleo puede ejecutar instrucciones individuales.Importancia: A mayor frecuencia (GHz), más rápido realiza la CPU las tareas que dependen de un solo hilo (single-core). Sin embargo, la frecuencia no se puede comparar directamente entre arquitecturas o generaciones distintas de procesadores, ya que las CPUs más modernas ejecutan más instrucciones por ciclo (IPC).

**Núcleos e Hilos (Cores / Threads)**

¿Qué significan?

Núcleos (Cores): Son las unidades físicas de procesamiento independientes dentro del chip de la CPU.

Hilos (Threads): Son las secuencias de tareas o pipelines de instrucciones virtuales que la CPU administra. Mediante tecnologías como Hyper-Threading (Intel) o SMT (AMD), un solo núcleo físico puede gestionar dos hilos simultáneamente.

¿En qué influyen? Definen la capacidad de multitarea y el rendimiento en tareas paralelizadas.

Importancia: Más núcleos e hilos permiten ejecutar múltiples aplicaciones al mismo tiempo o procesar programas optimizados para repartir carga de trabajo masiva (como renderizado 3D, edición de vídeo multicanal o compilación de código).

**TDP (Thermal Design Power / Potencia de Diseño Térmico)**

¿Qué significa? Se mide en vatios (W) y representa la cantidad máxima de calor que genera el procesador bajo una carga de trabajo teórica máxima y que el sistema de refrigeración está diseñado para disipar.

¿En qué influyen? Determina el tipo de disipador/refrigeración que requiere el procesador y da un parámetro clave del consumo energético y la eficiencia térmica del sistema.

Importancia: Un TDP elevado exige disipadores de calor más eficientes (o sistemas de refrigeración líquida) y fuentes de alimentación de mayor capacidad. En CPUs modernas, el consumo pico real (Power Limit / PL2) puede llegar a duplicar o superar el TDP base anunciado por el fabricante.

## FASE 2

### TAREA 2.1: Definición i Conectividad.

Definición de la CPU
La CPU (Unidad Central de Procesamiento) es el cerebro del ordenador, encargada de interpretar y ejecutar las instrucciones de los programas, así como de coordinar el funcionamiento de todos los demás componentes del sistema.

Conexiones físicas e interacción en la placa base
Sócalo (Socket): Es el zócalo o ranura física de la placa base donde se instala directamente la CPU y que realiza el contacto eléctrico y de datos a través de sus pines.

Memoria RAM: Se conecta directamente mediante los canales de memoria (controlador de memoria integrado en la CPU) para leer y escribir los datos de trabajo a gran velocidad.

Líneas PCIe (PCI Express): Es el bus de datos de alta velocidad que conecta la CPU de forma directa con tarjetas de expansión (como la tarjeta gráfica/GPU) y unidades de almacenamiento rápidas (como los SSD NVMe M.2).

### TAREA2.2: Modelos Actuales.

Arquitecturas de escritorio recientes de Intel (2024 - 2026)
Intel ha abandonado la nomenclatura clásica "Core i" (i5, i7, i9) en sus últimas generaciones de escritorio, dando paso a la nomenclatura Core Ultra.

Intel Core Ultra Serie 2 (Arquitectura Arrow Lake / Socket LGA1851): Lanzada a finales de 2024 y consolidada como la arquitectura de referencia para equipos de escritorio. Introduce un diseño basado en chiplets (tiles separados para CPU, GPU y NPU) y prescinde del Hyper-Threading tradicional para mejorar significativamente la eficiencia energética y las temperaturas.

Intel Core 14ª Generación (Arquitectura Raptor Lake Refresh / Socket LGA1700): Se mantiene como opción de transición en gamas medias y de entrada, utilizando la nomenclatura clásica (Core i5, i7, i9).

Casos de uso: Ultra 5 vs. Ultra 9
Intel Core Ultra 5 (ej. Ultra 5 245K):

A quién va dirigido: Usuarios de gama media, gamers con presupuesto equilibrado, estudiantes y profesionales de ofimática avanzada o edición ligera de foto y vídeo.

Caso de uso: Ideal para quienes buscan una excelente relación calidad-precio, alto rendimiento en juegos y gran eficiencia sin necesidad de invertir en sistemas de refrigeración extremos.

Intel Core Ultra 9 (ej. Ultra 9 285K):

A quién va dirigido: Profesionales, creadores de contenido de alto nivel y usuarios entusiastas.

Caso de uso: Diseñado para cargas de trabajo pesadas que aprovechan al máximo la multitarea y el procesamiento en paralelo: renderizado 3D, edición de vídeo en 4K/8K, compilación de código complejo, simulaciones y tareas de Inteligencia Artificial en local.

## FASE 3 

### Ejercicio 3.1: Mas ideas. 

¿Qué es el efecto Bottleneck (Cuello de Botella) entre CPU y GPU?El cuello de botella ocurre cuando uno de los dos componentes principales (CPU o GPU) limita la capacidad de rendimiento del otro porque no puede procesar los datos a la misma velocidad.En un videojuego, por ejemplo, la CPU calcula la física, la IA de los personajes y prepara la escena, mientras que la GPU renderiza los gráficos y los muestra en pantalla. Si la CPU no procesa la información lo suficientemente rápido, la GPU se queda "esperando" sin trabajar al $100\%$ de su capacidad, generando caídas de fotogramas (FPS) o tirones (stuttering).Existen dos escenarios habituales:Cuello de botella de CPU: La CPU está al $100\%$ de uso y la GPU al $60-70\%$. Ocurre en juegos competitivos a resoluciones bajas (1080p) o con CPUs muy antiguas combinadas con tarjetas gráficas muy potentes.Cuello de botella de GPU: La GPU trabaja al $99\%$ mientras la CPU está a bajo uso. Esto es lo ideal en gaming, ya que significa que estás aprovechando toda la potencia gráfica contratada (habitual a 1440p o 4K).¿Cómo evitarlo al planificar el montaje de un PC?Equilibrar el presupuesto y la gama: No combines un procesador de gama de entrada con una tarjeta gráfica de gama alta (por ejemplo, un Intel Core Ultra 3 o Core i3 con una RTX 4080/5080), ni viceversa.Considerar la resolución de pantalla:1080p (Full HD): Requiere una CPU más potente para mantener tasas altas de FPS.1440p / 4K: La carga se traslada principalmente a la GPU, por lo que la CPU no necesita ser la más cara del mercado.Revisar pruebas y benchmarks específicos: Antes de comprar, busca análisis reales del juego o software que vayas a usar combinando exactamente ese modelo de CPU y GPU a la resolución que pretendes jugar.

