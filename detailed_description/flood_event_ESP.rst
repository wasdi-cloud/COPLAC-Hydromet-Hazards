ES - servicio de cartografía de la extensión de las inundaciones (Flood Extent Mapping), detalles
=============================================================================================

El servicio de cartografía de la extensión de las inundaciones (FEM) se centra en la detección de inundaciones puntuales (único evento) a partir de datos de radares de apertura sintética (SAR) y satélites ópticos.
Los productos son mapas de delimitación de inundaciones para eventos específicos, con la extensión máxima derivada de la combinación de imágenes de Sentinel-1 (S1) y Sentinel-2 (S2). 

En cuanto a los productos eográficos,, el servicio FEM genera bajo demanda un mapa de extensión de una sola inundación.


.. figure:: ../_static/flood_event/1_scheme.png
    :alt: Flood Extent Mapping scheme
    :align: center
    :figwidth: 80%
    :name: fig:flood_event_scheme_esp

    Esquema sobre el flujo de trabajo del servicio de cartografía de la extensión de las inundaciones

.. raw:: html

   <div style="margin-top: 40px;"></div>

Este servicio se basa en dos cadenas de procesamiento que utilizan el algoritmo AUTOWADE (AUTOmatic Water Areas Detector), desarrollado por la CIMA Research Foundation.
La primera cadena utiliza datos ópticos para detectar zonas inundadas a partir de una única imagen Sentinel-2 (S2) obtenida tras la inundación (autowade_s2) [1]_.
La segunda cadena utiliza datos de radar de apertura sintética (SAR) y analiza un par de imágenes Sentinel-1 (S1): una obtenida antes y otra después de la inundación (autowade_s1) [2]_. 
Estas imágenes deben compartir la misma órbita relativa y cubrir la misma zona geográfica.
Ambas cadenas también utilizan los productos Copernicus DEM [3]_ y ESA global land cover [4]_ como datos auxiliares para mejorar la precisión de la detección de la extensión de las inundaciones. 
Cada algoritmo de detección de inundaciones produce un mapa clasificado con cuatro estados: píxeles enmascarados (0), no inundados (1), con agua permanente (2) e inundados (3).
Si se generan varios mapas dentro de la ventana temporal definida, estos se combinan, primero por sensores, para generar un mapa de extensión máxima (mapas de extensión máxima S1 y S2) que representa la unión de todas las áreas inundadas detectadas en las escenas disponibles.
Cuando se generan con éxito mapas de inundaciones a partir de datos S1 y S2 (es decir, cuando se dispone de datos ópticos y estos no se ven afectados por la cobertura nubosa), el servicio fusiona los dos resultados en un único mapa que representa la extensión máxima de la inundación detectada por cualquiera de las dos fuentes. 
En este caso, también se genera un mapa comparativo para resaltar las áreas de coincidencia y diferencia entre los mapas de inundaciones derivados de SAR y ópticos. Este mapa utiliza la siguiente leyenda: sin datos (0); sin inundaciones (1); un mapa con inundaciones, el otro sin inundaciones (2); un mapa con inundaciones, el otro sin datos (3); ambos mapas con inundaciones (4); agua permanente (5).

Este servicio es brindado por la CIMA Research Foundation.

.. figure:: ../_static/flood_event/2_example_colombia.png
    :alt: Flood Extent Mapping example in Colombia
    :align: center
    :figwidth: 80%
    :name: fig:flood_event_colombia_esp

    Ejemplo de productos del servicio FEM sobre Mojana (Colombia): a la izquierda, mapa de extensión de la inundación derivado de datos Sentinel-1; a la derecha, mapa comparativo (SAR y óptico). 

.. raw:: html

   <div style="margin-top: 40px;"></div>


Flujo de trabajo
-----------------------------------------

El esquema que se muestra en esta sección describe el flujo de trabajo de alto nivel del servicio FEM. 


.. figure:: ../_static/flood_event/3_workflow.png
    :alt: workflow of the FEM service
    :align: center
    :figwidth: 80%
    :name: fig:workflow_fem_esp

    Flujo de trabajo del servicio FEM.

.. raw:: html

   <div style="margin-top: 40px;"></div>

A continuación se detallan cada uno de los pasos de la cadena descritos en el flujo de trabajo FEM.

**User selection**

Componente de la plataforma donde los usuarios configuran los parámetros para la ejecución del servicio. 

**s1_grd_preprocess**

Flujo de trabajo de preprocesamiento estándar para obtener imágenes de intensidad sigma cero calibradas, corregidas y proyectadas de Sentinel-1 en dB utilizando como entrada productos GRD de Sentinel-1. El módulo de preprocesamiento incluye el emparejamiento de imágenes previas y posteriores por órbita que serán procesadas por el algoritmo autowade_s1. 

**s2_preprocess**

Preparación de datos Sentinel-2 MSI L2A y cálculo del índice espectral. El preprocesamiento incluye el enmascaramiento de nubes y sombras mediante el mapa S2 Scene CLassification (SCL), seguido de la generación del índice de agua normalizado modificado (MNDWI) [5]_. El MNDWI, con una resolución de 20 m, se extrae y se utiliza como entrada para los siguientes pasos del flujo de trabajo.

**autowade_s1** 

La ejecución de autowade_s1 implica detectar áreas inundadas y áreas de agua permanentes a partir de datos de Sentinel-1 utilizando un enfoque de detección de cambios entre imágenes previas y posteriores al evento adquiridas en la misma órbita [2]_.
En primer lugar, el método excluye las zonas escarpadas y urbanas mediante datos auxiliares [3]_ [4]_. Las masas de agua permanentes se identifican utilizando un enfoque de amortiguación desde el borde. En este proceso, se aplica un algoritmo de agrupamiento no supervisado a la imagen VV copolarizada para segmentar grupos de píxeles similares. Se supone que la clase con la mediana más baja representa píxeles de agua.
A continuación, la zona de agua dinámica continua (CDWA) derivada se compara con la capa de agua permanente de referencia de WorldCover. La intersección entre ambos conjuntos de datos se somete a una detección de bordes, seguida de una operación de amortiguación para obtener una distribución bimodal de píxeles de agua y no agua. Una vez lograda esta distribución, se aplica un método de umbral automático.
Para refinar la clasificación del agua permanente, se emplea un enfoque de crecimiento regional para garantizar que se incluyan todos los píxeles de agua vecinos. Se utiliza la misma estrategia para clasificar el agua de inundación, pero en este caso, el método se aplica a la diferencia entre las adquisiciones posteriores y anteriores al evento.


**autowade_s2**

La ejecución de autowade_s2 implica la detección de áreas inundadas y permanentes a partir de una imagen única posterior al evento de Sentinel-2. 
Ciertas áreas de los datos MNDWI preprocesados se excluyen del análisis, es decir, las áreas urbanas (de ESA WorldCover). La detección de agua sigue el «enfoque de búfer a partir de clústeres», tal y como lo describen Pulvirenti et al. (2020) [1]_. Se aplica un algoritmo de agrupamiento no supervisado al índice espectral para agrupar píxeles similares dentro de la escena, suponiendo que la clase con la mediana más alta representa píxeles de agua.
La zona de agua derivada del agrupamiento (CDWA) resultante se somete a una detección de bordes, seguida de una operación de amortiguación para generar una distribución bimodal de píxeles de agua y no agua. Una vez establecida esta distribución, se aplica un método de umbral automático.
Para refinar la clasificación del agua, se utiliza un enfoque de crecimiento de regiones para garantizar que se incluyan todos los píxeles de agua vecinos. Por último, al intersectar el mapa de delineación del agua con la capa de agua de referencia (derivada de ESA WorldCover), se identifica el agua permanente (píxeles clasificados como agua tanto en WorldCover como en el mapa derivado de S2), mientras que se distingue el agua inundada (píxeles clasificados como agua solo en el mapa derivado de Sentinel-2).


**s1_fe_postprocessor** y **s2_fe_postprocessor**

Módulos para el procesamiento de imágenes que resuelven el ruido, los efectos de borde y otros problemas que pueden afectar al resultado final.

**max_extent_computation**

Algoritmo para fusionar las extensiones de inundación obtenidas por separado de Sentinel-1 y Sentinel-2, producir mapas de extensión máxima de inundación y el mapa comparativo.

**fe_result_postproc**

Módulo para el procesamiento de imágenes de los resultados finales de la extensión de la inundación. 

**Stage-out**

Puntos finales del servicio para almacenar y visualizar los resultados.


.. figure:: ../_static/flood_event/4_example_jamaica.png
    :alt: Flood Extent Mapping example in Jamaica
    :align: center
    :figwidth: 80%
    :name: fig:example_flood_event_jamaica_esp

    Ejemplo de mapa de extensión de inundaciones derivado de S1 para la región de Mojana (Colombia) a fecha de 31 de mayo de 2024.

.. raw:: html

   <div style="margin-top: 40px;"></div>


Input
-----------------------------------------

Para ejecutar el servicio se necesitan los siguientes datos:

**Imágenes Sentinel**

* Sentinel-2 L2A: uno o más mosaicos que se superponen al área de interés (AOI), capturados durante o poco después del evento de inundación.
* Sentinel-1 GRD: dos conjuntos de mosaicos (o grupos de mosaicos) que se superponen al AOI, capturados antes y después del evento en la misma órbita relativa.

**Datos auxiliares: para su uso en los algoritmos AUTOWADEs**

* Copernicus DEM GLO-30: Modelo digital de elevación de Copernicus [3]_
* Worldcover: cobertura del suelo de la ESA [4]_

Parámetros
-----------------------------------------

Para ejecutar el servicio se necesitan los siguientes parámetros:

* Área de interés (Area of Interest, AOI): La región geográfica que se va a analizar.
* Tiempo de interés (Time of Interest, TOI): El intervalo de tiempo alrededor del evento que se va a analizar, para seleccionar las imágenes sobre el AOI.

Output
-----------------------------------------

El servicio producirá los siguientes resultados:

Mapa de extensión de una singola inundación.

* *Definición*: mapa de extensión de inundaciones: 0 - píxeles enmascarados; 1 - sin inundaciones; 2 - agua permanente; 3 - inundado.
* *Tipo y formato de datos*: UInt8, GeoTIFF.  
* *Resolución espacial*: 20 m.
* *Frecuencia*: obtenida bajo demanda.
* *Cobertura espacial*: El servicio está disponible para toda la región de América Latina y el Caribe.
* *Cobertura temporal*: dependiendo del tiempo de revisita combinada de los satélites Sentinel-1 y Sentinel-2. 
* *Limitaciones*: limitado por la disponibilidad de adquisiciones adecuadas de observación de la Tierra; las zonas urbanas y los terrenos escarpados quedan excluidos del análisis.

Mapa comparativo óptico y SAR de inundaciones

* *Definición*: mapa comparativo que destaca las áreas de coincidencia y diferencia entre los mapas de inundaciones derivados de SAR y ópticos. Leyenda: 0 - Sin datos; 1 - Sin inundaciones; 2 - Un mapa muestra inundaciones, el otro no; 3 - Un mapa muestra inundaciones, el otro no tiene datos; 4 - Ambos mapas muestran inundaciones; 5 - Agua permanente.
* *Tipo y formato de datos*: UInt8, GeoTIFF.  
* *Resolución espacial*: 20 m.
* *Frecuencia*: obtenida bajo demanda.
* *Cobertura espacial*: El servicio está disponible para toda la región de América Latina y el Caribe.
* *Cobertura temporal*: dependiendo del tiempo de revisita combinada de los satélites Sentinel-1 y Sentinel-2. 
* *Limitaciones*: limitado por la disponibilidad de adquisiciones adecuadas de observación de la Tierra.



Bibliografía
-----------------------------------------

.. [1] Pulvirenti, L., Squicciarino, G., Fiori, E. (2020). A Method to Automatically Detect Changes in Multitemporal Spectral Indices: Application to Natural Disaster Damage Assessment. Remote Sensing, 12(17), 2681. https://doi.org/10.3390/rs12172681
.. [2] Pulvirenti, L., Squicciarino, G., Fiori, E., Ferraris, L., & Puca, S. (2021). A Tool for Pre-Operational Daily Mapping of Floods and Permanent Water Using Sentinel-1 Data. Remote Sensing, 13(7), 1342. https://doi.org/10.3390/rs13071342
.. [3] Copernicus DEM - Global Digital Elevation Model - COP-DEM_GLO-30 https://doi.org/10.5270/ESA-c5d3d65
.. [4] WorldCover 2021 v200 - Zanaga, D., Van De Kerchove, R., Daems, D., De Keersmaecker, W., Brockmann, C., Kirches, G., Wevers, J., Cartus, O., Santoro, M., Fritz, S., Lesiv, M., Herold, M., Tsendbazar, N.E., Xu, P., Ramoino, F., Arino, O., 2022. ESA WorldCover 10 m 2021 v200. https://doi.org/10.5281/zenodo.7254221
.. [5] Xu, H. (2006). Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery. International Journal of Remote Sensing, 27(14), 3025–3033. https://doi.org/10.1080/01431160600589179
