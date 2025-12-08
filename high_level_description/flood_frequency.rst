Flood Frequency Mapping
=========================================

.. toctree::
   :maxdepth: 4
   :hidden:

   ../detailed_description/flood_frequency
   ../detailed_description/flood_frequency_ESP
   ../tutorials/flood_frequency

**Information content:**

Estimation of a series of flood records for a user defined period, typically a season or
multiple years, providing flood extent maps and the frequency map associated to these
records.
The service is developed by CIMA Foundation with WASDI Sarl.

**Service Description:**

This service is applied over a specified time window, potentially spanning a season or
multiple years, to generate a time series of flood extent maps and associated statistics (i.e.,
the empirical flood frequency map). It leverages SAR and Optical Sentinel imagery covering
the Area of Interest (AOI) specified by the user.
Each day that a satellite data is available within the chosen period and AOI, the service
produces a flood map using optical and/or SAR sources, depending on datataking. These
daily maps are then analyzed at the pixel level to determine how frequently each pixel has
been classified as flooded, which is subsequently visualized as an empirical flood frequency
map.

**Spatial Scale of Observation:**

The service generates high resolution maps using 20m resolution imagery.

**Temporal frequency:**

This service provides one-off historical (multitemporal) analysis for a specific Area of Interest
defined by the user.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood frequency mapping service can be used in the risk reduction community in the
broad sense to better understand the hazard, thus informing the risk assessment.

**Execution Parameters:**

* Area of Interest
* Start Date and End Date

**Input:**

* Sentinel-1 GRD
* Sentinel-2 L2A

**Third Party Input:**

* ESA WorldCover - https://esa-worldcover.org
* Copernicus DEM (COP-DEM) - https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

**Output:**

* “Daily” SAR flood extent maps
* “Daily” Optical flood extent maps
* Flood Count Map
* EO Data Count Map
* Empirical Frequency Map

NOTE: daily does not mean every day but every day where at least one SAR or Optical
satellite image is available.
