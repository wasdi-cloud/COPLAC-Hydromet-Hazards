Flood Hazard Mapping
=========================================

.. toctree::
   :maxdepth: 1
   :hidden:

   ../detailed_description/flood_hazard

**Information content:**

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

**Temporal frequency:**

This service provides one-off re-evaluation of the Hazard maps over the Area covered by the
Empirical Frequency Maps derived from satellite.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood hazard mapping service can be used in the risk reduction community in the broad
sense to better characterise the hazard, thus informing the risk assessment.

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
