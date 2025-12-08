Flood Extent Mapping
=========================================

.. toctree::
   :maxdepth: 4
   :hidden:

   ../detailed_description/flood_event
   ../detailed_description/flood_event_ESP
   ../tutorials/flood_event

**Information content:**

Estimation of the cumulative extent of flood traces using both Sentinel-1 and Sentinel-2 for
observation times over a period around the event start date, provided in the form of
classified Geotiff (flooded, not flooded, permanent water body).
The service is developed by CIMA Foundation and WASDI Sarl.

**Service Description:**

This service focuses on detecting floods over a period around a specific date (event start
date) in a specific Area of Interest (AOI) defined by the user; it uses SAR and Optical Flood
Extent Detection processors developed by CIMA Foundation.
The user specifies an area of interest and sets the start date of the flood event. A default
observation/acquisition period is applied automatically, but it can be adjusted as needed.
The service automatically searches pre- and post-event Sentinel-1 images with the same
geometry and post-event Sentinel-2 images covering the AOI. The service extracts the Land Cover map and Water Bodies map in the same area and triggers
the execution of the SAR Flood Extent Detection and Optical Flood Extent Detection for
each satellite image found.
As a result flood extent maps are generated for each observation and a maximum extent
map is provided as the cumulative sum of these maps.

**Spatial Scale of Observation:**

The service generates high resolution maps using 20m resolution imagery.

**Temporal frequency:**

This is a one off service providing flood extent estimates for a specific observation time using
EO data acquired before and after that time.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood extent mapping service tracks the extent of a flood both during an event and outside of
emergency situations for prevention and risk assessment. It also provides critical input for
the flood depth mapping service.

**Execution Parameters:**

* Area of Interest
* Event Date (Day)

**Input:**

* Sentinel-1 GRD
* Sentinel-2 L2A

**Third Party input:**

* ESA WorldCover - https://esa-worldcover.org
* Copernicus DEM: - https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

**Output Products:**

* SAR-Based Flood Extent Map
* Optical-Based Flood Extent Map
* Combined (max extent and comparative) Flood Extent Maps
