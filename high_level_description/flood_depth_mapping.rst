Flood Depth Mapping
=========================================

.. toctree::
   :maxdepth: 2
   :hidden:

   ../detailed_description/flood_depth_mapping

**Information content:**

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

**Temporal frequency:**

This is a one off service providing flood depth estimates for a specific flood extent map.

**Nature of service:**

This is an open source service.

**Benefit of service:**

The flood depth estimation service computes the maximum depth of flood water in each
pixel. It can be used during a flood event and outside an emergency basis for prevention and
risk assessment. Combined with vulnerability data provides a critical input for infering the
flood impact.

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
