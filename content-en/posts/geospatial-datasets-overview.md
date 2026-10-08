---
title: "What's in D:\\DATA: A Field Guide to Open Geospatial Datasets"
description: "6,106 files and 233 GB spanning terrain, land cover, land surface temperature, nighttime lights, building height, and population. A quick reference to the public datasets involved: who made them, at what resolution, how to cite them, and where the traps are."
date: 2026-10-07
tags: ["Geospatial Data", "Data Notes"]
comments: true
---

I keep a folder at `D:\DATA`: 6,106 files, 233 GB, running from 30-metre terrain to 1-kilometre nighttime lights, from the urban expansion of 1984 to the land cover of 2025. Once a collection gets this big, you start forgetting where each piece came from, what resolution it is, and whose work you are supposed to cite.

This post is my attempt to write that down. **One caveat up front: every parameter below is taken from official documentation and the original papers, not from what happens to be sitting in my folder** — my copy is neither complete nor necessarily current. Where I quote numbers I measured locally, it is only as a cross-check, and I flag it as such.

## 1. Quick reference

| Dataset | Theme | Spatial resolution | Time span | Producer |
|---|---|---|---|---|
| TRIMS LST | All-weather land surface temperature | 1 km | 2000–2024 | National Tibetan Plateau Data Center |
| MODIS LST | Land surface temperature | 1 km | 2000–present | NASA (Terra / Aqua) |
| ECOSTRESS L2 LSTE | Land surface temperature & emissivity | 70 m | 2018–present | NASA / JPL |
| CLCD | Land cover (9 major classes) | 30 m | 1985–2025 | Wuhan University |
| GLC_FCS30D | Land cover (fine classification) | 30 m | 1985–2022 | Aerospace Information Research Institute, CAS |
| PANDA | Artificial nighttime lights | 1 km | 1984–2020 | Tsinghua University et al. |
| CNBH10m | Building height | 10 m | — | Wu et al. (RSE 2023) |
| Landsat C2 L2 | Multispectral + land surface temperature | 30 m (thermal 100 m) | 1982–present | USGS / NASA |
| ASTER GDEM v3 | Digital elevation | 1 arc-second (~30 m) | observed 2000–2013 | NASA / METI |
| SRTM | Digital elevation | 1 arc-second (~30 m) | February 2000 | NASA / NGA |
| WorldPop | Population rasters | 100 m / 1 km | 2015–2030 | University of Southampton |
| OpenStreetMap | Roads, water, railways, admin | vector | continuously updated | OSM community (via Geofabrik) |

## 2. Land surface temperature

### TRIMS LST — solving the "clouds mean no data" problem

Thermal infrared remote sensing has one fatal weakness: clouds. When a satellite sees cloud, the land surface temperature underneath is simply missing. TRIMS LST merges reanalysis data with thermal infrared observations to fill those gaps, producing a spatially seamless, **all-weather** LST product.

- **Full name**: Daily 1-km all-weather land surface temperature dataset for the Chinese landmass and its surrounding areas (TRIMS LST; 2000–2024)
- **Method**: enhanced Reanalysis and Thermal infrared remote sensing Merging (E-RTM); the original RTM method is in Zhang et al. (2021, *Remote Sensing of Environment*)
- **Resolution and frequency**: 1 km, four observations per day (Terra day/night, Aqua day/night)
- **Coverage**: 72°E–135°E, 19°N–55°N, including Hong Kong, Macao and Taiwan; excluding the South China Sea islands
- **Projection**: Albers equal area
- **Values**: stored as integers — **divide the pixel value by 100 to get Kelvin**. Missing data is flagged as 0 (roughly 0.1–0.5% of the total)
- **Naming**: `TRIMS_Terra/Aqua + year + day-of-year + D/N`, e.g. `TRIMS_Aqua2024001D.tif`
- **Accuracy**: against MODIS LST, mean bias is 0.09 K (day) and −0.03 K (night), with bias standard deviations of 1.45 K and 1.17 K. Validated against 19 ground stations, MBE ranges from −2.26 K to 1.73 K and RMSE from 0.80 K to 3.68 K, with no significant difference between clear-sky and cloudy conditions
- **Bonus**: the product also ships MODIS overpass time files (`View_Time`). Raw values run 0–240 with 255 as background; apply the official scale factor to get local solar time (valid 0–24, background 25.5). During production these were converted to UTC
- **DOI**: `10.11888/Meteoro.tpdc.271252`

One trap: the English readme bundled with my copy says **2000–2022**, while the dataset's metadata record has already been updated to **2000–2024**. Confirm which version you actually have before you build anything on it.

### MODIS LST — the layer everything else is built on

TRIMS takes this as its primary input, so it is worth looking at first.

- **Products**: MOD11A1 (Terra) and MYD11A1 (Aqua), Collection 6.1 (v061)
- **Resolution and frequency**: **1 km, daily**. Terra crosses at roughly 10:30 local solar time (day) and 22:30 (night); Aqua at roughly 13:30 and 01:30
- **Science datasets**: `LST_Day_1km` and `LST_Night_1km`, plus `QC_Day` / `QC_Night` quality layers
- **Values**: stored as integers with a **scale factor of 0.02 in Kelvin** — multiply the pixel value by 0.02 to get K. This is one of the classic traps of the field; skip the scale factor and you will be reading "temperatures" of tens of thousands of kelvin
- **Grid**: **sinusoidal**, not a latitude/longitude grid, so reproject before overlaying anything else
- **Licence**: open (NASA LP DAAC)

Its strengths are a continuous, globally consistent record running from 2000 to the present. Its weaknesses are equally clear: **1 km is coarse for urban work**, and **clouds mean missing data**. That is precisely why TRIMS exists — it borrows the spatial correlation structure of MODIS LST and the low-frequency signal from reanalysis data to fill in whatever the clouds hid.

### ECOSTRESS — thermal imaging on an irregular schedule

ECOSTRESS rides on the International Space Station. Because the ISS orbit is not Sun-synchronous, the instrument does **not** cross at a fixed local time. That is both a limitation and the point: it can capture within-day temperature variation, and it can be tasked for rapid response to volcanoes, droughts, and irrigation events.

- **Product**: L2 LSTE (land surface temperature and emissivity), retrieved with the Temperature-Emissivity Separation (TES) method
- **Resolution**: 70 m × 70 m, resampled from an original pixel size of 38 m × 68 m
- **Accuracy**: overall RMSE around 1.07 K against global validation sites, r² > 0.988, MAE around 0.4 K; a separate validation reported uncertainty below 1 K
- **Band structure**: besides LST, L2 LSTE provides five emissivity bands (Emis1–Emis5, uint8, scale factor 0.002, valid range 0.49–1.0) together with quality layers; the official algorithm description is in the LP DAAC ECOSTRESS Level-2 user guide
- **Levels**: L1B GEO (geolocation), L2 LSTE (native swath), L2G LSTE (resampled to the 70 m grid), L2T LSTE (tiled, e.g. `51RTP`)
- **Versions**: my copy has both v001 (`ECOSTRESS_L2_LSTE_...`) and v002 (`ECOv002_L2_LSTE_...`). Use v002
- **Access**: NASA LP DAAC

Note that L2T is a **tiled** product — the `51RTP` in the filename is an MGRS tile reference — while L2G has already been placed on a regular 70 m grid. For time-series work, prefer L2G.

## 3. Land cover and surface characteristics

### CLCD — annual land cover for China

- **Full name**: China Land Cover Dataset
- **Resolution**: 30 m; **annual from 1985 onward**. The official record I checked (National Cryosphere Desert Data Center, published 2023) covers 1985–2022; the newest Zenodo version is labelled through 2025 (v1.0.5)
- **Classes**: nine major types — cropland, forest, shrub, grassland, water, snow/ice, barren, impervious surface, wetland. A `CLCD_classificationsystem.xlsx` class table ships with the data
- **Method**: 335,709 Landsat images on Google Earth Engine; training samples combining stable samples from the China Land Use/Cover Dataset (CLUD) with visual interpretation; a **random forest** classifier, followed by spatiotemporal filtering and logical reasoning as post-processing. After 2022, with USGS no longer maintaining Collection 1, updates switched to Collection 2 SR
- **Projection**: Albers equal area. The proj4 string is
  `+proj=aea +lat_1=25 +lat_2=47 +lat_0=0 +lon_0=105 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs`
  (central meridian 105°E, standard parallels 25°N and 47°N). The `_albert_` / `_albert_province.zip` in the filenames means Albers — it is not a person's name
- **File layout**: a national raster `CLCD_v01_YYYY_albert.tif` plus per-province packages `CLCD_v01_YYYY_albert_province.zip`. Current releases are exported as **Cloud Optimized GeoTIFF** with built-in overviews and a colour table, so they load faster
- **Licence**: **CC BY 4.0**
- **Citation**: Yang, J. & Huang, X. (2021). The 30 m annual land cover and its dynamics in China from 1990 to 2019. *Earth System Science Data*, 13, 3907–3925. DOI: `10.5194/essd-13-3907-2021`; data DOI `10.5281/zenodo.8176941`

CLCD is best understood as **coarse but reliable**. It separates built-up land, cropland and forest cleanly, which makes it excellent for long time-series change detection. It will not, however, distinguish evergreen broadleaved forest from deciduous needle-leaved forest.

### GLC_FCS30D — the fine-classification option

The **D** stands for Dynamic, and this is the most detailed classification system in the whole collection.

- **Full name**: GLC_FCS30D — global 30 m land-cover dynamic monitoring product with a fine classification system
- **Producers**: Liangyun Liu and Xiao Zhang, Aerospace Information Research Institute, Chinese Academy of Sciences
- **Do not confuse it with GLC_FCS30**: `GLC_FCS30` is the earlier product, released for a set of discrete years; `GLC_FCS30D` is its **annual dynamic** successor, with a finer classification and a continuous time series. The filenames differ by a single letter `D` — check carefully which one you have
- **Time span**: **1985–2022**. Before 2000 the update cycle is every five years; **from 2000 onward it is annual**
- **Classification**: 35 sub-categories. Key codes include `10` rainfed cropland, `20` irrigated cropland, `51/52` evergreen broadleaved forest, `71/72` evergreen needle-leaved forest, `120` shrubland, `130` grassland, `190` **impervious surfaces**, `210` **water body**, `220` permanent ice and snow; `0` and `250` are fill values
- **Accuracy**: 80.88% ± 0.27% overall for the basic 10-class system, and 73.24% ± 0.30% for the LCCS level-1 validation system (17 classes)
- **File structure**: each tile is split into two files — `GLC_FCS30D_19851995_5years_*` (3 bands: 1985, 1990, 1995) and `GLC_FCS30D_20002022_*` (**23 bands**: 2000 through 2022). **Band number equals year**; do not just grab band 1
- **Citation**: Zhang, X., Liu, L., Chen, X., Gao, Y., Xie, S., Mi, J. (2021). GLC_FCS30: global land-cover product with fine classification system at 30 m using time-series Landsat imagery. *ESSD*, 13, 2753–2776. DOI: `10.5194/essd-13-2753-2021`. Two companion papers cover GWL_FCS30 (wetlands, 2023) and GISD30 (impervious surfaces, 2022)
- **Data use policy — important**: the official user guide states that if you plan to use the data in a scientific analysis paper, you are **strongly recommended to contact the authors in advance** and to consider their contributions in the acknowledgements or as co-authors. This is not a plain CC licence. Do not assume you can simply help yourself

### PANDA — pushing nighttime lights back to 1984

- **Full name**: A Prolonged Artificial Nighttime-light Dataset of China (1984–2020); abbreviated PANDA
- **Released by**: National Supercomputing Center in Shenzhen, Tsinghua University, the International Research Center of Big Data for Sustainable Development Goals, and the University of Hong Kong. Authors include Lixian Zhang, Zhehao Ren, Bing Xu, Haohuan Fu, Bin Chen, and Peng Gong
- **Resolution and extent**: 1 km, annual, covering China, 37 annual files from 1984 to 2020
- **Why it matters**: DMSP-OLS nighttime lights only start in 1992, VIIRS only in 2012, and the two are not directly comparable. PANDA extends the record back to **1984** on a harmonised basis, which makes it particularly useful for urbanisation and long-term economic activity studies
- **Paper**: *Scientific Data*, 2024. DOI: `10.1038/s41597-024-03223-1` (an ESI highly cited paper)
- **Value characteristics**: stored as integers, with large areas at 0 (no light) and pixel counts falling as brightness rises — a useful sanity check that you are indeed looking at a nighttime lights product

### CNBH10m — putting a number on how tall the buildings are

Building height has long been one of the hardest variables to obtain in urban research: you cannot read it directly off a two-dimensional image, and unlike land cover there is no mature global product. CNBH-10m is **the first 10-metre building height estimate for China**, built by combining multi-source Earth observation data with machine learning.

- **Full name**: CNBH-10m (A first Chinese building height estimate at 10 m resolution)
- **Paper**: Wu, W. et al., *A first Chinese building height estimate at 10 m resolution (CNBH-10 m) using multi-source earth observations and machine learning*, **Remote Sensing of Environment**, 2023
- **Data deposit**: Zenodo (records `7064268` and `7923866`)
- **Measured characteristics**: 10 m resolution, single-band floating point, units presumably metres; tiled on a **3° × 3°** grid with names like `CNBH10m_X121Y29` (X for longitude, Y for latitude), plus a parallel set of EPSG:4326 tiles; projection is UTM (for example 51N, EPSG:32651)
- **Valid pixels are very sparse** — around 3% in a sampled tile — which is exactly what you would expect, since building height only means something inside built-up areas

Two warnings. First, **check how NoData is flagged before you use it**: with data this sparse, voids are easily averaged into your statistics as zeros. Second, I could not open Zenodo in this pass (the site was experiencing an outage), so I did not verify the accuracy figures — **take the RMSE and MAE from the paper itself**, not from second-hand numbers.

## 4. Satellite imagery

### Landsat Collection 2 Level-2 (L2SP)

This is the most "standard" dataset in the collection, and the one most worth depending on long-term.

- **What it is**: Collection 2 Level-2 science products provide both **surface reflectance (SR)** and **surface temperature (ST)**, already atmospherically corrected, so you do not have to start from raw DN values
- **Resolution**: 30 m multispectral; thermal infrared is natively 100 m and is resampled to 30 m in the product (keep this in mind — the real information content is at the 100 m scale)
- **Tiers**: `T1` is Tier 1 (best geometric and radiometric quality, suitable for time series); `T2` is Tier 2 (lower quality, fine for single-date use)
- **Sensors**: Landsat 5 TM (`LT05`), Landsat 7 ETM+ (`LE07`), Landsat 8 OLI/TIRS (`LC08`), Landsat 9 (`LC09`)
- **Naming**: `LXSS_L2SP_PATHROW_YYYYMMDD_PROCESSINGDATE_COLLECTION_TIER_*`. For example, `LC08_L2SP_119039_20200908_20200919_02_T1_...` is Landsat 8, path 119 / row 039, imaged on 2020-09-08
- **Useful bands**: `QA_PIXEL` (cloud mask — essential for time series), `QA_RADSAT` (saturated pixels), `*_ST_B10` (surface temperature)
- **Known issue**: **Landsat 7's Scan Line Corrector failed in May 2003**, producing regular striping (SLC-off). Any post-2003 LE07 scene needs gap-filling or should be avoided
- **Licence**: a work of the US federal government, in the **public domain**

## 5. Terrain

### ASTER GDEM (ASTGTM)

- **Full name**: ASTER Global Digital Elevation Model, produced jointly by NASA and Japan's METI
- **Resolution**: 1 arc-second, roughly 30 m, tiled at 1° × 1° with names like `ASTGTM_N30E119`
- **Coverage**: 83°N to 83°S, global
- **Version**: v3 is the current recommended release
- **Licence**: free and open

### SRTM

- **Full name**: Shuttle Radar Topography Mission, observed over 11 days in February 2000, produced by NASA and NGA
- **Resolution**: 1 arc-second (~30 m, SRTMGL1) and 3 arc-second (~90 m, SRTMGL3); the 1 arc-second global product is now publicly available
- **Format**: `.hgt` is a headerless format — big-endian, 16-bit signed integers, one elevation value per cell, with **−32768 marking voids**. You must supply the projection yourself
- **Licence**: public domain

**Which one should you use?** Both are 30-metre class, but their error characteristics differ. SRTM struggles where there is vegetation or steep terrain (the radar reflects off canopy rather than ground), while ASTER GDEM is noisier in flat areas and where cloud cover was persistent. For terrain analysis, **use both and cross-check** rather than trusting one.

## 6. Population

### WorldPop

WorldPop's real trap is not resolution. It is **version conventions** — several different products for the same country coexist, and they are not interchangeable.

- **Full name**: WorldPop, an open population raster programme led by the University of Southampton, formed in 2013 by merging the AfriPop, AsiaPop and AmeriPop projects
- **Decoding the filename**: take `chn_pop_2024_CN_100m_R2025A_v1.tif` — `chn` China, `pop` population count, `2024` year, `CN` country, `100m` resolution, `R2025A` **release**, `v1` version
- **`R2025A` is a new convention**: it belongs to the **WorldPop Global 2 (Global_2015_2030)** project, which covers **2015–2030 annually**, with 2021 onward being projections based on the 2024 revision of the UN World Population Prospects. That is *not* the older Global_2000_2020 product, which spans 2000–2020. **Before comparing across years or countries, confirm which project your file belongs to**
- **`pop` is not `pd`**: in the filename, `_pop_` is a **population count** while `_pd_` is **population density (people per km²)**. Never mix the two
- **Values and NoData**: Global 2 is Float32, EPSG:4326, with the 1 km version at 30 arc-seconds (0.008333°); **NoData is −99999**
- **Method**: random forest-based dasymetric redistribution; national totals aligned to UN WPP 2024; uninhabitable areas such as water bodies are masked out first, then covariates including nighttime lights, slope, elevation and climate drive the model
- **Licence**: CC BY 4.0
- **Citation**: Bondarenko M. et al., *The spatial distribution of population in 2015–2030 at a resolution of 30 arc (approximately 1 km at the equator) R2025A version v1*, WorldPop, University of Southampton, DOI `10.5258/SOTON/WP00845` (that DOI covers the 1 km product; confirm the 100 m product's own DOI on its product page), plus the customary credit to www.worldpop.org

## 7. Vector base data

### OpenStreetMap (Shapefile packages distributed by Geofabrik)

- **Source**: the OSM community; Geofabrik publishes free per-country and per-province shapefile packages named like `zhejiang-latest-free.shp.zip`
- **Layers**: `gis_osm_roads_free_1` (roads), `gis_osm_water_free_1` (waterways and water bodies), `gis_osm_railways_free_1` (railways), `gis_osm_adminareas_a_free_1` (administrative areas), among others
- **Licence — read this part**: **ODbL 1.0**. Attribution is mandatory, and if you produce a "derivative database" and publish it, you must **share it under the same licence**. Drawing a map in a paper usually only requires attribution; redistributing a clipped road network as a package triggers the share-alike obligation
- **Known problems**: coverage varies sharply between urban and rural areas, tagging is inconsistent, and the road classification scheme does not match Chinese national standards. It is not an authoritative dataset

### Administrative boundaries and the ten-dash line

- **Common sources**: Alibaba Cloud's DataV.GeoAtlas, GADM, Natural Earth, and similar projects (the `中国_省.geojson` / `中国_县.geojson` files fall into this category)
- **A compliance point that matters**: publishing a map in China requires that **territorial integrity** be represented correctly — including the South China Sea islands, South Tibet, and Taiwan — with the **ten-dash line** shown properly (formerly the nine-dash line; maps have generally shown ten segments since 2014). This is a hard requirement, not a stylistic choice
- **The safe route**: use the standard base maps published by the **Ministry of Natural Resources Standard Map Service** (`bzdt.ch.mnr.gov.cn`), or follow its specifications exactly. Generating output straight from a third-party GeoJSON without review is asking for trouble
- The map approval number (审图号) regime applies to publicly published maps; academic figures are well advised to use standard base maps as well

## 8. Using this collection: version pairs and traps

First, the version pairs that are easiest to confuse — there is more "same name, different thing" in this collection than I expected:

| Easily confused | The difference | Which to use |
|---|---|---|
| `GLC_FCS30` / `GLC_FCS30D` | The former covers a set of discrete years; the latter is **annual from 1985 to 2022** with a finer classification | Use D for change detection; either works for single-date mapping |
| WorldPop `Global_2000_2020` / `Global_2015_2030` | Different time spans, and aligned to different UN benchmark revisions (`R2025A` belongs to the latter) | Settle on one project before comparing across years |
| WorldPop `_pop_` / `_pd_` | Population count / population density (people per km²) | `pop` for totals, `pd` for intensity |
| `CLCD_v01` / later releases | v01 is largely built on Landsat Collection 1; updates switched to Collection 2 SR after 2022 | Keep a long time series inside one version to avoid a methodological jump |
| Landsat `T1` / `T2` | Tier 1 has the best geometric and radiometric quality; Tier 2 is lower | Use T1 for time series; use T2 only to fill gaps |
| ECOSTRESS `L2` / `L2G` / `L2T` | Native swath / resampled to the 70 m grid / tiled | Use L2G for time series, L2T for per-tile downloads |
| ASTER GDEM / SRTM | Optical stereo versus radar interferometry, with opposing error characteristics | Take both and cross-check |
| The several ways to write "kelvin" | MODIS ×0.02; TRIMS ÷100; ECOSTRESS has its own scale | Look up the scale factor per product; do not trust memory |

Then the pitfalls themselves:

1. **Mixed projections.** This collection contains Albers equal-area (TRIMS, CLCD), UTM (CNBH, some DEM products), and WGS84 geographic coordinates (PANDA, WorldPop, GLC_FCS30D). Reproject before overlaying, and **always compute areas in an equal-area projection.**
2. **Values are not what they look like.** TRIMS needs a divide-by-100 to reach Kelvin; MODIS needs a scale factor; `View_Time` needs × 0.1 and then must be read as UTC hours. Skip the scale factor and your results will be nonsense.
3. **NoData is a zoo.** TRIMS uses 0, SRTM uses −32768, PANDA uses −32768, this DEM uses 32767, CLCD uses 0, and WorldPop Global 2 uses −99999. **Harmonise the NoData flag before combining datasets**, or a legitimate zero will be averaged into your statistics as missing data — or worse, the other way round.
4. **Time conventions differ.** CLCD is calendar-year, Landsat is an acquisition instant, TRIMS is four daily snapshots, PANDA is an annual composite. "The same year" is not strictly comparable across them.
5. **Band index equals year.** In the 23-band GLC_FCS30D file, band number maps to year. Do not assume band 1 is anything other than 2000.
6. **Thermal resolution is not what the grid says.** Landsat thermal data is 100 m resampled onto a 30 m grid. The grid is 30 m; the information is 100 m.

**If you are actually going to combine these layers, the order I would recommend is:**

1. **Fix the projection first.** Pick an equal-area projection (CLCD and TRIMS both use Albers with a central meridian of 105°E in this collection) and reproject every raster into it. **Do all area statistics in that projection** — measuring area on a latitude/longitude grid is asking for trouble.
2. **Then align the grids.** Choose one reference raster (usually the finest and most complete), and resample **discrete** data (land cover, DEM, integer nighttime lights) with **nearest neighbour**; only **continuous** data (LST, population) should use bilinear. **Never run cubic convolution on categorical data** — it will interpolate class codes that do not exist.
3. **Harmonise NoData.** Normalise every dataset's missing value (0 / −32768 / 32767 / −99999) to a single flag — NaN, or one explicit sentinel — before any statistics.
4. **Convert to physical units.** Multiply every DN by its own scale factor so the values become kelvin, metres, people.
5. **Only then do feature engineering and modelling** — normalisation, band combinations, temporal compositing.

Getting the order wrong is painful. **Normalise before harmonising NoData** and your NoData will be treated as a valid extreme value in the scaling. **Model before reprojecting** and you have written resampling error directly into your features.

## 9. Citation and licence cheat sheet

| Dataset | Freely usable? | What you must do |
|---|---|---|
| TRIMS LST | Attribution required | Credit the source and authors; DOI `10.11888/Meteoro.tpdc.271252` |
| ECOSTRESS | Open | Cite the product and LP DAAC |
| CLCD | Open | Cite Yang & Huang (2021) |
| GLC_FCS30D | **Additional conditions** | The user guide recommends **contacting the authors in advance** and acknowledging their contribution or considering co-authorship |
| PANDA | Open | Cite the *Scientific Data* paper and the data center |
| Landsat C2 L2 | **Public domain** | Nothing mandatory; crediting USGS/NASA is good practice |
| ASTER GDEM / SRTM | Open / public domain | Credit NASA, METI, NGA |
| WorldPop | CC BY 4.0 | Attribution |
| OpenStreetMap | **ODbL 1.0** | Attribution; derivative databases must be shared alike |
| Administrative boundaries / standard maps | Depends on source | Check the **map approval number and standard map** requirements before publishing |

## 10. Two local findings (not about the datasets themselves)

While sorting through all this, I ran into two problems that have nothing to do with data quality in general and everything to do with my particular copy:

**1. The 465 MB WorldPop national file is corrupt.** `chn_pop_2024_CN_100m_R2025A_v1.tif` cannot be opened by GDAL or rasterio, reporting `TIFFReadDirectory: Failed to read directory at offset 923851936`. Inspecting the header, the TIFF version field reads 43 (it should be 42), and the first IFD claims 56,480 entries — the classic signature of an interrupted download or storage corruption. Re-download it.

**2. My TRIMS copy has Aqua but no Terra.** The product nominally provides four observations per day (Terra day/night plus Aqua day/night). But every DAY and NIGHT folder here holds 365 `TRIMS_Aqua*` data files alongside 365 `TRIMS_Aqua_Day/Night_View_Time*` overpass-time files — **there is no Terra**. In practice that means two observation times per day, not the four the product advertises. Terra would have to be fetched separately.

---

## 11. Appendix: which folder holds which dataset

Since this post is meant to introduce `D:\DATA`, here is the mapping. **The left column is only how the folders happen to be organised; the right column is the dataset's actual identity** — the same data under a different folder name is still the same data, so do not treat folder structure as a property of the dataset.

| Local folder | Dataset |
|---|---|
| `Boundary/` | Administrative boundaries (China provinces/counties, countries, ten-dash line) plus self-made study-area extents |
| `DEM/` | ASTER GDEM v3 (`ASTGTM_*` tiles) + SRTM (`.hgt`) + derived slope / aspect |
| `CNBH10m/` | CNBH-10m building height |
| `Land_cover/CLCD/` | CLCD annual land cover, by province |
| `Land_cover/GLC_FCS30/` | GLC_FCS30 and GLC_FCS30D |
| `PANDA_China/` | PANDA nighttime lights (1984–2020) |
| `Pop/` | WorldPop (Global 2 / R2025A) |
| `TRIMS/` | TRIMS LST, daily 1 km all-weather land surface temperature |
| `ECOSTRESS/` | ECOSTRESS L1B GEO / L2 LSTE / L2G / L2T |
| `Landsat/` | Landsat 5 / 7 / 8 Collection 2 Level-2 |
| `OSM/` | OpenStreetMap (Geofabrik packages) |
| `LST/` | An empty folder; it used to be where TRIMS reprojection output landed |
| `Products.zip` | Duplicates the contents of `PANDA_China/` |
| `List.xlsx` | A self-made short inventory (25 rows, not covering every dataset — not an authoritative index) |

## 12. Sources

The official entry points I actually consulted, in the order they appear above. Some sites (LP DAAC, Zenodo) were redirecting or briefly unavailable during this pass; if a link breaks, search by DOI.

- **TRIMS LST**: [National Tibetan Plateau Data Center](https://data.tpdc.ac.cn/), DOI `10.11888/Meteoro.tpdc.271252`
- **MODIS LST**: [NASA LP DAAC MOD11A1 v061](https://lpdaac.usgs.gov/products/mod11a1v061/)
- **ECOSTRESS**: [LP DAAC ECO_L2G_LSTE v002](https://lpdaac.usgs.gov/products/eco_l2g_lstev002/); algorithm details in the [ECOSTRESS Level-2 user guide](https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf)
- **CLCD**: [National Cryosphere Desert Data Center record](https://www.ncdc.ac.cn/portal/metadata/9de270f3-b5ad-4e19-afc0-2531f3977f2f) — source of the proj4 string, licence and method description; data DOI `10.5281/zenodo.8176941`, paper DOI `10.5194/essd-13-3907-2021`
- **GLC_FCS30D**: paper [GLC_FCS30, ESSD 2021](https://doi.org/10.5194/essd-13-2753-2021); data published by the Aerospace Information Research Institute, CAS
- **PANDA**: [Scientific Data paper](https://www.nature.com/articles/s41597-024-03223-1) · [data page](https://data.tpdc.ac.cn/en/data/e755f1ba-9cd1-4e43-98ca-cd081b5a0b3e/), DOI `10.1038/s41597-024-03223-1`
- **CNBH-10m**: [Zenodo data deposit](https://zenodo.org/records/7064268); paper in *Remote Sensing of Environment* (2023)
- **Landsat**: [USGS EarthExplorer](https://earthexplorer.usgs.gov/) · [Collection 2 documentation](https://www.usgs.gov/landsat-missions/landsat-collection-2)
- **ASTER GDEM v3**: [LP DAAC ASTGTM v003](https://lpdaac.usgs.gov/products/astgtmv003/)
- **SRTM**: [LP DAAC SRTMGL3 v003](https://lpdaac.usgs.gov/products/srtmgl3v003/)
- **WorldPop**: [Global 2 / R2025A release statement (PDF)](https://data.worldpop.org/repo/prj/Global_2015_2030/R2025A/doc/Global2_Release_Statement_R2025A_v1.pdf), DOI `10.5258/SOTON/WP00845`
- **OpenStreetMap**: [Geofabrik downloads](https://download.geofabrik.de/) · [copyright and licence](https://www.openstreetmap.org/copyright)
- **Standard maps**: [Ministry of Natural Resources Standard Map Service](https://bzdt.ch.mnr.gov.cn/)

*Dataset parameters in this post follow the official documentation and original papers. Sources I actually opened for this pass include: the TRIMS LST official readme and its metadata record at the National Tibetan Plateau Data Center; the official GLC_FCS30D user guide (Aerospace Information Research Institute, CAS); the PANDA paper (Scientific Data, 2024) and the release announcement from the Tsinghua key laboratory; the CLCD metadata record at the National Cryosphere Desert Data Center, which supplied the proj4 string, licence and method description; the FAO catalogue metadata for WorldPop Global 2 / R2025A, which supplied the NoData value, units and citation format; the Remote Sensing of Environment entry for CNBH-10m; and USGS / NASA LP DAAC product documentation. Locally measured values are used only for cross-checking and are labelled as such. Please re-verify versions and DOIs before relying on any of them.*
