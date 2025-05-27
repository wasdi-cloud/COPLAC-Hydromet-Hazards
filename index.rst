****************************************************************************
COPLAC HYDROMET HAZARDS
****************************************************************************

1. The Flood event detection service
==============================================

1.1 Service in Specialized PE
---------------------------------------------
**Service Name:**

Flood Extent

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
geometry and post-event Sentinel-2 images covering the AOI. The service extracts the Land
Use / Land Cover (LU/LC) cover map and Water Bodies map in the same area and triggers
the execution of the SAR Flood Extent Detection and Optical Flood Extent Detection for
each satellite image found.
As a result flood extent maps are generated for each observation and a maximum extent
map is provided as the cumulative sum of these maps.

**Spatial Scale of Observation:**

The service generates high resolution maps using 20m resolution imagery.
Temporal frequency:
This is a one off service providing flood extent estimates for a specific observation time using
EO data acquired before and after that time.
**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood mapping service tracks the extent of a flood both during an event and outside of
emergency situations for prevention and risk assessment. It also provides critical input for
the flood depth mapping service.

**Cost range 1 :**

* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

**Execution Parameters:**

* Area of Interest
* Event Date (Day)

**Input:**

* Sentinel-1 GRD
* Sentinel-2 L2A

**Third Party input 2 :**

* ESA WorldCover - https://esa-worldcover.org
* Copernicus DEM: - https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

**Output:**

* SAR-Based Flood Extent Map
* Optical-Based Flood Extent Map
* Combined (max extent) Flood Extent Map

**Scenarios of operations:**

On demand.


1 assume the service is provided from the PE and the price is based on platform operations,
a fee for the maintenance of the service and processing cost, very approximate range values
are sufficient
2 Any input with a dependency on external source (website URL)

1.2 Service in Baseline PE

**Service Name:**

Diachronic flood detection

**Information content:**

Estimation of the cumulateve extent of flood traces using Sentinel-1 for observation times
over a period around the event start date, provided in the form of classified Geotiff (flooded,
not flooded, permanent water body).
The service is co-developed by CIMA Foundation and Indra with Terradue Sarl.

**Service Description:**

This service focuses on detecting floods over a period around a specific date (event start
date) in a specific Area of Interest (AOI) defined by the user; it uses a SAR Flood Extent
Detection processor developed by CIMA Foundation.
The user specifies an area of interest and sets the start date of the flood event. A default
observation/acquisition period is applied automatically, but it can be adjusted as needed.
The service automatically searches pre- and post-event Sentinel-1 images with the same
geometry covering the AOI. The service extracts the Land Use / Land Cover (LU/LC) cover
map and Water Bodies map in the same area and triggers the execution of the SAR Flood
Extent Detection algorithm for the satellite image pairs found.
As a result a SAR-derived flood extent map is generated and provided for each observation.

**Spatial Scale of Observation:**

The service generates high resolution maps using 20m resolution imagery.
Temporal frequency:
This is a one off service providing flood extent estimates for a specific observation time using
EO data acquired before and after that time.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood mapping service tracks the extent of a flood both during an event and outside of
emergency situations for prevention and risk assessment. It also provides critical input for
the flood depth mapping service.
Cost range:

* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

**Execution Parameters:**

Area of Interest
Event Date (Day)

**Input:**

Sentinel-1 GRD

**Third Party Input:**

* ESA WorldCover - https://esa-worldcover.org
* Copernicus DEM - https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

**Output:**

SAR-Based Flood Extent Map

**Scenarios of operations:**

On demand.


2. The Flood Depth Estimation service
==============================================

2.1 Service in Specialized PE
-----------------------------------------------
**Service Name:**

Flood Depth Mapping
Information content (including organization name of provider, this is the caption):
Maps providing the maximum water depth per pixel for a specific flood extent map.
The service is co-developed by LIST and CIMA Foundation, with WASDI Sarl.
**Service Description:**

This service provides high-resolution maps detailing the maximum water depth per pixel for
specific flood extents, using as ancillary layer a Height Above Nearest Drainage (HAND) re-
elaboration of the Copernicus Digital Elevation Model (COP-DEM_GLO-30). The core
algorithm applies dynamic windows to execute the overlaying calculations as adjusted as
possible.
The user must provide as input a flood extent map that is either a Third Party product or the
product generated using the Flood Event Detection service.
**Spatial Scale of Observation:**

The spatial scale/resolution depends on the input flood extent map.
In case the flood extent is extracted from the Flood Event Detection service, then the
resolution will be 20 m.
Temporal frequency:
This is a one off service providing flood depth estimates for a specific flood extent map.
**Nature of service:**

This is an open source service.
**Benefit of service:**
The flood depth estimation service computes the maximum depth of flood water in each
pixel. It can be used during a flood event and outside an emergency basis for prevention and
risk assessment. Combined with vulnerability data provides a critical input for infering the
flood impact.
Cost range:
* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz
**Execution Parameters:**

N/A

**Input:**

Flood extent map
Third Party 

**Input:**

* Height Above Nearest Drainage (HAND): re-elaboration of the Copernicus DigitalElevation Model (COP-DEM)
* Copernicus DEM (COP-DEM) - https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

**Output:**

The flood water depth map is provided as a Georeferenced raster (GeoTIFF), with water
depth expressed in decimetres

**Scenarios of operations:**

On demand.


2.2 Service in Baseline PE
---------------------------------------------------

**Service Name:**

Flood Depth Estimation
Information content (including organization name of provider, this is the caption):
Maps providing the maximum water depth per pixel for a specific flood extent map.
The service is co-developed by LIST and CIMA Foundation, with Terradue and Indra.

**Service Description:**

This service provides high-resolution maps detailing the maximum water depth per pixel for
specific flood extents, using as ancillary layer a Height Above Nearest Drainage (HAND) re-
elaboration of the Copernicus Digital Elevation Model (COP-DEM_GLO-30). The core
algorithm applies an optimized fixed window to execute the overlaying calculations.
The user must provide as input a flood extent map that is either a Third Party product or the
product generated using the Flood Event Detection service.

**Spatial Scale of Observation:**

The spatial scale/resolution depends on the input flood extent map. In case the Flood Event
Detection service is used to generate the flood extent map the resolution will be 20 m.
Temporal frequency:
This is a one off service providing flood depth estimates for a specific flood extent map.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood depth estimation service computes the maximum depth of flood water in each
pixel. It can be used during a flood event and outside an emergency basis for prevention and
risk assessment. Combined with vulnerability data provides a critical input for infering the
flood impact.
Price range:

* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

**Execution Parameters:**

N/A

**Input:**

Flood extent map

**Third Party Input:**

* Height Above the Nearest Drainage (HAND) re-elaboration of the Copernicus DigitalElevation Model (COP - DEM)
* Copernicus DEM (COP-DEM) - https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

**Output:**

The flood water depth map is provided as a Georeferenced raster (GeoTIFF), with water
depth expressed in decimetres

**Scenarios of operations:**

On demand.


3. The Flood Frequency Mapping service
===========================================================
3.1 Service in Specialized PE
---------------------------------------------------
**Service Name:**

Flood Frequency Mapping
Information content (including organization name of provider, this is the caption):
Estimation of a series of flood records for a user defined period, typically a season or
multiple years, providing flood extent maps and the frequency map associated to these
records.
The service is developed by CIMA Foundation with WASDI Sarl.

**Service Description:**

This service is applied over a user-defined time window, potentially spanning a season or
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
Temporal frequency:
This service provides one-off historical (multitemporal) analysis for a specific Area of Interest
defined by the user.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood frequency mapping service can be used in the risk reduction community in the
broad sense to better understand the hazard, thus informing the risk assessment.
Cost range:
* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

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

**Scenarios of operations:**

On demand


3.2 Service in Baseline PE
-------------------------------------------------------------

**Service Name:**

SAR-based Flood Frequency Mapping

**Information content :**

Estimation of a series of flood records for a user defined period, typically a season or
multiple years, providing flood extent maps and the frequency map associated to these
records, using Sentinel-1 imagery.
The service is developed by CIMA Foundation with Terradue Sarl.

**Service Description:**

This service is applied over a user-defined time window, potentially spanning a season or
multiple years, to generate a time series of flood extent maps and associated statistics (i.e.,
the empirical flood frequency map). It leverages Sentinel-1 (SAR) imagery covering the Area
of Interest (AOI) specified by the user.
Each day that Sentinel-1 data is available within the chosen period and AOI, the service
produces a flood map. These “daily” maps are then analyzed at the pixel level to determine
how frequently each pixel has been classified as flooded, which is subsequently visualized
as an empirical flood frequency map.

**Spatial Scale of Observation:**

The service generates high resolution maps using 20m resolution imagery.
Temporal frequency:
This service provides one-off historical (multitemporal) analysis for a specific Area of Interest
defined by the user.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood frequency mapping service can be used in the risk reduction community in the
broad sense to better understand the hazard, thus informing the risk assessment.
Cost range:

* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

**Execution Parameters:**

* Area of Interest
* Start Date and End Date

**Input:**

Sentinel-1 GRD

**Third Party Input:**

* ESA WorldCover - https://esa-worldcover.org
* Copernicus DEM (COP-DEM) - https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

**Output:**

* Selection of“Daily” SAR flood extent maps
* Flood Count Map
* EO Data Count Map
* Empirical Frequency Map

**NOTE:** daily does not mean every day but every day where at least one SAR satellite image
is available.

**Scenarios of operations:**

On demand.


4. The Flood Hazard Mapping service
==============================================================
4.1 Service in Specialized PE
--------------------------------------------------------------

**Service Name:**

Flood Hazard Mapping
Information content (including organization name of provider, this is the caption):
Generation of enhanced flood hazard maps by merging modelled hazard maps from the
GloFAS model and the empirical flood frequency map derived from the Flood Frequency
Mapping service based only Sentinel-1.
The service is co-developed by LIST and CIMA Foundation with WASDI Sarl.

**Service Description:**

The service produces a set of satellite-enhanced Hazard maps by comparing the flood
frequency outputs from the Flood Frequency mapping service with the GloFAS flood Hazard
maps, then adjusting the latter based on these insights. In addition, ancillary computations
are carried out to exclude non-floodable areas from the analysis, ensuring a more accurate
and relevant final product, insensitive to satellite input resolution. The user indicates the
Workspace where the outputs of the Flood Frequency Mapping service are available. The
main benefits are expected for high frequency/low return periods maps.

**Spatial Scale of Observation:**

The spatial scale of the resulting product is idetermined by the GloFAS Model Hazard Maps
used as input, whose resolution is 90 meters.
Temporal frequency:
This service provides one-off re-evaluation of the Hazard maps over the Area covered by the
Empirical Frequency Maps derived from satellite.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood hazard mapping service can be used in the risk reduction community in the broad
sense to better characterise the hazard, thus informing the risk assessment.
Cost range:

* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

**Execution Parameters:**

Area of Interest

**Input:**

Sentinel-1 GRD pairs of tiles overlapping the AOI subsequently acquired in the same orbit geometry, from which are derived:

    * Flood Count Map
    * Data Count Map
    * Empirical Frequency Map

**Third Party Input:**

* ESA WorldCover - https://esa-worldcover.org
* Global Surface Water (GSW) from JRC - https://global-surface-water.appspot.com/
* Global Flood Awareness System (GloFAS) Hazard Maps - https://global-flood.emergency.copernicus.eu/general-information/data-access/

**Output:**

Improved Hazard maps for different return periods

**Scenarios of operations:**

On demand


4.2 Service in Baseline PE
--------------------------------------------------

**Service Name:**

Flood Hazard Mapping

**Information content :**

Generation of enhanced flood hazard maps by merging modelled hazard maps from the
GloFAS model and the empirical flood frequency map derived from the Flod Ferquency
Mapping service based on Sentinel-1.
The service is co-developed by LIST and CIMA Foundation, with Terradue Sarl.

**Service Description:**

The service produces a set of satellite-enhanced Hazard maps by comparing the flood
frequency outputs from the Flood Frequency mapping service with the GloFAS flood Hazard
maps, then adjusting the latter based on these insights. In addition, ancillary computations
are carried out to exclude non-floodable areas from the analysis, ensuring a more accurate
and relevant final product. The user indicates the Workspace where the outputs of the Flood
Frequency Mapping service are available. The main benefits are expected for high
frequency/low return periods maps.

**Spatial Scale of Observation:**

The spatial scale of the resulting product is idetermined by the GloFAS Model Hazard Maps
used as input, whose resolution is 90 meters.
Temporal frequency:
This service provides one-off re-evaluation of the Hazard maps over the Area covered by the
Empirical Frequency Maps derived from satellite.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood hazard mapping service can be used in the risk reduction community in the broad
sense to better characterise the hazard, thus informing the risk assessment.
Cost range:

* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

**Execution Parameters:**

Area of Interest

**Input:**

* Sentinel-1 GRD pairs of tiles overlapping the AOI subsequently acquired in the same orbit geometry, from which are derived:
* Flood Count Map
* Data Count Map
* Empirical Frequency Map

**Third Party Input:**

* ESA WorldCover - https://esa-worldcover.org
* Global Surface Water (GSW) from JRC - https://global-surface-water.appspot.com/
* Global Flood Awareness System (GloFAS) Hazard Maps - https://global-flood.emergency.copernicus.eu/general-information/data-access/

**Output:**

Improved Hazard maps for different return periods

**Scenarios of operations:**

On demand.


5. SAR Features service
==========================================================
**Service Name:**

SAR Features Service - Urban Coherence and Intensity Change Detection

**Information content :**

This service provides a detection of changes using co-pol sigma nought and coherence from
two Sentinel-1 SLC image pairs acquired before or after an event. It provides as output a
built-up area mask and a change detection map (building damage or flood map).
The service is developed by Terradue Sarl.

**Service Description:**

This service employs coherence and amplitude from InSAR processing to provide an
estimation of detected changes from a multi-temporal image stack of co-pol coherence and
intensity images from the Copernicus Sentinel-1 mission. Three application scenarios are
considered:
1. the identification of damaged structures (e.g. after earthquakes or tropical cyclones)
2. the mapping of floods in built-up areas.
3. Other disaster type or impact, TBD
Before executing the service, the user shall choose for which hazard type the change
detection service shall be employed (e.g. flood, or earthquake). Tailored preset formulas and
default service parameters will be applied in the processing according to the user selection.

**Spatial Scale of Observation:**

Same as Sentinel-1 (preprocessed) SLC imagery
Temporal frequency:
This service provides one-off re-evaluation of the Hazard maps over the Area covered by the
Empirical Frequency Maps derived from satellite.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood hazard mapping service can be used in the risk reduction community in the broad
sense to better characterise the hazard, thus informing the risk assessment.

Cost range:
* Main cost components:
* Calculation methodology:
* Value: Yyy Euro/month for zzz

**Execution Parameters:**

* AOI: the geographical region to be analyzed
* Time of the event: The date and time when the event happened
* Hazard type: flood, earthquake, TBD
* Image Segmentation parameters

**Input:**

* Sentinel-1 SLC imagery in TOPSAR (IW and EW) mode with the same radar geometry (incidence angle, orbit path)
* Event pair: a set of two Sentinel-1 SLC images (master and secondary) captured around the event date to assess surface changes.
* Reference pair: A set of two Sentinel-1 SLC images (master and secondary)taken before the event, serving as a baseline for comparison.

**Third Party Input:**

N/A

**Output:**

* Built up area mask in COG format and Polygon vector as GeoJSON
* Change detection map (building damage or flood map) in COG format and Polygonvector as GeoJSON

**Scenarios of operations:**

On demand.