ES - Servicio de Mapeo de Frecuencia de Inundaciones aplicado a Colombia
=====================================================================

Resumen del servicio
----------------------

El servicio de Mapeo de Frecuencia de Inundaciones (Flood Frequency Mapping, FFM) utiliza mapas multitemporales de la extensión de las inundaciones para generar un mapa de frecuencia de inundaciones que ilustra los patrones de ocurrencia de las inundaciones. El servicio se basa en mapas de inundaciones derivados de datos ópticos y SAR que se analizan sistemáticamente en todo el archivo Sentinel-2 (L2A) y Sentinel-1 (GRD) desde 2015 hasta 2024, con actualizaciones periódicas. El servicio funciona independientemente de las activaciones de los usuarios, generando mapas actualizados de la extensión de las inundaciones utilizando datos de Sentinel-1 y Sentinel-2 y un algoritmo automatizado de detección de cambios. Con el tiempo, se analiza el conjunto completo de estos mapas de extensión de las inundaciones para producir un mapa completo de frecuencia de inundaciones que muestra la recurrencia de las inundaciones en toda la Área de Interés (Area of Interest, AOI), que para la implementación preoperativa del servicio es la región de La Mojana (Colombia).

La implementación preoperativa del servicio FFM tiene una ejecución inicial para calcular la frecuencia de inundaciones
de todo el archivo de 2015-2024. Posteriormente, el mapa de frecuencia de inundaciones se
actualiza cada seis meses, incorporando todas las nuevas adquisiciones de Sentinel-1 y
Sentinel-2 en el análisis.

El servicio ha sido desarrollado por la Fundación de Investigación CIMA y WASDI
Sarl, y está disponible a través del Entorno de Procesamiento Especializado (PE) de CopernicusLAC,
impulsado por WASDI Sarl.

Para obtener más información sobre la implementación preoperativa en Colombia, consulte :download:`esta presentación (en inglés) <../_static/UC2_tutorial/CopernicusLAC-colombia.pdf>`

.. _access-platform-uc2:

Los espacios de trabajo para el mapeo de la frecuencia de inundaciones
------------------------------------------------------------------------

El servicio Flood Frequency Mapping (FFM) se ha implementado para la Área de Interés (AOI) definida por los usuarios dentro de la región de La Mojana en Colombia.

Este servicio se proporciona a través de espacios de trabajo dedicados en el Entorno de Procesamiento Especializado (PE) de CopernicusLAC. Cada espacio de trabajo recopila los mapas de extensión de inundaciones y los mapas de frecuencia de inundaciones generados para la AOI seleccionada.

El servicio FFM está diseñado para el monitoreo continuo. Procesa todas las
imágenes satelitales disponibles sobre la AOI, genera los correspondientes mapas de inundaciones
y actualiza el mapa de frecuencia de inundaciones cada seis meses basándose en los
nuevos datos.

Debido al gran volumen de datos, y de acuerdo con los requisitos de los usuarios, los resultados del servicio se organizan en dos espacios de trabajo separados:

1. | **workspace ARCHIVO**
   | *Nombre:* **COPLAC_UC2_archivo**
   | Contiene el archivo completo de todos los mapas de extensión de inundaciones y el mapa completo de frecuencia de inundaciones para el AOI.

2. | **workspace OPERACIONAL**
   | *Nombre:* **COPLAC_UC2_operacional**
   | Una versión simplificada del archivo, que contiene solo los mapas más recientes de la extensión de las inundaciones y el último mapa actualizado de frecuencia.

Puede acceder a los espacios de trabajo (workspaces) de dos maneras:

1. Enlace directo:

-  Enlace al workspace ARCHIVO: :raw-html:`<a href="https://coplac.wasdi.net/#/edit/17c4090b-4fcf-4c5e-a994-2ee3b19f55cb" target="_blank">WASDI 2.0 - COPLAC_UC2_archivo</a>`

-  Enlace al workspace OPERACIONAL: :raw-html:`<a href="https://coplac.wasdi.net/#/edit/3c29010b-007c-4e8e-b8b0-9d9fdeaa6390" target="_blank">WASDI 2.0 - COPLAC_UC2_operacional</a>`

2. | Desde la sección del administrador de espacios de trabajo:
   | Tanto *COPLAC_UC2_archivo* como *COPLAC_UC2_operacional* son visibles en su lista de espacios de trabajo, tal y como se muestra en la Figura 9, si está **correctamente registrado como usuario de CopernicusLAC** (Consulte la sección
     :doc:`Access the platform<../specializedPE>`).

.. image:: ../_static/UC2_tutorial/image10.png
   :width: 5.39143in
   :height: 3.14961in

Figura 9. Servicio de mapeo de frecuencia de inundaciones de CopernicusLAC: acceso desde
el menú workspaces de CopernicusLAC a los espacios de trabajo dedicados *COPLAC_UC2_archivo* o *COPLAC_UC2_operacional*.

En el espacio de trabajo completo del archivo, el panel situado en la parte superior izquierda de la interfaz muestra una lista de todas las capas disponibles (Figura 10). Estas incluyen todos los datos procesados desde 2015 hasta la actualidad. Los datos se actualizan continuamente en los espacios de trabajo tan pronto como se procesan.

.. image:: ../_static/UC2_tutorial/image11.png
   :width: 5.36131in
   :height: 3.14796in

Figure 10. CopernicusLAC – Workspace del servicio Flood Frequency Mapping

Resultados, visualización de datos y download
------------------------------------------------

El servicio generará como resultado mapas GeoTIFF.

El espacio de trabajo contiene una colección de mapas de extensión de inundaciones generados a partir de imágenes satelitales Sentinel-1 (SAR) 
y Sentinel-2 (ópticas) adquiridas entre 2015 y la actualidad. 
Estos conjuntos de datos proporcionan tanto productos de extensión de inundaciones de una sola fecha como resúmenes acumulativos 
en intervalos de 16 días. Los archivos disponibles incluyen el siguiente GeoTIFF:

- ``MOJAN_[FECHA]_flood.tiff``  
  Mapa de extensión de la inundación a partir de datos **Sentinel-1 SAR** obtenidos en la *[FECHA]* (Leyenda 1).

- ``MOJAN_[FECHA]_s2-flood.tiff``  
  Mapa de extensión de la inundación a partir de datos **Sentinel-2 optical** obtenidos en la *[FECHA]* (Leyenda 1).

- ``MOJAN_[FechaInicio]_[FechaFin]_sar_flood_sum_days_16.tif``  
  Extensión máxima acumulada calculada a partir de los **mapas de extensión de inundaciones derivados del SAR** disponibles en el intervalo de 16 días definido por *FechaInicio* y *FechaFin* (Leyenda 1).

- ``MOJAN_[FechaInicio]_[FechaFin]_flood_sum_days_16.tif``  
  Extensión máxima acumulada calculada a partir de los mapas de extensión de inundaciones disponibles derivados de **SAR y ópticos**  en el intervalo de 16 días definido por *FechaInicio* y *FechaFin* (Leyenda 1).

- ``MOJAN_[FechaInicio]_[FechaFin]_frisk[DIAS].tif``  Mapa comparativo óptico y SAR de inundaciones (cuando se dispone tanto de S2 como de S1) (Leyenda 2).


*Leyenda 1*:

   0 - Sin datos

   1 - No hay inundación

   2 - Agua permanente

   3 - Áreas inundadas

*Leyenda 2*:

   0 - Sin datos

   1 - No hay inundación

   2 - Un mapa muestra inundaciones, el otro no.

   3 - Un mapa muestra inundaciones, el otro no tiene datos.

   4 - Inundación en ambos mapas

   5 - Agua permanente

Además, el espacio de trabajo proporciona capas empíricas de frecuencia de inundaciones, actualizadas cada seis meses:

- ``MOJANFFM_flood``  
  Recuento de inundaciones: número de veces que cada píxel se clasificó como inundado, en los mapas derivados de Sentinel-1.

- ``MOJANFFM_data``  
  Conteo de datos EO: número de veces que se observó cada píxel en los mapas derivados del Sentinel-1.

- ``MOJANFFM_frequency``  
  Frecuencia empírica de inundaciones basada en Sentinel-1, calculada como *conteo de inundaciones / conteo de datos* para cada píxel.

- ``MOJANS2FFM_flood``  
  Conteo de inundaciones: número de veces que cada píxel fue clasificado como inundado en los mapas derivados del Sentinel-2.

- ``MOJANS2FFM_data``  
  Conteo de datos EO: número de veces que se observó cada píxel en los mapas derivados del Sentinel-2.

- ``MOJANS2FFM_frequency``  
  Frecuencia empírica de inundaciones basada en Sentinel-2, calculada como *conteo de inundaciones / conteo de datos* para cada píxel.

Puede visualizar las capas directamente en el workspace de lo Specialized PE (entorno de trabajo especializado) o descargarlas en su dispositivo local para su posterior procesamiento.

¿Cómo mostrar datos en su workspace en lo Specialized PE?

-  Busca la capa que le interesa en su espacio de trabajo, amplía la selección, activa la capa que te interesa y haz clic en el icono de la bombilla.

-  La capa seleccionada se mostrará en el mapa y el producto debería aparecer en la lista de productos del recuadro Capas (Figura 11).

.. image:: ../_static/UC2_tutorial/image12.png
   :width: 5.36038in
   :height: 3.14961in

Figure 11. Visualización de mapas en lo Specialized PE de CopernicusLAC

¿Cómo descargar datos desde su workspace en lo Specialized PE?

-  Acceda a su espacio de trabajo en lo Specialized PE de CopernicusLAC.

-  Busque la capa que le interese en su espacio de trabajo y selecciónela (Figura 12 - 1). La opción de descarga aparecerá en la parte superior de la lista de capas (Figura 12 - 2).

   .. image:: ../_static/UC2_tutorial/image13.png
      :width: 5.35851in
      :height: 3.14961in

Figure 12. Descarga de datos en lo Specialized PE de CopernicusLAC

En el espacio de trabajo del archivo, la capa que aparece en la parte superior de la lista es el área de interés inicial definida por los usuarios:

.. image:: ../_static/UC2_tutorial/image14.png
   :width: 5.36131in
   :height: 3.14796in

Figure 13. FFM Workspace – Área de interés


.. image:: ../_static/UC2_tutorial/image15.png
   :width: 5.33524in
   :height: 3.14961in

Figure 14. FFM Workspace – Mapas de extensión de inundaciones


.. image:: ../_static/UC2_tutorial/image16.png
   :width: 5.36412in
   :height: 3.14961in

Figure 15. FFM Workspace – Mapa de frecuencia de inundaciones
